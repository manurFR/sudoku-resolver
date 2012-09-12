#!/usr/bin/env python
# -*- coding: UTF8 -*-

import logging
import Stats
from Grid import SIZE

class NakedPairsResolution:
    """ Naked Pairs are subsets of two cells in the same row, column or block that have the same two remaining candidates.
        These two candidate digits can then appear only in the two cells : which goes where can not be decided at this time, 
        but these two digits can be removed from the remaining candidates of all the other cells in the same row, column or block.
        Note that a pair of cells in the same block can also be in the same row or in the same column : then the candidates' removal must take place in both.
    """
    def run(self, grid):
        solvedCells = 0
        for x, y in iter(grid):
            if self.vertical_naked_pair(grid, x, y):
                logging.info("Naked Pairs resolution : found value for ({},{}) : {}".format(x, y, grid.get_solution(x, y)))
                Stats.increment(self.__class__.__name__)
                solvedCells += 1
        return solvedCells

    def vertical_naked_pair(self, grid, x, y):
        return 0


