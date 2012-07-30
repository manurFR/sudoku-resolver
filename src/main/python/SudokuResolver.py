#!/usr/bin/env python
# -*- coding: UTF8 -*-

import sys
from Grid import Grid
from GridResolution import GridResolution

class SudokuResolver:
    def load(self, fileToLoad):
        self.grid = Grid(fileToLoad)
        self.gridResolution = GridResolution(self.grid)

    def solve(self):
        """ Iterate on the grid's unsolved cells and perform known resolution algorithms on them
            until the grid is solved or in an unsolved state (which is an information theiterator
            gives us as argument of the StopIteration exception).
            Returns True if the grid has been solved, False if the application wasn't able to solve it.
        """
        try:
            iterOnGrid = iter(self.grid)
            while True:
                self.gridResolution.consider_cell(iterOnGrid.next())
        except StopIteration as stop:
           return stop.args[0]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Usage: SudokuResolver.py <grid.txt>"
        sys.exit(1)

    resolver = SudokuResolver()
    with open(sys.argv[1], 'r') as fileToLoad:
        resolver.load(fileToLoad)
        print resolver.solve()
        print resolver.grid.display()
