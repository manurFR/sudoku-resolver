#!/usr/bin/env python
# -*- coding: UTF8 -*-

import logging
from Grid import SIZE

class NakedSingleResolution:
    """ A naked single is a cell with only one remaining candidate value after exclusion of all the other values because they are featured on the same line, column or 3x3 block.
        The most obvious resolution of a line, column or 3x3 block that contains all numbers but one is a special case of naked single resolution.
    """
    def horizontal_naked_single(self, grid, x, y):
        """ Remove from the (x, y) cell all the candidates that are already present on the same line.
            Returns 1 if the cell is solved (ie has only one remaining candidate) after this process, 0 otherwise.
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
        if grid.get_solution(x, y):
            logging.info("Naked Single resolution : found value for ({},{}) : {}".format(x, y, grid.get_solution(x, y)))
            return 1
        else:
            return 0 

    def vertical_naked_single(self, grid, x, y):
        """ Remove from the (x, y) cell all the candidates that are already present on the same column.
            Returns 1 if the cell is solved (ie has only one remaining candidate) after this process, 0 otherwise.
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
        if grid.get_solution(x, y):
            logging.info("Naked Single resolution : found value for ({},{}) : {}".format(x, y, grid.get_solution(x, y)))
            return 1
        else:
            return 0 

    def block_naked_single(self, grid, x, y):
        """ Remove from the (x, y) cell all the candidates that are already present on the same 3x3 block.
            Returns 1 if the cell is solved (ie has only one remaining candidate) after this process, 0 otherwise.
        """
        if grid.get_solution(x, y):
            return 0
        xStartOfBlock = (x / 3) * 3
        yStartOfBlock = (y / 3) * 3
        for i in range(3):
            for j in range(3):
                if xStartOfBlock + i == x and yStartOfBlock + j == y:
                    continue
                peer = grid.get_solution(xStartOfBlock + i, yStartOfBlock + j)
                if peer and peer in grid.candidates[x][y]:
                    logging.debug("...removing candidate {} already present on ({},{})".format(peer, xStartOfBlock + i, yStartOfBlock + j))
                    grid.remove_candidate(x, y, peer)
        if grid.get_solution(x, y):
            logging.info("Naked Single resolution : found value for ({},{}) : {}".format(x, y, grid.get_solution(x, y)))
            return 1
        else:
            return 0 

