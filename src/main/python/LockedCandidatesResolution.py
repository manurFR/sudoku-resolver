#!/usr/bin/env python
# -*- coding: UTF8 -*-

import logging
import Stats
from Grid import SIZE

class LockedCandidatesResolution:
    """ Locked candidates (also known as Pointed Pairs or Pointed Triples) come in two types, almost similar but actually different :
        - Type 1 "Line->Block reduction" : two or three aligned cells inside a block share a same remaining candidate, and that digit is not a remaining
          candidate in any other cell OF THE BLOCK. Since a block must feature each digit, that candidate must appear on this alignment of two or three
          cells. Consequently, it can not appear on any other cell of the same LINE (row or column). The corresponding candidates can be removed.
        - Type 2 "Block->Line reduction" : two or three aligned cells inside a block share a same remaining candidate, and that digit is not a remaining
          candidate in any other cell OF THE SAME LINE (row or column). Since a line must feature each digit, that candidate must appear in one of these
          two or three cells. Consequently, it can not appear on any other cell of the same BLOCK. The corresponding candidates can be removed.
        These resolutions will only infrequently lead to solving cells, but it may remove remaining candidates that otherwise prevent other resolution methods to succeed.
    """
    def run(self, grid):
        solvedCells = 0
        for xBlock in [0, 3, 6]:
            for yBlock in [0, 3, 6]:
                solvedCells += self.row_block_reduction(grid, xBlock, yBlock) + self.column_block_reduction(grid, xBlock, yBlock) + \
                                self.block_row_reduction(grid, xBlock, yBlock) + self.block_column_reduction(grid, xBlock, yBlock)
        Stats.increment(self.__class__.__name__, solvedCells)
        return solvedCells

    def row_block_reduction(self, grid, xBlock, yBlock):
        """ For each of the 9 digits not already solved in the (xBlock, yBlock) block, check if this digit is included in the remaining candidates
             of two or three cells in a row, AND not included in the remaining candidates of the other two rows.
            If it is the case, remove this digit from the remaining candidates of all the cells in the same row outside of the block.
            Returns the number of cells solved by this process.
        """
        digits = self.remaining_candidates_in_block(grid, xBlock, yBlock)
        if not digits:
            return 0

        solvedCells = 0
        for d in digits:
            occurrences = dict.fromkeys(range(yBlock, yBlock+3), 0)
            rowsWhereThisDigitIsPresent = set()
            rowsWhereThisDigitIsPresentTwiceOrThrice = set()
            for row in range(yBlock, yBlock+3):
                for col in range(xBlock, xBlock+3):
                    if d in grid.candidates[col][row]:
                        if row in rowsWhereThisDigitIsPresent:
                            rowsWhereThisDigitIsPresentTwiceOrThrice.add(row)
                        else:
                            rowsWhereThisDigitIsPresent.add(row)
            if len(rowsWhereThisDigitIsPresentTwiceOrThrice) == 1 and len(rowsWhereThisDigitIsPresent) == 1: # if there is one and only one row with 2 or 3 cells featuring the current digit as remaining candidate...
                rowToProcess = rowsWhereThisDigitIsPresentTwiceOrThrice.pop()
                for i in range(SIZE):
                    if (i < xBlock or i > xBlock + 2) and d in grid.candidates[i][rowToProcess]:
                        logging.debug("Locked Candidates resolution (row->block) : removing candidate {} in ({},{}) thanks to locked candidates in block ({},{})".format(d, i, rowToProcess, xBlock, yBlock))
                        grid.remove_candidate(i, rowToProcess, d)
                        if grid.get_solution(i, rowToProcess) != None:
                            logging.info("Locked Candidates resolution : found value for ({},{}) : {}".format(i, rowToProcess, grid.get_solution(i, rowToProcess)))
                            solvedCells += 1
        return solvedCells

    def column_block_reduction(self, grid, xBlock, yBlock):
        """ For each of the 9 digits not already solved in the (xBlock, yBlock) block, check if this digit is included in the remaining candidates
             of two or three cells in a column, AND not included in the remaining candidates of the other two columns.
            If it is the case, remove this digit from the remaining candidates of all the cells in the same column outside of the block.
            Returns the number of cells solved by this process.
        """
        digits = self.remaining_candidates_in_block(grid, xBlock, yBlock)
        if not digits:
            return 0

        solvedCells = 0
        for d in digits:
            occurrences = dict.fromkeys(range(yBlock, yBlock+3), 0)
            colsWhereThisDigitIsPresent = set()
            colsWhereThisDigitIsPresentTwiceOrThrice = set()
            for col in range(xBlock, xBlock+3):
                for row in range(yBlock, yBlock+3):
                    if d in grid.candidates[col][row]:
                        if col in colsWhereThisDigitIsPresent:
                            colsWhereThisDigitIsPresentTwiceOrThrice.add(col)
                        else:
                            colsWhereThisDigitIsPresent.add(col)
            if len(colsWhereThisDigitIsPresentTwiceOrThrice) == 1 and len(colsWhereThisDigitIsPresent) == 1: # if there is one and only one column with 2 or 3 cells featuring the current digit as remaining candidate...
                colToProcess = colsWhereThisDigitIsPresentTwiceOrThrice.pop()
                for i in range(SIZE):
                    if (i < yBlock or i > yBlock + 2) and d in grid.candidates[colToProcess][i]:
                        logging.debug("Locked Candidates resolution (column->block) : removing candidate {} in ({},{}) thanks to locked candidates in block ({},{})".format(d, colToProcess, i,  xBlock, yBlock))
                        grid.remove_candidate(colToProcess, i, d)
                        if grid.get_solution(colToProcess, i) != None:
                            logging.info("Locked Candidates resolution : found value for ({},{}) : {}".format(colToProcess, i, grid.get_solution(colToProcess, i)))
                            solvedCells += 1
        return solvedCells

    def block_row_reduction(self, grid, xBlock, yBlock):
        """ For each of the 9 digits not already solved in the (xBlock, yBlock) block, check if this digit is included in the remaining candidates
             of two or three cells in a row inside the block, AND not included in the remaining candidates of the rest of the row (outside of the block).
            If it is the case, remove this digit from the remaining candidates of all the cells of the block which are not on the row.
            Returns the number of cells solved by this process.
        """
        digits = self.remaining_candidates_in_block(grid, xBlock, yBlock)
        if not digits:
            return 0

        solvedCells = 0
        for d in digits:
            for row in range(yBlock, yBlock+3):
                occurrencesInTheBlock = 0
                occurrencesOutsideTheBlock = 0
                for col in range(SIZE):
                    if d in grid.candidates[col][row]:
                        if col >= xBlock and col <= xBlock+2:
                            occurrencesInTheBlock += 1
                        else:
                            occurrencesOutsideTheBlock += 1

                if occurrencesInTheBlock >= 2 and occurrencesOutsideTheBlock == 0: # if there are 2 or 3 cells in the block featuring the current digit as remaining candidate and no other cell in the same row...
                    for y in range(yBlock, yBlock+3):
                        if y == row:
                            continue # don't remove the digit from the remaining candidates in the current row
                        for x in range(xBlock, xBlock+3):
                            if d in grid.candidates[x][y]:
                                logging.debug("Locked Candidates resolution (block->row) : removing candidate {} in ({},{}) thanks to locked candidates in block ({},{})".format(d, x, y, xBlock, yBlock))
                                grid.remove_candidate(x, y, d)
                                if grid.get_solution(x, y) != None:
                                    logging.info("Locked Candidates resolution : found value for ({},{}) : {}".format(x, y, grid.get_solution(x, y)))
                                    solvedCells += 1
        return solvedCells

    def block_column_reduction(self, grid, xBlock, yBlock):
        """ For each of the 9 digits not already solved in the (xBlock, yBlock) block, check if this digit is included in the remaining candidates
             of two or three cells in a column inside the block, AND not included in the remaining candidates of the rest of the column (outside of the block).
            If it is the case, remove this digit from the remaining candidates of all the cells of the block which are not on the column.
            Returns the number of cells solved by this process.
        """
        digits = self.remaining_candidates_in_block(grid, xBlock, yBlock)
        if not digits:
            return 0

        solvedCells = 0
        for d in digits:
            for col in range(xBlock, xBlock+3):
                occurrencesInTheBlock = 0
                occurrencesOutsideTheBlock = 0
                for row in range(SIZE):
                    if d in grid.candidates[col][row]:
                        if row >= yBlock and row <= yBlock+2:
                            occurrencesInTheBlock += 1
                        else:
                            occurrencesOutsideTheBlock += 1

                if occurrencesInTheBlock >= 2 and occurrencesOutsideTheBlock == 0: # if there are 2 or 3 cells in the block featuring the current digit as remaining candidate and no other cell in the same column...
                    for x in range(xBlock, xBlock+3):
                        if x == col:
                            continue # don't remove the digit from the remaining candidates in the current column
                        for y in range(yBlock, yBlock+3):
                            if d in grid.candidates[x][y]:
                                logging.debug("Locked Candidates resolution (block->column) : removing candidate {} in ({},{}) thanks to locked candidates in block ({},{})".format(d, x, y, xBlock, yBlock))
                                grid.remove_candidate(x, y, d)
                                if grid.get_solution(x, y) != None:
                                    logging.info("Locked Candidates resolution : found value for ({},{}) : {}".format(x, y, grid.get_solution(x, y)))
                                    solvedCells += 1
        return solvedCells

    def remaining_candidates_in_block(self, grid, xBlock, yBlock):
        """ Returns the sorted list of all the digits still not solved in a block """
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in range(xBlock, xBlock+3):
            for y in range(yBlock, yBlock+3):
                if grid.get_solution(x, y) in digits:
                    digits.remove(grid.get_solution(x, y))
        return digits
