import sys
from graphics import Window, Button
from maze import Maze
from settings import create_settings_menu

def start_process(window, margin, num_rows, num_columns, cell_size_x, cell_size_y, algorithm, seed):
    maze = Maze(margin, margin, num_rows, num_columns, cell_size_x, cell_size_y, window, seed)
    print("Maze created!")

    is_solvable = maze.solve(algorithm)
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

    algorithm = ["dfs"]
    seed = [42]  # Default seed value

    def show_main_menu():
        start_button.show()
        settings_button.show()

    def hide_main_menu():
        start_button.hide()
        settings_button.hide()

    show_settings_menu = create_settings_menu(window, screen_x, screen_y, algorithm, seed, show_main_menu)

    def on_start_click():
        hide_main_menu()
        start_process(window, margin, num_rows, num_columns, cell_size_x, cell_size_y, algorithm[0], seed[0])

    def on_settings_click():
        hide_main_menu()
        show_settings_menu()

    start_button = Button(window, "Start", screen_x // 2 - 50, screen_y // 2 - 75, 100, 50, on_start_click)
    settings_button = Button(window, "Settings", screen_x // 2 - 50, screen_y // 2, 100, 50, on_settings_click)

    show_main_menu()

    window.wait_for_close()

main()
