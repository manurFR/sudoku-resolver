#!/usr/bin/env python
# -*- coding: UTF8 -*-

import unittest
from LockedCandidatesResolution import LockedCandidatesResolution
from Grid import Grid, SIZE
from TestUtils import prepareRemainingCandidates
from StringIO import StringIO

class TestLockedCandidatesResolution(unittest.TestCase):
    def setUp(self):
        self.lockedCandidatesResolution = LockedCandidatesResolution()

    def test_row_block_reduction(self):
        grid = Grid(StringIO(".179.36..\n....8....\n9.....5.7\n.72.1.43.\n...4.2.7.\n.6437.25.\n7.1....65\n....3....\n..56.172.\n"))
        prepareRemainingCandidates(grid)
        self.assertItemsEqual([2, 3, 4, 5, 6], grid.candidates[0][1])
        self.assertItemsEqual([2, 3, 4, 5],    grid.candidates[1][1])
        self.assertItemsEqual([3, 6],          grid.candidates[2][1])
        self.assertEqual(1, self.lockedCandidatesResolution.row_block_reduction(grid, 6, 0))
        self.assertItemsEqual([2, 4, 5, 6], grid.candidates[0][1])
        self.assertItemsEqual([2, 4, 5],    grid.candidates[1][1])
        self.assertItemsEqual([6],          grid.candidates[2][1])
        self.assertEqual(".179.36..\n..6.8....\n9.....5.7\n.72.1.43.\n...4.2.7.\n.6437.25.\n7.1....65\n....3....\n..56.172.\n", grid.display())

    def test_column_block_reduction(self):
        grid = Grid(StringIO("000023400004000100050084090601070902793206801000010760000000009800000004060000587"))
        prepareRemainingCandidates(grid)
        self.assertItemsEqual([1, 3, 4, 5, 6, 7, 8], grid.candidates[3][6])
        self.assertItemsEqual([1, 3, 5, 6, 7, 9],    grid.candidates[3][7])
        self.assertItemsEqual([1, 3, 4, 9],          grid.candidates[3][8])
        self.assertEqual(0, self.lockedCandidatesResolution.column_block_reduction(grid, 3, 0))
        self.assertItemsEqual([3, 4, 5, 6, 7, 8], grid.candidates[3][6])
        self.assertItemsEqual([3, 5, 6, 7, 9],    grid.candidates[3][7])
        self.assertItemsEqual([3, 4, 9],          grid.candidates[3][8])

    def test_block_column_reduction(self):
        grid = Grid(StringIO("500200010001900730000000800050020008062039000000004300000000000080467900007300000"))
        prepareRemainingCandidates(grid)
        self.assertItemsEqual([2, 4, 5, 6, 7, 8],    grid.candidates[7][6])
        self.assertItemsEqual([2, 5],                grid.candidates[7][7])
        self.assertItemsEqual([2, 4, 5, 6, 8],       grid.candidates[7][8])
        self.assertItemsEqual([1, 2, 3, 4, 5, 6, 7], grid.candidates[8][6])
        self.assertItemsEqual([1, 2, 3, 5],          grid.candidates[8][7])
        self.assertItemsEqual([1, 2, 4, 5, 6],       grid.candidates[8][8])
        self.assertEqual(1, self.lockedCandidatesResolution.block_column_reduction(grid, 6, 6))
        self.assertItemsEqual([4, 5, 6, 7, 8],    grid.candidates[7][6])
        self.assertItemsEqual([5],                grid.candidates[7][7])
        self.assertItemsEqual([4, 5, 6, 8],       grid.candidates[7][8])
        self.assertItemsEqual([1, 3, 4, 5, 6, 7], grid.candidates[8][6])
        self.assertItemsEqual([1, 3, 5],          grid.candidates[8][7])
        self.assertItemsEqual([1, 4, 5, 6],       grid.candidates[8][8])
        self.assertEqual("5..2...1...19..73.......8...5..2...8.62.39........43............8.46795...73.....", grid.display(lineBreak=False))

    def test_block_row_reduction(self):
        grid = Grid(StringIO(".16..78.3\n.9.8.....\n87...1.6.\n.48...3..\n65...9.82\n239...65.\n.6.9...2.\n.8...2936\n9246..51.\n"))
        prepareRemainingCandidates(grid)
        self.assertItemsEqual([2, 3, 4, 5],    grid.candidates[3][2])
        self.assertItemsEqual([2, 3, 4, 5, 6], grid.candidates[4][1])
        self.assertItemsEqual([2, 3, 4, 5, 9], grid.candidates[4][2])
        self.assertEqual(0, self.lockedCandidatesResolution.block_row_reduction(grid, 3, 0))
        self.assertItemsEqual([3, 4, 5],    grid.candidates[3][2])
        self.assertItemsEqual([3, 4, 5, 6], grid.candidates[4][1])
        self.assertItemsEqual([3, 4, 5, 9], grid.candidates[4][2])
        
if __name__ == '__main__':
    unittest.main()

