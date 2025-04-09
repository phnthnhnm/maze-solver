import sys
from graphics import Window, Button
from maze import Maze

def start_process(window, margin, num_rows, num_columns, cell_size_x, cell_size_y, algorithm):
    maze = Maze(margin, margin, num_rows, num_columns, cell_size_x, cell_size_y, window, 200)
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

    def show_main_menu():
        start_button.show()
        settings_button.show()

    def hide_main_menu():
        start_button.hide()
        settings_button.hide()

    def on_start_click():
        hide_main_menu()
        start_process(window, margin, num_rows, num_columns, cell_size_x, cell_size_y, algorithm[0])

    def on_settings_click():
        hide_main_menu()
        dfs_button.show()
        bfs_button.show()
        a_star_button.show()
        back_button.show()

    def on_back_click():
        dfs_button.hide()
        bfs_button.hide()
        a_star_button.hide()
        back_button.hide()
        show_main_menu()

    def set_algorithm(alg):
        algorithm[0] = alg
        print(f"Algorithm set to: {alg}")

    start_button = Button(window, "Start", screen_x // 2 - 50, screen_y // 2 - 75, 100, 50, on_start_click)
    settings_button = Button(window, "Settings", screen_x // 2 - 50, screen_y // 2, 100, 50, on_settings_click)

    dfs_button = Button(window, "DFS", screen_x // 2 - 50, screen_y // 2 - 75, 100, 50, lambda: set_algorithm("dfs"))
    bfs_button = Button(window, "BFS", screen_x // 2 - 50, screen_y // 2, 100, 50, lambda: set_algorithm("bfs"))
    a_star_button = Button(window, "A*", screen_x // 2 - 50, screen_y // 2 + 75, 100, 50, lambda: set_algorithm("a_star"))
    back_button = Button(window, "Back", screen_x // 2 - 50, screen_y // 2 + 150, 100, 50, on_back_click)

    dfs_button.hide()
    bfs_button.hide()
    a_star_button.hide()
    back_button.hide()

    show_main_menu()

    window.wait_for_close()

main()
