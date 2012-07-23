import unittest
from StringIO import StringIO
from Grid import Grid

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()

    def test_display(self):
        for x in range(9):
            for y in range(9):
                if x==y:
                    self.grid.set(x, y, x+1)
        self.assertEqual("1........\n.2.......\n..3......\n...4.....\n....5....\n.....6...\n......7..\n.......8.\n........9\n", self.grid.display())

    def test_remove_candidate(self):
        self.assertEqual([1,2,3,4,5,6,7,8,9], self.grid.candidates[0][0])
        self.grid.remove_candidate(0, 0, 1)
        self.assertEqual([2,3,4,5,6,7,8,9], self.grid.candidates[0][0])

    def test_remove_candidate_no_exception_if_the_number_is_already_removed(self):
        self.grid.remove_candidate(0, 0, 1)
        try:
            self.grid.remove_candidate(0, 0, 1)
        except ValueError:
            self.fail("Removing a number already removed should not raise a ValueError")

    def test_load(self):
        stringToLoad = "..1..2..3\n.........\n456......\n.......7.\n.........\n....8....\n.........\n123456789\n..8..2..5\n"
        self.grid.load(StringIO(stringToLoad))
        self.assertEqual(stringToLoad, self.grid.display())

if __name__ == '__main__':
    unittest.main()
