#!/usr/bin/env python
# -*- coding: UTF8 -*-

import unittest
from NakedPairsResolution import NakedPairsResolution
from Grid import Grid, SIZE
from TestUtils import prepareRemainingCandidates
from StringIO import StringIO

class TestNakedPairsResolution(unittest.TestCase):
    def setUp(self):
        self.nakedPairsResolution = NakedPairsResolution()

    def test_vertical_naked_pair(self):
        grid = Grid(StringIO("..516....\n6...73...\n3....57.6\n....3.691\n139756482\n862491..7\n4.1.....5\n...5....8\n.....72..\n"))
        prepareRemainingCandidates(grid)
        self.assertItemsEqual([2, 4, 7, 8, 9], grid.candidates[1][0])
        self.assertItemsEqual([1, 2, 4, 8, 9], grid.candidates[1][1])
        self.assertItemsEqual([1, 2, 4, 8, 9], grid.candidates[1][2])
        self.assertItemsEqual([4, 8], grid.candidates[2][1])
        self.assertItemsEqual([4, 8], grid.candidates[2][2])
        self.assertEqual(0, self.nakedPairsResolution.vertical_naked_pair(grid, 2, 1))
#        self.assertItemsEqual([2, 7, 9], grid.candidates[1][0])
#        self.assertItemsEqual([1, 2, 9], grid.candidates[1][1])
#        self.assertItemsEqual([1, 2, 9], grid.candidates[1][2])

        
if __name__ == '__main__':
    unittest.main()


