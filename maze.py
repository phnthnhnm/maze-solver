from cell import Cell
import random
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_columns,
        cell_size_x,
        cell_size_y,
        window=None,
        seed=None,
        speed=[0.01],
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._speed = speed

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_columns):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._window))
            self._cells.append(col_cells)

        for i in range(self._num_columns):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._window is None:
            return

        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._window is None:
            return

        self._window.redraw()
        time.sleep(self._speed[0])

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_columns - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_columns - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            next_index_list = []

            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            if i < self._num_columns - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self, alg="dfs"):
        if alg == "dfs":
            return self._solve_dfs(0, 0)
        elif alg == "bfs":
            return self._solve_bfs(0, 0)
        elif alg == "a_star":
            return self._solve_a_star(0, 0)
        else:
            raise ValueError(f"Unknown algorithm: {alg}")

    def _solve_bfs(self, i, j):
        from collections import deque

        queue = deque([(i, j)])
        self._cells[i][j].visited = True

        while queue:
            x, y = queue.popleft()
            self._animate()

            if x == self._num_columns - 1 and y == self._num_rows - 1:
                return True

            for dx, dy, wall_check in [
                (-1, 0, lambda x, y: not self._cells[x][y].has_left_wall),
                (1, 0, lambda x, y: not self._cells[x][y].has_right_wall),
                (0, -1, lambda x, y: not self._cells[x][y].has_top_wall),
                (0, 1, lambda x, y: not self._cells[x][y].has_bottom_wall),
            ]:
                nx, ny = x + dx, y + dy

                if (
                    0 <= nx < self._num_columns
                    and 0 <= ny < self._num_rows
                    and not self._cells[nx][ny].visited
                    and wall_check(x, y)
                ):
                    self._cells[x][y].draw_move(self._cells[nx][ny])
                    self._cells[nx][ny].visited = True
                    queue.append((nx, ny))

        return False

    def _solve_dfs(self, i, j):
        self._animate()

        self._cells[i][j].visited = True

        if i == self._num_columns - 1 and j == self._num_rows - 1:
            return True

        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_dfs(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if (
            i < self._num_columns - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_dfs(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_dfs(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        if (
            j < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_dfs(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False

    def _solve_a_star(self, i, j):
        from heapq import heappush, heappop

        def heuristic(x, y):
            return abs(x - (self._num_columns - 1)) + abs(y - (self._num_rows - 1))

        open_set = []
        heappush(open_set, (0 + heuristic(i, j), 0, i, j))
        self._cells[i][j].visited = True

        while open_set:
            _, cost, x, y = heappop(open_set)
            self._animate()

            if x == self._num_columns - 1 and y == self._num_rows - 1:
                return True

            for dx, dy, wall_check in [
                (-1, 0, lambda x, y: not self._cells[x][y].has_left_wall),
                (1, 0, lambda x, y: not self._cells[x][y].has_right_wall),
                (0, -1, lambda x, y: not self._cells[x][y].has_top_wall),
                (0, 1, lambda x, y: not self._cells[x][y].has_bottom_wall),
            ]:
                nx, ny = x + dx, y + dy

                if (
                    0 <= nx < self._num_columns
                    and 0 <= ny < self._num_rows
                    and not self._cells[nx][ny].visited
                    and wall_check(x, y)
                ):
                    self._cells[x][y].draw_move(self._cells[nx][ny])
                    self._cells[nx][ny].visited = True
                    heappush(open_set, (cost + 1 + heuristic(nx, ny), cost + 1, nx, ny))

        return False
