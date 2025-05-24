from graphics import Line, Point

class Cell:
    def __init__(self, window = None):
        self.__win = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
    
    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "red")
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "white")
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "red")
        else:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "red")
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "red")
        else:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")
    
    def draw_move(self, to_cell, undo = False):
        colour = "gray" if undo else "red"
        start_x = (self.__x1 + self.__x2) / 2
        start_y = (self.__y1 + self.__y2) / 2
        end_x = (to_cell.__x1 + to_cell.__x2) / 2
        end_y = (to_cell.__y1 + to_cell.__y2) / 2
        self.__win.draw_line(Line(Point(start_x, start_y), Point(end_x, end_y)), colour)