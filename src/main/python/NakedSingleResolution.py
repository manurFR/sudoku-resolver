#!/usr/bin/env python
# -*- coding: UTF8 -*-

import logging
from Grid import SIZE, startCoordinatesOfBlock

class NakedSingleResolution:
    """ A naked single is a cell with only one remaining candidate value after exclusion of all the other values because they are featured on the same line, column or 3x3 block.
        The most obvious resolution of a line, column or 3x3 block that contains all numbers but one is a special case of naked single resolution.
    """
    def horizontal_naked_single(self, grid, x, y):
        """ Remove from the (x, y) cell all the candidates that are already present on the same line.
            Returns True if the cell is solved (ie has only one remaining candidate) after this process, False otherwise.
        """
        if grid.get_solution(x, y):
            return 0
        for i in range(SIZE):
            if i == x:
                continue
            peer = grid.get_solution(i, y)
            if peer and peer in grid.candidates[x][y]:
                logging.debug("...removing candidate {} already present on ({},{})".format(peer, i, y))
                grid.remove_candidate(x, y, peer)
        return grid.get_solution(x, y) != None

    def vertical_naked_single(self, grid, x, y):
        """ Remove from the (x, y) cell all the candidates that are already present on the same column.
            Returns True if the cell is solved (ie has only one remaining candidate) after this process, False otherwise.
        """
        if grid.get_solution(x, y):
            return 0
        for j in range(SIZE):
            if j == y:
                continue
            peer = grid.get_solution(x, j)
            if peer and peer in grid.candidates[x][y]:
                logging.debug("...removing candidate {} already present on ({},{})".format(peer, x, j))
                grid.remove_candidate(x, y, peer)
        return grid.get_solution(x, y) != None

    def block_naked_single(self, grid, x, y):
        """ Remove from the (x, y) cell all the candidates that are already present on the same 3x3 block.
            Returns True if the cell is solved (ie has only one remaining candidate) after this process, False otherwise.
        """
        if grid.get_solution(x, y):
            return 0
        xBlock, yBlock = startCoordinatesOfBlock(x, y)
        for i in range(3):
            for j in range(3):
                if xBlock + i == x and yBlock + j == y:
                    continue
                peer = grid.get_solution(xBlock + i, yBlock + j)
                if peer and peer in grid.candidates[x][y]:
                    logging.debug("...removing candidate {} already present on ({},{})".format(peer, xBlock + i, yBlock + j))
                    grid.remove_candidate(x, y, peer)
        return grid.get_solution(x, y) != None

