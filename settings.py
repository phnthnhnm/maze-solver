from graphics import Button, Dropdown, InputField

def create_settings_menu(window, screen_x, screen_y, algorithm, seed, show_main_menu):
    def on_back_click():
        dropdown.hide()
        seed_input.hide()
        back_button.hide()
        show_main_menu()

    def on_algorithm_select(selected_alg):
        algorithm[0] = selected_alg
        print(f"Algorithm set to: {selected_alg}")

    def on_seed_change(new_seed):
        try:
            seed[0] = int(new_seed)
            print(f"Seed set to: {seed[0]}")
        except ValueError:
            print("Invalid seed value")

    # Create a dropdown menu for algorithm selection
    dropdown = Dropdown(
        window._Window__root, ["dfs", "bfs", "a_star"], algorithm[0], on_algorithm_select
    )

    # Create seed input field
    seed_input = InputField(window._Window__root, "Seed:", seed[0], on_seed_change)

    back_button = Button(window, "Back", screen_x // 2 - 50, screen_y // 2 + 100, 100, 50, on_back_click)

    def show_settings_menu():
        dropdown.place(screen_x // 2 - 50, screen_y // 2 - 75)
        seed_input.place(screen_x // 2 - 100, screen_y // 2, screen_x // 2 - 50, screen_y // 2)
        back_button.show()

    return show_settings_menu
