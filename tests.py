import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_columns = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_columns, 10, 10)
        self.assertEqual(
            len(maze._cells),
            num_columns,
        )
        self.assertEqual(
            len(maze._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_columns = 16
        num_rows = 12
        maze = Maze(0, 0, num_rows, num_columns, 10, 10)
        self.assertEqual(
            len(maze._cells),
            num_columns,
        )
        self.assertEqual(
            len(maze._cells[0]),
            num_rows,
        )


if __name__ == "__main__":
    unittest.main()
