import sys
from graphics import Window, Button
from maze import Maze

def start_process(window, margin, num_rows, num_columns, cell_size_x, cell_size_y):
    maze = Maze(margin, margin, num_rows, num_columns, cell_size_x, cell_size_y, window, 200)
    print("Maze created!")

    is_solvable = maze.solve("a_star")
    print("Solving the maze...")

    if not is_solvable:
        print("This maze can not be solved!")
    else:
        print("The maze has been solved!")

def main():
    num_rows = 12
    num_columns = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_columns
    cell_size_y = (screen_y - 2 * margin) / num_rows
    window = Window(screen_x, screen_y)

    sys.setrecursionlimit(10000)

    def on_start_click():
        start_button.hide()
        start_process(window, margin, num_rows, num_columns, cell_size_x, cell_size_y)

    start_button = Button(window, "Start", screen_x // 2 - 50, screen_y // 2 - 25, 100, 50, on_start_click)
    start_button.show()

    window.wait_for_close()

main()
