from graphics import Button, Dropdown, InputField, Label
import random

def create_settings_menu(window, screen_x, screen_y, algorithm, seed, speed, show_main_menu):
    if not isinstance(speed, list):
        raise TypeError("Expected 'speed' to be a list, but got {}".format(type(speed).__name__))

    def on_back_click():
        algorithm_label.place_forget()
        dropdown.hide()
        seed_input.hide()
        speed_input.hide()
        randomize_button.hide()
        back_button.hide()
        show_main_menu()

    # Mapping display names to internal values
    algorithm_mapping = {
        "DFS": "dfs",
        "BFS": "bfs",
        "A*": "a_star"
    }

    def on_algorithm_select(selected_alg):
        algorithm[0] = algorithm_mapping[selected_alg]
        print(f"Algorithm set to: {algorithm[0]}")

    def on_seed_change(new_seed):
        try:
            seed[0] = int(new_seed)
            print(f"Seed set to: {seed[0]}")
        except ValueError:
            print("Invalid seed value")

    def on_randomize_seed():
        seed[0] = random.randint(0, 10000)
        seed_input.update_value(seed[0])
        print(f"Seed randomized to: {seed[0]}")

    def on_speed_change(new_speed):
        try:
            speed[0] = float(new_speed)
            print(f"Speed set to: {speed[0]}")
        except ValueError:
            print("Invalid speed value")

    algorithm_label = Label(window._Window__root, text="Algorithm:")
    dropdown = Dropdown(
        window._Window__root, list(algorithm_mapping.keys()),
        list(algorithm_mapping.keys())[0],
        on_algorithm_select
    )

    seed_input = InputField(window._Window__root, "Seed:", seed[0], on_seed_change)
    speed_input = InputField(window._Window__root, "Speed:", speed[0], on_speed_change)
    randomize_button = Button(window, "Randomize", screen_x // 2 + 120, screen_y // 2, 100, 30, on_randomize_seed)
    randomize_button.hide()

    back_button = Button(window, "Back", screen_x // 2 - 50, screen_y // 2 + 100, 100, 50, on_back_click)
    back_button.hide() 
    speed_input.hide()
    
    def show_settings_menu():
        algorithm_label.place(x=screen_x // 2 - 100, y=screen_y // 2 - 75)
        dropdown.place(screen_x // 2 - 20, screen_y // 2 - 75)
        seed_input.place(screen_x // 2 - 100, screen_y // 2, screen_x // 2 - 50, screen_y // 2)
        speed_input.place(screen_x // 2 - 100, screen_y // 2 + 50, screen_x // 2 - 50, screen_y // 2 + 50)
        randomize_button.show()
        back_button.show()

    return show_settings_menu
