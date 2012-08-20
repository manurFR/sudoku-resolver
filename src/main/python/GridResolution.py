#!/usr/bin/env python
# -*- coding: UTF8 -*-

import logging
import Stats
from Grid import Grid
from NakedSingleResolution import NakedSingleResolution
from HiddenSingleResolution import HiddenSingleResolution

class GridResolution:
    def __init__(self, grid):
        self.grid = grid
        self.nakedSingleResolution = NakedSingleResolution()
        self.hiddenSingleResolution = HiddenSingleResolution()

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
        if self.hiddenSingleResolution.block_hidden_single(self.grid, x, y):
            Stats.increment(self.hiddenSingleResolution.__class__.__name__)
            return True

        return False
