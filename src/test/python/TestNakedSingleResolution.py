#!/usr/bin/env python
# -*- coding: UTF8 -*-

import unittest
from NakedSingleResolution import NakedSingleResolution
from Grid import Grid
from StringIO import StringIO

class TestNakedSingleResolution(unittest.TestCase):
    def setUp(self):
        self.nakedSingleResolution = NakedSingleResolution()

    def test_horizontal_naked_single_complete_line(self):
        grid = Grid(StringIO(".........\n.23456789\n.........\n.234.6789\n.........\n.........\n.........\n.........\n.........\n"))
        self.assertEqual(1, self.nakedSingleResolution.horizontal_naked_single(grid, 0, 1))
        self.assertEqual(0, self.nakedSingleResolution.horizontal_naked_single(grid, 0, 3))
        self.assertEqual(".........\n123456789\n.........\n.234.6789\n.........\n.........\n.........\n.........\n.........\n", grid.display())

    def test_vertical_naked_single_complete_column(self):
        grid = Grid(StringIO("...1..9..\n...2..8..\n...3.....\n......6..\n...5..5..\n...6..4..\n......3..\n...8..2..\n...9..1..\n"))
        self.assertEqual(1, self.nakedSingleResolution.vertical_naked_single(grid, 6, 2))
        self.assertEqual(0, self.nakedSingleResolution.vertical_naked_single(grid, 3, 3))
        self.assertEqual("...1..9..\n...2..8..\n...3..7..\n......6..\n...5..5..\n...6..4..\n......3..\n...8..2..\n...9..1..\n", grid.display())

    def test_block_naked_single_complete_block(self):
        grid = Grid(StringIO("...123...\n...456...\n...78....\n1.3......\n.56......\n789......\n.........\n.........\n.........\n"))
        self.assertEqual(1, self.nakedSingleResolution.block_naked_single(grid, 5, 2))
        self.assertEqual(0, self.nakedSingleResolution.block_naked_single(grid, 1, 3))
        self.assertEqual("...123...\n...456...\n...789...\n1.3......\n.56......\n789......\n.........\n.........\n.........\n", grid.display())

    def test_horizontal_naked_single_generic(self):
        grid = Grid(StringIO(".1.2.3.4.\n.........\n.........\n.........\n.........\n.........\n.........\n.........\n.........\n"))
        self.assertEqual(0, self.nakedSingleResolution.horizontal_naked_single(grid, 0, 0))
        self.assertItemsEqual([5,6,7,8,9], grid.candidates[0][0])

    def test_vertical_naked_single_generic(self):
        grid = Grid(StringIO(".1.......\n.2.......\n.........\n.4.......\n.5.......\n.........\n.7.......\n.........\n.9.......\n"))
        self.assertEqual(0, self.nakedSingleResolution.vertical_naked_single(grid, 1, 2))
        self.assertItemsEqual([3,6,8], grid.candidates[1][2])

    def test_block_naked_single_generic(self):
        grid = Grid(StringIO(".12......\n7.8......\n9........\n.........\n.........\n.........\n.........\n.........\n.........\n"))
        self.assertEqual(0, self.nakedSingleResolution.block_naked_single(grid, 0, 0))
        self.assertItemsEqual([3,4,5,6], grid.candidates[0][0])

    def test_naked_single_acceptance(self):
        grid = Grid(StringIO("1........\n...2.3.4.\n..9......\n.........\n.5.......\n.........\n.6.......\n.........\n.7.......\n"))
        self.assertEqual(0, self.nakedSingleResolution.block_naked_single(grid, 1, 1))
        self.assertEqual(0, self.nakedSingleResolution.horizontal_naked_single(grid, 1, 1))
        self.assertEqual(1, self.nakedSingleResolution.vertical_naked_single(grid, 1, 1))
        self.assertEqual(8, grid.get_solution(1, 1))

if __name__ == '__main__':
    unittest.main()
