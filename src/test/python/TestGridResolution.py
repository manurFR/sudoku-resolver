#!/usr/bin/env python
# -*- coding: UTF8 -*-

import unittest
from StringIO import StringIO
from Grid import Grid
from GridResolution import GridResolution

class MockStrategy:
    def __init__(self, solving):
        self.solving = solving

    def run(self, grid):
        return 1 if self.solving else 0

class MockGrid:
    def __init__(self, callsBeforeSolved):
        self.callsBeforeSolved = callsBeforeSolved

    def is_solved(self):
        self.callsBeforeSolved -= 1
        return True if self.callsBeforeSolved == 0 else False

class TestGridResolution(unittest.TestCase):
    def test_solve_strategies_successful_and_grid_solved(self):
        gridResolution = GridResolution(grid=Grid(StringIO("415638972\n362479185\n789215364\n926341758\n138756429\n574982631\n257164893\n843597216\n691823547\n")), strategies=[MockStrategy(False), MockStrategy(True)])
        self.assertTrue(gridResolution.solve())

    def test_solve_strategies_unsuccessful(self):
        gridResolution = GridResolution(grid=Grid(), strategies=[MockStrategy(False)])
        self.assertFalse(gridResolution.solve())

    def test_solve_in_many_passes(self):
        grid = MockGrid(3)
        gridResolution = GridResolution(grid=grid, strategies=[MockStrategy(True)])
        self.assertTrue(gridResolution.solve())

if __name__ == "__main__":
    unittest.main()
