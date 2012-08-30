#!/usr/bin/env python
# -*- coding: UTF8 -*-

import logging
import Stats
from Grid import SIZE, startCoordinatesOfBlock

def log_removals(how, removed_candidates, x, y):
    if removed_candidates:
        logging.debug("Naked Single resolution ({} pass) : removed candidate{} {} from ({},{})".format(how, 's' if len(removed_candidates)>1 else '', removed_candidates, x, y))

class NakedSingleResolution:
    """ A naked single is a cell with only one remaining candidate value after exclusion of all the other values because they are featured on the same line, column or 3x3 block.
        The most obvious resolution of a line, column or 3x3 block that contains all numbers but one is a special case of naked single resolution.

        But even if a pass doesn't solve any cell, this resolution is crucial because it propagates the new constraints brought by newly solved cells.
        Thus it will be run at the start of the program (the initial clues being the solved cells to propagate), and after any other resolution has solved at least one cell.
    """
    def run(self, grid):
        solvedCells = 0
        for x, y in iter(grid):
            if self.horizontal_naked_single(grid, x, y) or self.vertical_naked_single(grid, x, y) or self.block_naked_single(grid, x, y):
                logging.info("Naked Single resolution : found value for ({},{}) : {}".format(x, y, grid.get_solution(x, y)))
                Stats.increment(self.__class__.__name__)
                solvedCells += 1
        return solvedCells

    def horizontal_naked_single(self, grid, x, y):
        """ Remove from the (x, y) cell all the candidates that are already present on the same line.
            Returns True if the cell is solved (ie has only one remaining candidate) after this process, False otherwise.
        """
        if grid.get_solution(x, y):
            return 0
        removed_candidates = []
        for i in range(SIZE):
            if i == x:
                continue
            peer = grid.get_solution(i, y)
            if peer and peer in grid.candidates[x][y]:
                removed_candidates.append(peer)
                grid.remove_candidate(x, y, peer)
        log_removals("horizontal", removed_candidates, x, y)
        return grid.get_solution(x, y) != None

    def vertical_naked_single(self, grid, x, y):
        """ Remove from the (x, y) cell all the candidates that are already present on the same column.
            Returns True if the cell is solved (ie has only one remaining candidate) after this process, False otherwise.
        """
        if grid.get_solution(x, y):
            return 0
        removed_candidates = []
        for j in range(SIZE):
            if j == y:
                continue
            peer = grid.get_solution(x, j)
            if peer and peer in grid.candidates[x][y]:
                removed_candidates.append(peer)
                grid.remove_candidate(x, y, peer)
        log_removals("vertical", removed_candidates, x, y)
        return grid.get_solution(x, y) != None

    def block_naked_single(self, grid, x, y):
        """ Remove from the (x, y) cell all the candidates that are already present on the same 3x3 block.
            Returns True if the cell is solved (ie has only one remaining candidate) after this process, False otherwise.
        """
        if grid.get_solution(x, y):
            return 0
        xBlock, yBlock = startCoordinatesOfBlock(x, y)
        removed_candidates = []
        for i in range(3):
            for j in range(3):
                if xBlock + i == x and yBlock + j == y:
                    continue
                peer = grid.get_solution(xBlock + i, yBlock + j)
                if peer and peer in grid.candidates[x][y]:
                    removed_candidates.append(peer)
                    grid.remove_candidate(x, y, peer)
        log_removals("block", removed_candidates, x, y)
        return grid.get_solution(x, y) != None

