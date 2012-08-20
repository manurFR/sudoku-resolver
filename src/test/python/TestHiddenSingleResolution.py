#!/usr/bin/env python
# -*- coding: UTF8 -*-

import unittest
from NakedSingleResolution import NakedSingleResolution
from HiddenSingleResolution import HiddenSingleResolution
from Grid import Grid, SIZE
from StringIO import StringIO

class TestHiddenSingleResolution(unittest.TestCase):
    def setUp(self):
        self.nakedSingleResolution = NakedSingleResolution()
        self.hiddenSingleResolution = HiddenSingleResolution()

    def test_horizontal_hidden_single_in_a_block(self):
        grid = Grid(StringIO(".1...3..8\n...5..9.3\n....29...\n.8....6.9\n279156834\n4.6....7.\n...27....\n3.2..1...\n6..3...9.\n"))
        self.prepareRemainingCandidates(grid)
        self.assertEqual(True, self.hiddenSingleResolution.block_hidden_single(grid, 4, 1))
        self.assertEqual(False, self.hiddenSingleResolution.block_hidden_single(grid, 0, 3))
        self.assertEqual(".1...3..8\n...51.9.3\n....29...\n.8....6.9\n279156834\n4.6....7.\n...27....\n3.2..1...\n6..3...9.\n", grid.display())

    def prepareRemainingCandidates(self, grid):
        for x in range(SIZE):
            for y in range(SIZE):
                self.nakedSingleResolution.horizontal_naked_single(grid, x, y)
                self.nakedSingleResolution.vertical_naked_single(grid, x, y)
                self.nakedSingleResolution.block_naked_single(grid, x, y)

if __name__ == '__main__':
    unittest.main()

