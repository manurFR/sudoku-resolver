#!/usr/bin/env python
# -*- coding: UTF8 -*-

from Grid import Grid
from NakedSingleResolution import NakedSingleResolution

class GridResolution:
    def __init__(self, grid):
        self.grid = grid
        self.nakedSingleResolution = NakedSingleResolution()

    def consider_cell(self, cell):
        """ Perform all known resolutions on the cell to try to solve its value.
            If one of the resolutions is successful, it will return 1.
            Lets return the sum of all resolutions, which will be 1 if the cell is solved, 0 otherwise.
        """
        x, y = cell
        return self.nakedSingleResolution.horizontal_naked_single(self.grid, x, y) \
             + self.nakedSingleResolution.vertical_naked_single(self.grid, x, y)   \
             + self.nakedSingleResolution.block_naked_single(self.grid, x, y)
