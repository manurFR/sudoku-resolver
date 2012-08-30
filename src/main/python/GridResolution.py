#!/usr/bin/env python
# -*- coding: UTF8 -*-

import logging
import Stats
from Grid import Grid
from NakedSingleResolution import NakedSingleResolution
from HiddenSingleResolution import HiddenSingleResolution

STRATEGIES = [NakedSingleResolution(), HiddenSingleResolution()]

class GridResolution:
    def __init__(self, grid, strategies=STRATEGIES):
        self.grid = grid
        self.strategies = strategies

    def solve(self):
        """ Try to solve the grid by applying each "strategy" of resolution in series until the whole grid is solved or no strategy can find new digits anymore.
            - The "Naked Single" resolution is actually the process by which each solved digit is removed from the remaining candidates in all the other cells in the same row, column and block.
               Thus it must always be performed first (to process the starting clues) and then after any other strategy has found at least one new digit.
            - The strategies are performed in order of ascending difficulty (for a human being, not a computer, and that order remains subjective), always starting by Naked Single, and
               always cycling back to Naked Single each time a strategy finds at least one new digit.
            - Each resolution has the choice to be implemented by cycling over each cell of the grid and applying a solving algorithm for that cell, or by any other way.
               x It MUST implement a method called run(grid) taking a Grid as argument ;
               x That method MUST return the number of cells the strategy has solved during this pass (or 0 if none).

            Returns True if the grid has been solved, False if the application wasn't able to solve it.
        """
        passCounter = 0
        while True:
            passCounter += 1
            logging.debug("Pass #{}".format(passCounter))

            for stg in self.strategies:
                if stg.run(self.grid) > 0:
                    if self.grid.is_solved():
                        return True 
                    else:
                        break # don't go on to the next strategy ; start a new pass beginning with NakedSingleResolution
            else:
                # No strategy has solved any cell during this pass. The grid will go unsolved.
                return False

    def consider_cell(self, cell):
        """ Perform all known resolutions on the cell to try to solve its value.
            If one of the resolutions is successful, it will return 1.
            Return True if the cell is solved, False otherwise.
        """
        x, y = cell
        logging.debug("Now considering cell ({},{}) - Remaining candidates : {}".format(x, y, self.grid.candidates[x][y]))
        # Trying to find a NAKED SINGLE in this cell
        if self.nakedSingleResolution.horizontal_naked_single(self.grid, x, y)    \
             or self.nakedSingleResolution.vertical_naked_single(self.grid, x, y) \
             or self.nakedSingleResolution.block_naked_single(self.grid, x, y):
            logging.info("Naked Single resolution : found value for ({},{}) : {}".format(x, y, self.grid.get_solution(x, y)))
            Stats.increment(self.nakedSingleResolution.__class__.__name__)
            return True

        # Trying to find a HIDDEN SINGLE in this cell
        if self.hiddenSingleResolution.block_hidden_single(self.grid, x, y)          \
            or self.hiddenSingleResolution.horizontal_hidden_single(self.grid, x, y) \
            or self.hiddenSingleResolution.vertical_hidden_single(self.grid, x, y):
            Stats.increment(self.hiddenSingleResolution.__class__.__name__)
            return True

        return False
