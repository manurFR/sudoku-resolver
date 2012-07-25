#!/usr/bin/env python
# -*- coding: UTF8 -*-

from Grid import SIZE

class ObviousResolution:
    """ Most obvious ways of finding the value of a cell.
        If a line, column or 3x3 block contains all numbers but one, the empty cell can only be that remaining number
    """
    def horizontal_obvious(self, grid, x, y):
        """ Check if the whole line except the (x, y) cell has been found.
            Returns 1 and set the number of that cell in that case, returns 0 otherwise.
        """
        for i in range(SIZE):
            if i == x:
                continue
            if len(grid.candidates[i][y]) > 1:
                return 0
            else:
                grid.remove_candidate(x, y, grid.candidates[i][y][0])
        return 1

    def vertical_obvious(self, grid, x, y):
        """ Check if the whole column except the (x, y) cell has been found.
            Returns 1 and set the number of that cell in that case, returns 0 otherwise.
        """
        for j in range(SIZE):
            if j == y:
                continue
            if len(grid.candidates[x][j]) > 1:
                return 0
            else:
                grid.remove_candidate(x, y, grid.candidates[x][j][0])
        return 1

    def block_obvious(self, grid, x, y):
        """ Check if the whole 3x3 block except the (x, y) cell has been found.
            Returns 1 and set the number of that cell in that case, returns 0 otherwise.
        """
        xStartOfBlock = (x / 3) * 3
        yStartOfBlock = (y / 3) * 3
        for i in range(3):
            for j in range(3):
                if xStartOfBlock + i == x and yStartOfBlock + j == y:
                    continue
                candidatesForTheCell = grid.candidates[xStartOfBlock + i][yStartOfBlock + j]
                if len(candidatesForTheCell) > 1:
                    return 0
                else:
                    grid.remove_candidate(x, y, candidatesForTheCell[0])
        return 1

