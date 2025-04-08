from graphics import Window
from cell import Cell


def main():
    window = Window(800, 600)

    cell = Cell(window)
    cell.has_left_wall = False
    cell.draw(50, 50, 100, 100)

    cell = Cell(window)
    cell.has_right_wall = False
    cell.draw(125, 125, 200, 200)

    cell = Cell(window)
    cell.has_bottom_wall = False
    cell.draw(225, 225, 250, 250)

    cell = Cell(window)
    cell.has_top_wall = False
    cell.draw(300, 300, 500, 500)

    window.wait_for_close()


main()
