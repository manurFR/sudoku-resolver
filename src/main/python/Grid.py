class Grid():
    candidates = [['.' for x in range(9)] for y in range(9)]

    def set(self, x, y, val):
        self.candidates[x][y] = str(val)

    def display(self):
        #print self.candidates 
        grid = ""
        for y in range(9):
            grid = grid + "".join(self.candidates[y]) + "\n"
        return grid
