from cell import Cell
import time
import random

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
        seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []

        self.seed = 0
        if seed != None:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
    
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
        time.sleep(0.01)
    
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_left_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.num_rows - 1][self.num_cols - 1].has_right_wall = False
        self.__draw_cell(self.num_rows - 1, self.num_cols - 1)

    def __break_walls_r(self, row, column):
        self.__cells[row][column].visited = True
        
        while True:
            possible_directions = []

            if row > 0 and not self.__cells[row -1][column].visited: #top
                possible_directions.append([row -1, column])               
            if column < self.num_cols - 1 and not self.__cells[row][column +1].visited: #right 
                possible_directions.append([row, column +1])
            if row < self.num_rows - 1 and not self.__cells[row +1][column].visited: #bottom
                possible_directions.append([row +1, column])
            if column > 0 and not self.__cells[row][column -1].visited: #left
                possible_directions.append([row, column -1])

            if len(possible_directions) == 0:
                self.__draw_cell(row, column)
                return
            
            direction = possible_directions[random.randrange(0, len(possible_directions))]
            if direction[0] == row - 1: #top
                self.__cells[row][column].has_top_wall = False
                self.__cells[direction[0]][direction[1]].has_bottom_wall = False
            elif direction[1] == column + 1: #right
                self.__cells[row][column].has_right_wall = False
                self.__cells[direction[0]][direction[1]].has_left_wall = False
            elif direction[0] == row + 1: #bottom
                self.__cells[row][column].has_bottom_wall = False
                self.__cells[direction[0]][direction[1]].has_top_wall = False
            elif direction[1] == column - 1: #left
                self.__cells[row][column].has_left_wall = False
                self.__cells[direction[0]][direction[1]].has_right_wall = False
            else:
                raise Exception("No wall was provided for possible direction")
            
            self.__draw_cell(row, column)
            self.__draw_cell(direction[0], direction[1])
            
            self.__break_walls_r(direction[0], direction[1])
