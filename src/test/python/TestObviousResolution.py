#!/usr/bin/env python
# -*- coding: UTF8 -*-

import unittest
from ObviousResolution import ObviousResolution
from Grid import Grid
from StringIO import StringIO

class TestObviousResolution(unittest.TestCase):
    def setUp(self):
        self.obviousResolution = ObviousResolution()

    def test_horizontal_obvious(self):
        grid = Grid(StringIO(".........\n.23456789\n.........\n.234.6789\n.........\n.........\n.........\n.........\n.........\n"))
        self.assertEqual(1, self.obviousResolution.horizontal_obvious(grid, 0, 1))
        self.assertEqual(0, self.obviousResolution.horizontal_obvious(grid, 0, 3))
        self.assertEqual(".........\n123456789\n.........\n.234.6789\n.........\n.........\n.........\n.........\n.........\n", grid.display())

    def test_vertical_obvious(self):
        grid = Grid(StringIO("...1..9..\n...2..8..\n...3.....\n......6..\n...5..5..\n...6..4..\n......3..\n...8..2..\n...9..1..\n"))
        self.assertEqual(1, self.obviousResolution.vertical_obvious(grid, 6, 2))
        self.assertEqual(0, self.obviousResolution.vertical_obvious(grid, 3, 3))
        self.assertEqual("...1..9..\n...2..8..\n...3..7..\n......6..\n...5..5..\n...6..4..\n......3..\n...8..2..\n...9..1..\n", grid.display())

    def test_block_obvious(self):
        grid = Grid(StringIO("...123...\n...456...\n...78....\n1.3......\n.56......\n789......\n.........\n.........\n.........\n"))
        self.assertEqual(1, self.obviousResolution.block_obvious(grid, 5, 2))
        self.assertEqual(0, self.obviousResolution.block_obvious(grid, 1, 3))
        self.assertEqual("...123...\n...456...\n...789...\n1.3......\n.56......\n789......\n.........\n.........\n.........\n", grid.display())

if __name__ == '__main__':
    unittest.main()
