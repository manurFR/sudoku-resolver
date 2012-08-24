#!/usr/bin/env python
# -*- coding: UTF8 -*-

import unittest, logging
from StringIO import StringIO
from SudokuResolver import prepareGrid
from GridResolution import GridResolution

@unittest.skip("")
class TestAcceptance(unittest.TestCase):
    def test_grid_with_only_naked_single(self):
        grid = prepareGrid(gridAsString="..........1.2.3.4....456....47...89...2.7.6...98...75....684....3.7.1.6..........")
        self.assertTrue(GridResolution(grid).solve())
        self.assertEqual("425817936\n716293548\n983456271\n147365892\n352978614\n698142753\n571684329\n839721465\n264539187\n", grid.display())

    def test_grid_with_only_hidden_single(self):
        grid = prepareGrid(gridAsString="1..2..3...2..1..4...3..5..67..6..5...5..8..7...8..4..18..7..4...3..6..2...9..2..7")
        self.assertTrue(GridResolution(grid).solve())
        self.assertEqual("186247395925316748473895216791623584354981672268574931812759463537468129649132857", grid.display(lineBreak=False))

if __name__ == '__main__':
    unittest.main()
