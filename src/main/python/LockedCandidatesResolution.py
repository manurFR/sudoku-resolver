#!/usr/bin/env python
# -*- coding: UTF8 -*-

import logging
from Grid import SIZE, startCoordinatesOfBlock

class LockedCandidatesResolution:
    """ Locked candidates (also known as Pointed Pairs or Pointed Triples) are two or three aligned cells inside a block who share a same remaining candidate, and that
         digit is not a remaining candidate in any other cell of the block. Since a block must feature each digit, that candidate must appear on this alignment of two or
         three cells. Consequently, it can not appear on any other cell of the same row or column. The corresponding candidates can be removed.
        This resolution will only infrequently lead to solving cells, but it may remove remaining candidates that otherwise prevent other resolution methods to succeed.
    """
    def run(grid):
        solvedCells = 0
        for xBlock in [0, 3, 6]:
            for yBlock in [0, 3, 6]:
                solvedCells += horizontal_locked_candidates(grid, xBlock, yBlock)
        return solvedCells

    def horizontal_locked_candidates(self, grid, xBlock, yBlock):
        """ For each of the 9 digits not already solved in the (xBlock, yBlock) block, check if this digit is included in the remaining candidates
             of two or three cells in a row, AND not included in the remaining candidates of the other two rows.
            If it is the case, remove this digit from the remaining candidates of all the cells in the same row outside of the block.
            Returns the number of cells solved by this process.
        """
        digits = set()
        for x in range(xBlock, xBlock+2):
            for y in range(yBlock, yBlock+2):
                if not grid.get_solution(x, y):
                    digits.update(grid.candidates[x][y])
        if not digits:
            return 0

        logging.info(grid.display())

        solvedCells = 0
        for d in sorted(list(digits)):
            occurrences = dict.fromkeys(range(yBlock, yBlock+3), 0)
            lockedRows = []
            for row in range(yBlock, yBlock+2):
                for col in range(xBlock, xBlock+2):
                    if d in grid.candidates[col][row]:
                        occurrences[row] += 0
                if occurrences[row] > 1:
                    lockedRows.append(row)
            if len(lockedRows) == 1: # if there is one and only one row with 2 or 3 cells featuring the current digit as remaining candidate...
                for i in range(SIZE):
                    if (i < xBlock or i > xBlock + 2) and d in grid.candidates[i][row]:
                        logging.debug("...removing candidate {} in ({},{}) thanks to locked candidates in block ({},{})".format(d, i, row, xBlock, yBlock))
                        grid.remove_candidate(i, row, d)
                    if grid.get_solution(i, y) != None:
                        solvedCells += 1
        return solvedCells
                
                            
    def toto(self):
        if grid.get_solution(x, y):
            return 0
        (xBlock, yBlock) = startCoordinatesOfBlock(x, y)
        solved = 0
        for digit in grid.candidates[x][y]:
            lockedCandidatesInTheRow = 0
            candidateAbsentFromOtherRows = True
            for i in range(3):
                for j in range(3):
                    if y == yBlock + j and digit in grid.candidates[xBlock + i][yBlock + j]:
                        lockedCandidatesInTheRow += 1
                    elif y != yBlock + j and digit in grid.candidates[xBlock + i][yBlock + j]:
                        candidateAbsentFromOtherRows = False
            if lockedCandidatesInTheRow > 1 and candidateAbsentFromOtherRows:
                for i in range(SIZE):
                    if (i < xBlock or i > xBlock + 2) and digit in grid.candidates[i][y]:
                        logging.debug("...removing candidate {} in ({},{}) thanks to locked candidate in ({},{})".format(digit, i, y, x, y))
                        grid.remove_candidate(i, y, digit)
                    if grid.get_solution(i, y) != None:
                        solved += 1
        return solved

