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
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []

        self.__create_cells()
    
    def __create_cells(self):
        for i in range(self.num_rows):
            self.__cells.append([])
            for j in range(self.num_cols):
                self.__cells[i].append(Cell(self.win))
                self.__draw_cell(i, j)
    
    def __draw_cell(self, row, column):
        cell_pos_x = self.x1 + ((row) * self.cell_size_x)
        cell_pos_y = self.y1 + ((column) * self.cell_size_y)
        self.__cells[row][column].draw(cell_pos_x, cell_pos_y, cell_pos_x + self.cell_size_x, cell_pos_y + self.cell_size_y)
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
 