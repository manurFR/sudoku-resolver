#!/usr/bin/env python
# -*- coding: UTF8 -*-

import logging
import Stats
from Grid import SIZE, startCoordinatesOfBlock

class HiddenSingleResolution:
    """ A hidden single is a cell where one digit can only appear in its row, column or block.
        For a given cell, we will only consider the digits from the remaining candidates, so that we don't need to evaluate the digit already solved in its row, column or block.
        This implies that the Naked Single Resolutions MUST have been performed before trying this one, otherwise the results might be incorrect.
    """
    def run(self, grid):
        solvedCells = 0
        for x, y in iter(grid):
            if self.block_hidden_single(grid, x, y) or self.horizontal_hidden_single(grid, x, y) or self.vertical_hidden_single(grid, x, y):
                logging.info("Hidden Single resolution : found value for ({},{}) : {}".format(x, y, grid.get_solution(x, y)))
                Stats.increment(self.__class__.__name__)
                solvedCells += 1
        return solvedCells

    def block_hidden_single(self, grid, x, y):
        """ For each of the remaining candidates in the (x, y) cell, determine if there is no other cell in the same block having the same digit among its remaining candidates.
            If not, since each digit must appear once in each block, it means that cell must hold that digit.
            Returns True if such a hidden single was found in this cell, False otherwise.
        """
        if grid.get_solution(x, y):
            return False
        (xBlock, yBlock) = startCoordinatesOfBlock(x, y)
        for digit in grid.candidates[x][y]:
            notFound = True
            for i in range(3):
                for j in range(3):
                    if xBlock + i == x and yBlock + j == y:
                        continue
                    if digit in grid.candidates[xBlock + i][yBlock + j]:
                        notFound = False
                        break
            if notFound:
                grid.set(x, y, digit)
                return True
        return False

    def horizontal_hidden_single(self, grid, x, y):
        """ For each of the remaining candidates in the (x, y) cell, determine if there is no other cell in the same row having the same digit among its remaining candidates.
            If not, since each digit must appear once in each row, it means that cell must hold that digit.
            Returns True if such a hidden single was found in this cell, False otherwise.
        """
        if grid.get_solution(x, y):
            return False
        for digit in grid.candidates[x][y]:
            notFound = True
            for i in range(SIZE):
                if i == x:
                    continue
                if digit in grid.candidates[i][y]:
                    notFound = False
                    break
            if notFound:
                grid.set(x, y, digit)
                return True
        return False

    def vertical_hidden_single(self, grid, x, y):
        """ For each of the remaining candidates in the (x, y) cell, determine if there is no other cell in the same column having the same digit among its remaining candidates.
            If not, since each digit must appear once in each column, it means that cell must hold that digit.
            Returns True if such a hidden single was found in this cell, False otherwise.
        """
        if grid.get_solution(x, y):
            return False
        for digit in grid.candidates[x][y]:
            notFound = True
            for j in range(SIZE):
                if j == y:
                    continue
                if digit in grid.candidates[x][j]:
                    notFound = False
                    break
            if notFound:
                grid.set(x, y, digit)
                return True
        return False
