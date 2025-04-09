from graphics import Button

def create_settings_menu(window, screen_x, screen_y, algorithm, show_main_menu):
    def set_algorithm(alg):
        algorithm[0] = alg
        print(f"Algorithm set to: {alg}")

    def on_back_click():
        dfs_button.hide()
        bfs_button.hide()
        a_star_button.hide()
        back_button.hide()
        show_main_menu()

    dfs_button = Button(window, "DFS", screen_x // 2 - 50, screen_y // 2 - 75, 100, 50, lambda: set_algorithm("dfs"))
    bfs_button = Button(window, "BFS", screen_x // 2 - 50, screen_y // 2, 100, 50, lambda: set_algorithm("bfs"))
    a_star_button = Button(window, "A*", screen_x // 2 - 50, screen_y // 2 + 75, 100, 50, lambda: set_algorithm("a_star"))
    back_button = Button(window, "Back", screen_x // 2 - 50, screen_y // 2 + 150, 100, 50, on_back_click)

    dfs_button.hide()
    bfs_button.hide()
    a_star_button.hide()
    back_button.hide()

    def show_settings_menu():
        dfs_button.show()
        bfs_button.show()
        a_star_button.show()
        back_button.show()

    return show_settings_menu
