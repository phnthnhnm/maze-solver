from graphics import Window, Line, Point


def main():
    window = Window(800, 600)
    line = Line(Point(50, 50), Point(400, 400))
    
    window.draw_line(line, "red")
    window.wait_for_close()


main()
