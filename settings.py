from graphics import Button, Dropdown
from tkinter import StringVar, OptionMenu

def create_settings_menu(window, screen_x, screen_y, algorithm, show_main_menu):
    def on_back_click():
        dropdown.hide()
        back_button.hide()
        show_main_menu()

    def on_algorithm_select(selected_alg):
        algorithm[0] = selected_alg
        print(f"Algorithm set to: {selected_alg}")

    # Create a dropdown menu for algorithm selection
    dropdown = Dropdown(
        window._Window__root, ["dfs", "bfs", "a_star"], algorithm[0], on_algorithm_select
    )

    back_button = Button(window, "Back", screen_x // 2 - 50, screen_y // 2 + 50, 100, 50, on_back_click)
    back_button.hide()

    def show_settings_menu():
        dropdown.place(screen_x // 2 - 50, screen_y // 2 - 75)
        back_button.show()

    return show_settings_menu
