#!/usr/bin/env python
# -*- coding: UTF8 -*-

import sys, argparse, logging
import Stats
from SudokuResolverExceptions import SudokuResolverException
from Grid import Grid
from GridResolution import GridResolution


class SudokuResolver:
    def load(self, fileToLoad=None, gridAsString=None):
        self.grid = Grid(fileToLoad, gridAsString)
        self.gridResolution = GridResolution(self.grid)
        if fileToLoad:
            fileToLoad.close()

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
    parser.add_argument("-g", "--grid", help="a grid directly on the command line (9x9 digits and dots, with or without \\n)")
    parser.add_argument("gridAsFile", type=argparse.FileType('r'), nargs='?', help="a file containing the grid to solve")
    args = parser.parse_args()

    if not args.gridAsFile and not args.grid:
        parser.error("A grid must be provided.")

    logLevel = [logging.WARNING, logging.INFO, logging.DEBUG][args.verbose]
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logLevel)

    resolver = SudokuResolver()
    resolver.load(args.gridAsFile, args.grid)
    print "Loaded grid :"
    print resolver.grid.display()
    if resolver.solve():
        logging.info("Grid solved completely !")
    else:
        logging.info("Solving stopped without being able to finish the grid.")
    print "Final grid :"
    print resolver.grid.display()

    logging.info("Distribution of cell solving resolutions :")
    for key, value in Stats.results().iteritems():
        logging.info("  {}\t : {} cell(s)".format(key, value))

if __name__ == "__main__":
    try:
        main()
    except SudokuResolverException as ex:
        logging.error(ex.message)

