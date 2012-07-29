from StringIO import StringIO

SIZE = 9

class Grid():
    """ The sudoku grid of 9x9 cells.
        Each cell features a list of the 1 to 9 remaining candidates (from numbers 1 to 9) allowed for this cell.
        When a cell has only one remaining candidate (list of size 1), it is the definitive number found for this cell.
    """
    def __init__(self, fileToLoad = None):    
        """ Initialization of the grid.
            If a fileToLoad is provided, it is parsed to create the grid.
            If not, initially each of the 9x9 cells will have a full list [1,2,3,4,5,6,7,8,9] of possible candidates.
        """
        if fileToLoad == None:
            fileToLoad = StringIO(__blankGrid__())
        self.load(fileToLoad) 

    def set(self, x, y, val):
        """ Sets a cell to one number, ie a list containing one element : the specified value.
            Will serve for setting the initial numbers given with the grid.
        """
        self.candidates[x][y] = [val]

    def get_solution(self, x, y):
        """ Returns the remaining candidate for the cell (x, y) if there is only one, ie the cell is solved.
            Return None if there are more than one possible candidate left for this cell
        """
        if len(self.candidates[x][y]) == 1:
            return self.candidates[x][y][0]
        return None

    def remove_candidate(self, x, y, val):
        """ Removes a remaining candidate from a cell. """
        if val in self.candidates[x][y]:
            self.candidates[x][y].remove(val)

    def display(self):
        """ Returns a string representation of the grid in the current state.
            Cells whose value has been found are displayed by the corresponding number (from 1 to 9).
            Cells with two or more remaining possible values are displayed with a dot (".").
            Each row ends with a line return ("\n").
        """
        grid = ""
        for y in range(SIZE):
            for x in range(SIZE):
                cell_candidates = self.candidates[x][y]
                if len(cell_candidates) > 1:
                    grid = grid + "."
                else:
                    grid = grid + str(cell_candidates[0])
            grid = grid + "\n"
        return grid

    def load(self, fileToLoad):
        """ Loads a string representation of a grid into the cells of this grid.
            See the display() docstring above for the expected formatting.
            Empty lines and lines starting with a # are ignored.        
        """
        self.candidates = [[[] for x in range(SIZE)] for y in range(SIZE)]
        lineIndex = 0
        for line in fileToLoad:
            lineToParse = line.rstrip("\r\n")

            if lineToParse[0:1] == '#' or len(lineToParse) == 0:
                continue
            elif lineIndex >= SIZE:
                raise GridLoadingException("Loading Error : too many lines")
            elif len(lineToParse) > SIZE:
                raise GridLoadingException("Loading Error : line {} has more than {} characters : {}".format(lineIndex+1, SIZE, lineToParse))

            columnIndex = 0
            for char in lineToParse:
                if char == '.':
                    self.candidates[columnIndex][lineIndex] = range(1, 10)
                elif char.isdigit():
                    self.set(columnIndex, lineIndex, int(char))
                else:
                    raise GridLoadingException("Loading Error : invalid character on line {}, column {} : {}".format(lineIndex+1, columnIndex+1, lineToParse))
                columnIndex += 1

            lineIndex += 1

    def __iter__(self):
        """ Returns an iterator over the unsolved cells of the grid. """
        class GridIterator:
            def __init__(self, grid):
                self.grid = grid
                self.currentCell = [-1, 0]
                self.howManySolvedCellsInThisPass = 0
                self.howManySolvedCellsInLastPass = 0
            def __iter__(self):
                return self
            def next(self):
                """ Finds the next unsolved cell.
                    Raises StopIteration if the grid is fully solved or in an unsolvable state.
                    Note : this algorithm requires two full passes with no changes in order to detect an unsolvable grid,
                    because it compares the number of solved cells between two consecutive passes.
                    A solved grid will be detected earlier, ie the first time the bottom right cell is reached after the grid is completed.
                """
                while True:
                    # Detect fully solved or unsolvable grids
                    if self.currentCell == [0, 0]:
                        self.howManySolvedCellsInThisPass = 0
                    if self.grid.get_solution(self.currentCell[0], self.currentCell[1]) <> None:
                        self.howManySolvedCellsInThisPass += 1
                    if self.currentCell == [SIZE - 1, SIZE - 1]:
                        if self.howManySolvedCellsInLastPass == SIZE*SIZE or self.howManySolvedCellsInThisPass == self.howManySolvedCellsInLastPass:
                            raise StopIteration
                        else:
                            self.howManySolvedCellsInLastPass = self.howManySolvedCellsInThisPass

                    # Find next cell and check if it is unsolved
                    if self.currentCell[0] == SIZE - 1: # end of line : go to first cell of next line
                        if self.currentCell[1] == SIZE - 1: # end of grid : go back to the top left cell
                            self.currentCell[0] = 0
                            self.currentCell[1] = 0
                        else:
                            self.currentCell[0] = 0
                            self.currentCell[1] += 1
                    else:
                        self.currentCell[0] += 1
                    if self.grid.get_solution(self.currentCell[0], self.currentCell[1]) == None:
                        return self.currentCell
        return GridIterator(self)

class GridLoadingException(Exception):
    pass

def __blankGrid__():
    return """\
.........
.........
.........
.........
.........
.........
.........
.........
........."""
