SIZE = 9

class Grid():
    """ The sudoku grid of 9x9 cells.
        Each cell features a list of the 1 to 9 remaining candidates (from numbers 1 to 9) allowed for this cell.
        When a cell has only one remaining candidate (list of size 1), it is the definitive number found for this cell.
    """
    def __init__(self):    
        """ initialization of the grid, with each of the 9x9 cells containing the list [1,2,3,4,5,6,7,8,9] of all possible values """
        self.candidates = [[range(1, 10) for x in range(SIZE)] for y in range(SIZE)]

    def set(self, x, y, val):
        """ Sets a cell to one number, ie a list containing one element : the specified value.
            Will serve for setting the initial numbers given with the grid.
        """
        self.candidates[x][y] = [val]

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
