#!/usr/bin/env python
# -*- coding: UTF8 -*-

from Grid import SIZE

class ObviousResolution:
    """ Very obvious ways of finding the value of a cell.
        If a line, column or 3x3 block contains all numbers but one, the empty cell can only be that remaining number
    """
    def horizontal_singleton(self, grid, x, y):
        """ Check if the whole line except the (x, y) cell has been found.
            In that case, the number of that cell is trivial.
            Returns 1 if the cell's number has been determined, 0 otherwise.
        """
        for i in range(SIZE):
            if i == x:
                continue
            if len(grid.candidates[i][y]) > 1:
                return 0
            else:
                grid.remove_candidate(x, y, grid.candidates[i][y][0])
        return 1
