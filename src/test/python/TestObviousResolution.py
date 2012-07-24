#!/usr/bin/env python
# -*- coding: UTF8 -*-

import unittest
from ObviousResolution import ObviousResolution
from Grid import Grid
from StringIO import StringIO

class TestObviousResolution(unittest.TestCase):
    def setUp(self):
        self.obviousResolution = ObviousResolution()

    def test_horizontal_singleton(self):
        grid = Grid(StringIO(".........\n.23456789\n.........\n.234.6789\n.........\n.........\n.........\n.........\n.........\n"))
        self.assertEqual(1, self.obviousResolution.horizontal_singleton(grid, 0, 1))
        self.assertEqual(0, self.obviousResolution.horizontal_singleton(grid, 0, 3))
        self.assertEqual(".........\n123456789\n.........\n.234.6789\n.........\n.........\n.........\n.........\n.........\n", grid.display())

if __name__ == '__main__':
    unittest.main()
