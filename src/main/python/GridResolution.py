#!/usr/bin/env python
# -*- coding: UTF8 -*-

import logging
from NakedSingleResolution import NakedSingleResolution
from HiddenSingleResolution import HiddenSingleResolution
from LockedCandidatesResolution import LockedCandidatesResolution

STRATEGIES = [NakedSingleResolution(), HiddenSingleResolution(), LockedCandidatesResolution()]

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
            logging.debug("\n\n")
            logging.debug("Pass #{}\n=======".format(passCounter))
            logging.debug("Starting grid:\n{}".format(self.grid.display()))

            for stg in self.strategies:
                if stg.run(self.grid) > 0:
                    if self.grid.is_solved():
                        return True 
                    else:
                        break # don't go on to the next strategy ; start a new pass beginning with NakedSingleResolution
            else:
                # No strategy has solved any cell during this pass. The grid will go unsolved.
                return False

