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
    def horizontal_locked_candidates(self, grid, x, y):
        """ For each of the remaining candidates in the (x, y) cell, determine if at least one of the other two cells in the same row from the same block also feature
             this candidate, AND that no other cell in the same block feature the same candidate.
            If it is the case, remove this candidate digit from the remaining candidates of all the cells in the x row outside of the block.
            Returns the number of solved cells in this process.
        """
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

