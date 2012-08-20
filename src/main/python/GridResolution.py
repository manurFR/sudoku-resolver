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
            Return 1 if the cell is solved, 0 otherwise.
        """
        x, y = cell
        logging.debug("Now considering cell ({},{}) - Remaining candidates : {}".format(x, y, self.grid.candidates[x][y]))
        # Trying to find a NAKED SINGLE in this cell
        if self.nakedSingleResolution.horizontal_naked_single(self.grid, x, y) \
             + self.nakedSingleResolution.vertical_naked_single(self.grid, x, y)   \
             + self.nakedSingleResolution.block_naked_single(self.grid, x, y) > 0:
            Stats.increment(self.nakedSingleResolution.__class__.__name__)
            return 1

        # Trying to find a HIDDEN SINGLE in this cell
        if self.hiddenSingleResolution.block_hidden_single(self.grid, x, y) > 0:
            Stats.increment(self.hiddenSingleResolution.__class__.__name__)
            return 1

        return 0
