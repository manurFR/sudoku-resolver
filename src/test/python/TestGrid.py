import unittest
from Grid import Grid

class GridTest(unittest.TestCase):
    def test_display(self):
        grid = Grid()
        for x in range(9):
            for y in range(9):
                if x==y:
                    grid.set(x, y, x)
        self.assertEqual("1........\n.2.......\n..3......\n...4.....\n....5....\n.....6...\n......7..\n.......8.\n........9\n", grid.display())

if __name__ == '__main__':
    unittest.main()
