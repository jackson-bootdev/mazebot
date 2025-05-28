from graphics import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    m = Maze(50, 50, 15, 15, 25, 25, win)

    print("maze created")
    is_solvable = m.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")

    win.wait_for_close()

main()