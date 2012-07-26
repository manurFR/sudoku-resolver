#!/usr/bin/env python
# -*- coding: UTF8 -*-

from Grid import SIZE

class NakedSingleResolution:
    """ A naked single is a cell with only one remaining candidate value after exclusion of all the other values because they are featured on the same line, column or 3x3 block.
        The most obvious resolution of a line, column or 3x3 block that contains all numbers but one is a special case of naked single resolution.
    """
    def horizontal_naked_single(self, grid, x, y):
        """ Remove from the (x, y) cell all the candidates that are already present on the same line.
            Returns 1 if the cell is solved (ie has only one remaining candidate) after this process, 0 otherwise.
        """
        for i in range(SIZE):
            if i == x:
                continue
            if grid.get_solution(i, y) <> None:
                grid.remove_candidate(x, y, grid.get_solution(i, y))
        return 1 if grid.get_solution(x, y) <> None else 0 

    def vertical_naked_single(self, grid, x, y):
        """ Remove from the (x, y) cell all the candidates that are already present on the same column.
            Returns 1 if the cell is solved (ie has only one remaining candidate) after this process, 0 otherwise.
        """
        for j in range(SIZE):
            if j == y:
                continue
            if grid.get_solution(x, j) <> None:
                grid.remove_candidate(x, y, grid.get_solution(x, j))
        return 1 if grid.get_solution(x, y) <> None else 0 

    def block_naked_single(self, grid, x, y):
        """ Remove from the (x, y) cell all the candidates that are already present on the same 3x3 block.
            Returns 1 if the cell is solved (ie has only one remaining candidate) after this process, 0 otherwise.
        """
        xStartOfBlock = (x / 3) * 3
        yStartOfBlock = (y / 3) * 3
        for i in range(3):
            for j in range(3):
                if xStartOfBlock + i == x and yStartOfBlock + j == y:
                    continue
                cellSolution = grid.get_solution(xStartOfBlock + i, yStartOfBlock + j)
                if cellSolution <> None:
                    grid.remove_candidate(x, y, cellSolution)
        return 1 if grid.get_solution(x, y) <> None else 0 

