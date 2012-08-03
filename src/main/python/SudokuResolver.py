#!/usr/bin/env python
# -*- coding: UTF8 -*-

import sys, argparse, logging
from SudokuResolverExceptions import SudokuResolverException
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

def main():
    parser = argparse.ArgumentParser(description="A sudoku resolver")
    parser.add_argument("-v", "--verbose", action="count", default=0, help="increase output verbosity (-vv or --verbose=2 for even more verbosity)")
    parser.add_argument("inputGrid", type=argparse.FileType('r'), default=sys.stdin, help="a file containing the grid to solve")
    args = parser.parse_args()

    logLevel = [logging.WARNING, logging.INFO, logging.DEBUG][args.verbose]
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logLevel)

    resolver = SudokuResolver()
    resolver.load(args.inputGrid)
    print resolver.solve()
    print resolver.grid.display()

    args.inputGrid.close()

if __name__ == "__main__":
    try:
        main()
    except SudokuResolverException as ex:
        logging.error(ex.message)

