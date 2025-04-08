import sys
from graphics import Window
from maze import Maze


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

    maze = Maze(margin, margin, num_rows, num_columns, cell_size_x, cell_size_y, window, 10)
    print("Maze created!")
    
    is_solvable = maze.solve()
    print("Solving the maze...")
    
    if not is_solvable:
        print("This maze can not be solved!")
    else:
        print("The maze has been solved!")
        
    window.wait_for_close()


main()
