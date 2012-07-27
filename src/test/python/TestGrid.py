import unittest
from StringIO import StringIO
from Grid import Grid, GridLoadingException

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

    def test_load_with_a_line_longer_than_9_characters(self):
        with self.assertRaises(GridLoadingException) as ex:
            Grid(StringIO("1234567891\n.........\n.........\n.........\n.........\n.........\n.........\n.........\n.........\n"))
        self.assertEqual("Loading Error : line 1 has more than 9 characters : 1234567891", ex.exception.message)

    def test_load_with_invalid_characters(self):
        with self.assertRaises(GridLoadingException) as ex:
            Grid(StringIO("123456789\n.........\n.........\n...x.....\n.........\n.........\n.........\n.........\n.........\n"))
        self.assertEqual("Loading Error : invalid character on line 4, column 4 : ...x.....", ex.exception.message)

    def test_load_with_leading_comments_and_empty_lines(self):
        stringToLoad = "..1..2..3\n.........\n456......\n.......7.\n.........\n....8....\n.........\n123456789\n..8..2..5\n"
        self.grid.load(StringIO("# comment\n\n\n" + stringToLoad)) 
        self.assertEqual(stringToLoad, self.grid.display())

    def test_load_with_more_than_9_lines(self):
        with self.assertRaises(GridLoadingException) as ex:
            Grid(StringIO("123456789\n.........\n.........\n.........\n.........\n.........\n.........\n.........\n.........\n\n.........\n"))
        self.assertEqual("Loading Error : too many lines", ex.exception.message)

    def test_get_solution(self):
        self.grid.load(StringIO("1........\n.2.......\n..3......\n...4.....\n....5....\n.....6...\n......7..\n.......8.\n........9\n")) 
        self.assertEqual(2, self.grid.get_solution(1,1))
        self.assertEqual(None, self.grid.get_solution(2,1))

    def test_iter_next_starting_cell_with_blank_grid(self):
        iterator = iter(self.grid)
        self.assertEqual([0, 0], iterator.next())

    def test_iter_next(self):
        self.grid.load(StringIO("41.6.8972\n3.2479185\n789215364\n926341758\n138756429\n574982631\n257164893\n843597216\n691823547\n")) 
        iterator = iter(self.grid)
        self.assertEqual([2, 0], iterator.next(), "first")
        self.assertEqual([4, 0], iterator.next(), "second")
        self.assertEqual([1, 1], iterator.next(), "third")
        self.assertEqual([2, 0], iterator.next(), "back to first")

if __name__ == '__main__':
    unittest.main()
