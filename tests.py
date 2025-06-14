import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_cols,
        )
    
    def test_maze_create__and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._Maze__cells[0][0].has_left_wall,
            False
        )
        self.assertEqual(
            m1._Maze__cells[num_rows - 1][num_cols - 1].has_right_wall,
            False,
        )
    
    def test_maze_create__and_exit(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for row in m1._Maze__cells:
            for cell in row:
                self.assertEqual(
                    cell.visited,
                    False
                )

if __name__ == "__main__":
    unittest.main()

