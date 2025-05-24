from cell import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []

        self.__create_cells()
        self.__break_entrance_and_exit()
    
    def __create_cells(self):
        for i in range(self.num_rows):
            self.__cells.append([])
            for j in range(self.num_cols):
                self.__cells[i].append(Cell(self.__win))
                self.__draw_cell(i, j)
    
    def __draw_cell(self, row, column):
        if self.__win is None:
            return
        cell_pos_x = self.x1 + ((column) * self.cell_size_x)
        cell_pos_y = self.y1 + ((row) * self.cell_size_y)
        self.__cells[row][column].draw(cell_pos_x, cell_pos_y, cell_pos_x + self.cell_size_x, cell_pos_y + self.cell_size_y)
        self._animate()
    
    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)
    
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
        self.__draw_cell(self.num_rows - 1, self.num_cols - 1)

 