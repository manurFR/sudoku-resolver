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

    def test_horizontal_locked_candidates(self):
        grid = Grid(StringIO(".179.36..\n....8....\n9.....5.7\n.72.1.43.\n...4.2.7.\n.6437.25.\n7.1....65\n....3....\n..56.172.\n"))
        prepareRemainingCandidates(grid)
        self.assertItemsEqual([2, 3, 4, 5, 6], grid.candidates[0][1])
        self.assertItemsEqual([2, 3, 4, 5], grid.candidates[1][1])
        self.assertItemsEqual([3, 6], grid.candidates[2][1])
        self.assertEqual(1, self.lockedCandidatesResolution.horizontal_locked_candidates(grid, 6, 0))
        self.assertItemsEqual([2, 4, 5, 6], grid.candidates[0][1])
        self.assertItemsEqual([2, 4, 5], grid.candidates[1][1])
        self.assertItemsEqual([6], grid.candidates[2][1])
        self.assertEqual(".179.36..\n..6.8....\n9.....5.7\n.72.1.43.\n...4.2.7.\n.6437.25.\n7.1....65\n....3....\n..56.172.\n", grid.display())

if __name__ == '__main__':
    unittest.main()

