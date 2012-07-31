#!/usr/bin/env python
# -*- coding: UTF8 -*-

import unittest
from StringIO import StringIO
from SudokuResolver import SudokuResolver

class TestAcceptance(unittest.TestCase):
    def setUp(self):
        self.resolver = SudokuResolver()

    def test_grid_with_only_naked_single(self):
        self.resolver.load(StringIO("..........1.2.3.4....456....47...89...2.7.6...98...75....684....3.7.1.6.........."))
        self.assertTrue(self.resolver.solve())
        self.assertEqual("425817936\n716293548\n983456271\n147365892\n352978614\n698142753\n571684329\n839721465\n264539187\n", self.resolver.grid.display());

if __name__ == '__main__':
    unittest.main()
