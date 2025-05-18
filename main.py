from tkinter import Tk, BOTH, Canvas

def main():
    win = Window(800, 600)
    win.wait_for_close()

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Bot")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

main()