from tkinter import Tk, BOTH, Canvas, StringVar, OptionMenu, Entry, Label


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(
        self,
        p1,
        p2,
    ):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Button:
    def __init__(self, window, text, x, y, width, height, command):
        self.__window = window
        self.__canvas = window._Window__canvas
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__command = command

        self.__button = self.__canvas.create_rectangle(
            x, y, x + width, y + height, fill="lightgray", outline="black"
        )
        self.__text = self.__canvas.create_text(
            x + width // 2, y + height // 2, text=text, fill="black"
        )

        self.__canvas.tag_bind(self.__button, "<Button-1>", self.__on_click)
        self.__canvas.tag_bind(self.__text, "<Button-1>", self.__on_click)

    def __on_click(self, event):
        if self.__command:
            self.__command()

    def show(self):
        self.__canvas.itemconfigure(self.__button, state="normal")
        self.__canvas.itemconfigure(self.__text, state="normal")

    def hide(self):
        self.__canvas.itemconfigure(self.__button, state="hidden")
        self.__canvas.itemconfigure(self.__text, state="hidden")


class Dropdown:
    def __init__(self, root, options, default, on_select):
        self._var = StringVar(root)
        self._var.set(default)
        self._var.trace("w", lambda *args: on_select(self._var.get()))

        self._menu = OptionMenu(root, self._var, *options)

    def place(self, x, y):
        self._menu.place(x=x, y=y)

    def hide(self):
        self._menu.place_forget()


class InputField:
    def __init__(self, root, label_text, default_value, on_change):
        self._label = Label(root, text=label_text)
        self._entry = Entry(root)
        self._entry.insert(0, str(default_value))
        self._entry.bind("<Return>", lambda event: on_change(self._entry.get()))

    def place(self, label_x, label_y, entry_x, entry_y):
        self._label.place(x=label_x, y=label_y)
        self._entry.place(x=entry_x, y=entry_y)

    def hide(self):
        self._label.place_forget()
        self._entry.place_forget()

    def update_value(self, new_value):
        self._entry.delete(0, "end")
        self._entry.insert(0, str(new_value))
