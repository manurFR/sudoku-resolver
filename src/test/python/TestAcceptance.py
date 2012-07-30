#!/usr/bin/env python
# -*- coding: UTF8 -*-

import unittest
from StringIO import StringIO
from SudokuResolver import SudokuResolver

class TestAcceptance(unittest.TestCase):
    def setUp(self):
        self.resolver = SudokuResolver()

    def test_grid_with_only_naked_single(self):
        self.resolver.load(StringIO(".........\n.1.2.3.4.\n...456...\n.47...89.\n..2.7.6..\n.98...75.\n...684...\n.3.7.1.6.\n.........\n"))
        self.assertTrue(self.resolver.solve())
        self.assertEqual("425817936\n716293548\n983456271\n147365892\n352978614\n698142753\n571684329\n839721465\n264539187\n", self.resolver.grid.display());

if __name__ == '__main__':
    unittest.main()
