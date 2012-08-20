#!/usr/bin/env python
# -*- coding: UTF8 -*-

import unittest
from StringIO import StringIO
from Grid import Grid
from GridResolution import GridResolution

class TestGridResolution(unittest.TestCase):
    def test_consider_cell_naked_single(self):
        gridResolution = GridResolution(Grid(StringIO("1........\n...2.3.4.\n..9......\n.........\n.5.......\n.........\n.6.......\n.........\n.7.......\n")))
        self.assertEqual(True, gridResolution.consider_cell([1, 1]))
        self.assertEqual(8, gridResolution.grid.get_solution(1, 1))

if __name__ == "__main__":
    unittest.main()
