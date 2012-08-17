import unittest
from StringIO import StringIO
from Grid import Grid, startCoordinatesOfBlock
from SudokuResolverExceptions import GridLoadingException

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

    def test_load_without_line_returns(self):
        self.grid.load(StringIO("..1..2..3.........456.............7..............8.............123456789..8..2..5"))
        self.assertEqual("..1..2..3\n.........\n456......\n.......7.\n.........\n....8....\n.........\n123456789\n..8..2..5\n", self.grid.display())

    def test_load_grid_with_zeroes_and_random_line_returns(self):
        self.grid.load(StringIO("00100200300000000045\n600000000000007000000000000008\n0000000000000123456789008002005"))
        self.assertEqual("..1..2..3\n.........\n456......\n.......7.\n.........\n....8....\n.........\n123456789\n..8..2..5\n", self.grid.display())

    def test_load_with_a_grid_longer_than_9x9_characters(self):
        with self.assertRaises(GridLoadingException) as ex:
            Grid(StringIO("1234567891........................................................................"))
        self.assertEqual("Loading Error : too many characters", ex.exception.message)

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
        self.assertEqual("Loading Error : too many characters", ex.exception.message)

    def test_load_incomplete_grid(self):
        with self.assertRaises(GridLoadingException) as ex:
            Grid(StringIO("123456789\n.........\n....\n.........\n.........\n\n.........\n"))
        self.assertEqual("Loading Error : incomplete grid, missing cells", ex.exception.message)

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

    def test_iter_next_exit_if_complete_grid(self):
        self.grid.load(StringIO("415638972\n362479185\n789215364\n926341758\n138756429\n574982631\n257164893\n843597216\n691823547\n"))
        iterator = iter(self.grid)
        with self.assertRaises(StopIteration) as ex:
            iterator.next()
        self.assertTrue(ex.exception.args[0])

    def test_iter_next_exit_if_complete_cycle_without_change(self):
        self.grid.load(StringIO("41.638972\n362479185\n789215364\n926341758\n138756429\n574982631\n257164893\n843597216\n691823547\n"))
        iterator = iter(self.grid)
        self.assertEqual([2, 0], iterator.next())
        self.assertEqual([2, 0], iterator.next())
        with self.assertRaises(StopIteration) as ex:
            iterator.next()
        self.assertFalse(ex.exception.args[0])

    def test_start_coordinates_of_block(self):
        self.assertEqual((3, 0), startCoordinatesOfBlock(4, 1))
        self.assertEqual((0, 0), startCoordinatesOfBlock(0, 0))
        self.assertEqual((6, 6), startCoordinatesOfBlock(7, 6))
        self.assertEqual((0, 6), startCoordinatesOfBlock(2, 8))

if __name__ == '__main__':
    unittest.main()
