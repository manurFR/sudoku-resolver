#!/usr/bin/env python
# -*- coding: UTF8 -*-

import logging
import Stats
from Grid import SIZE

class LockedCandidatesResolution:
    """ Locked candidates (also known as Pointed Pairs or Pointed Triples) are two or three aligned cells inside a block who share a same remaining candidate, and that
         digit is not a remaining candidate in any other cell of the block. Since a block must feature each digit, that candidate must appear on this alignment of two or
         three cells. Consequently, it can not appear on any other cell of the same row or column. The corresponding candidates can be removed.
        This resolution will only infrequently lead to solving cells, but it may remove remaining candidates that otherwise prevent other resolution methods to succeed.
    """
    def run(self, grid):
        solvedCells = 0
        for xBlock in [0, 3, 6]:
            for yBlock in [0, 3, 6]:
                solvedCells += self.horizontal_locked_candidates(grid, xBlock, yBlock) + self.vertical_locked_candidates(grid, xBlock, yBlock)
        Stats.increment(self.__class__.__name__, solvedCells)
        return solvedCells

    def horizontal_locked_candidates(self, grid, xBlock, yBlock):
        """ For each of the 9 digits not already solved in the (xBlock, yBlock) block, check if this digit is included in the remaining candidates
             of two or three cells in a row, AND not included in the remaining candidates of the other two rows.
            If it is the case, remove this digit from the remaining candidates of all the cells in the same row outside of the block.
            Returns the number of cells solved by this process.
        """
        digits = self.remaining_candidates_in_block(grid, xBlock, yBlock)
        if not digits:
            return 0

        solvedCells = 0
        for d in digits:
            occurrences = dict.fromkeys(range(yBlock, yBlock+3), 0)
            rowsWhereThisDigitIsPresent = set()
            rowsWhereThisDigitIsPresentTwiceOrThrice = set()
            for row in range(yBlock, yBlock+3):
                for col in range(xBlock, xBlock+3):
                    if d in grid.candidates[col][row]:
                        if row in rowsWhereThisDigitIsPresent:
                            rowsWhereThisDigitIsPresentTwiceOrThrice.add(row)
                        else:
                            rowsWhereThisDigitIsPresent.add(row)
            if len(rowsWhereThisDigitIsPresentTwiceOrThrice) == 1 and len(rowsWhereThisDigitIsPresent) == 1: # if there is one and only one row with 2 or 3 cells featuring the current digit as remaining candidate...
                rowToProcess = rowsWhereThisDigitIsPresentTwiceOrThrice.pop()
                for i in range(SIZE):
                    if (i < xBlock or i > xBlock + 2) and d in grid.candidates[i][rowToProcess]:
                        logging.debug("Locked Candidates resolution (horizontal) : removing candidate {} in ({},{}) thanks to locked candidates in block ({},{})".format(d, i, rowToProcess, xBlock, yBlock))
                        grid.remove_candidate(i, rowToProcess, d)
                        if grid.get_solution(i, rowToProcess) != None:
                            logging.info("Locked Candidates resolution : found value for ({},{}) : {}".format(i, rowToProcess, grid.get_solution(i, rowToProcess)))
                            solvedCells += 1
        return solvedCells

    def vertical_locked_candidates(self, grid, xBlock, yBlock):
        """ For each of the 9 digits not already solved in the (xBlock, yBlock) block, check if this digit is included in the remaining candidates

             of two or three cells in a column, AND not included in the remaining candidates of the other two columns.
            If it is the case, remove this digit from the remaining candidates of all the cells in the same column outside of the block.
            Returns the number of cells solved by this process.
        """
        digits = self.remaining_candidates_in_block(grid, xBlock, yBlock)
        if not digits:
            return 0

        solvedCells = 0
        for d in digits:
            occurrences = dict.fromkeys(range(yBlock, yBlock+3), 0)
            colsWhereThisDigitIsPresent = set()
            colsWhereThisDigitIsPresentTwiceOrThrice = set()
            for col in range(xBlock, xBlock+3):
                for row in range(yBlock, yBlock+3):
                    if d in grid.candidates[col][row]:
                        if col in colsWhereThisDigitIsPresent:
                            colsWhereThisDigitIsPresentTwiceOrThrice.add(col)
                        else:
                            colsWhereThisDigitIsPresent.add(col)
            if len(colsWhereThisDigitIsPresentTwiceOrThrice) == 1 and len(colsWhereThisDigitIsPresent) == 1: # if there is one and only one column with 2 or 3 cells featuring the current digit as remaining candidate...
                colToProcess = colsWhereThisDigitIsPresentTwiceOrThrice.pop()
                for i in range(SIZE):
                    if (i < yBlock or i > yBlock + 2) and d in grid.candidates[colToProcess][i]:
                        logging.debug("Locked Candidates resolution (vertical) : removing candidate {} in ({},{}) thanks to locked candidates in block ({},{})".format(d, colToProcess, i,  xBlock, yBlock))
                        grid.remove_candidate(colToProcess, i, d)
                        if grid.get_solution(colToProcess, i) != None:
                            logging.info("Locked Candidates resolution : found value for ({},{}) : {}".format(colToProcess, i, grid.get_solution(colToProcess, i)))
                            solvedCells += 1
        return solvedCells

    def remaining_candidates_in_block(self, grid, xBlock, yBlock):
        """ Returns the sorted list of all the digits still not solved in a block """
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in range(xBlock, xBlock+3):
            for y in range(yBlock, yBlock+3):
                if grid.get_solution(x, y) in digits:
                    digits.remove(grid.get_solution(x, y))
        return digits
