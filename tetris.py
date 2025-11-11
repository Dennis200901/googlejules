import tkinter as tk
import random

class TetrisGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Tetris")
        self.master.geometry("300x600")

        self.canvas = tk.Canvas(self.master, width=300, height=600, bg='black')
        self.canvas.pack()

        self.grid_width = 10
        self.grid_height = 20
        self.cell_size = 30
        self.grid = [[0] * self.grid_width for _ in range(self.grid_height)]

        self.shapes = [
            [[1, 1, 1, 1]],  # I
            [[1, 1], [1, 1]],  # O
            [[0, 1, 0], [1, 1, 1]],  # T
            [[0, 1, 1], [1, 1, 0]],  # S
            [[1, 1, 0], [0, 1, 1]],  # Z
            [[1, 0, 0], [1, 1, 1]],  # J
            [[0, 0, 1], [1, 1, 1]]  # L
        ]
        self.colors = ['cyan', 'yellow', 'purple', 'green', 'red', 'blue', 'orange']

        self.current_shape = None
        self.current_color = None
        self.current_x = 0
        self.current_y = 0

        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Down>", self.move_down)
        self.master.bind("<Up>", self.rotate)

        self.new_shape()
        self.update()

    def new_shape(self):
        shape_index = random.randint(0, len(self.shapes) - 1)
        self.current_shape = self.shapes[shape_index]
        self.current_color = self.colors[shape_index]
        self.current_x = self.grid_width // 2 - len(self.current_shape[0]) // 2
        self.current_y = 0
        if self.check_collision(self.current_shape, self.current_x, self.current_y):
            self.game_over()

    def check_collision(self, shape, x, y):
        for row_index, row in enumerate(shape):
            for col_index, cell in enumerate(row):
                if cell:
                    if (y + row_index >= self.grid_height or
                            x + col_index < 0 or
                            x + col_index >= self.grid_width or
                            self.grid[y + row_index][x + col_index]):
                        return True
        return False

    def merge_shape(self):
        for row_index, row in enumerate(self.current_shape):
            for col_index, cell in enumerate(row):
                if cell:
                    self.grid[self.current_y + row_index][self.current_x + col_index] = self.current_color

    def clear_lines(self):
        lines_to_clear = []
        for row_index, row in enumerate(self.grid):
            if all(cell != 0 for cell in row):
                lines_to_clear.append(row_index)

        for row_index in lines_to_clear:
            del self.grid[row_index]
            self.grid.insert(0, [0] * self.grid_width)

    def draw_grid(self):
        self.canvas.delete("all")
        for row_index, row in enumerate(self.grid):
            for col_index, cell in enumerate(row):
                if cell:
                    self.canvas.create_rectangle(
                        col_index * self.cell_size, row_index * self.cell_size,
                        (col_index + 1) * self.cell_size, (row_index + 1) * self.cell_size,
                        fill=cell, outline='gray'
                    )

    def draw_shape(self):
        for row_index, row in enumerate(self.current_shape):
            for col_index, cell in enumerate(row):
                if cell:
                    self.canvas.create_rectangle(
                        (self.current_x + col_index) * self.cell_size, (self.current_y + row_index) * self.cell_size,
                        (self.current_x + col_index + 1) * self.cell_size, (self.current_y + row_index + 1) * self.cell_size,
                        fill=self.current_color, outline='gray'
                    )

    def move_left(self, event):
        if not self.check_collision(self.current_shape, self.current_x - 1, self.current_y):
            self.current_x -= 1

    def move_right(self, event):
        if not self.check_collision(self.current_shape, self.current_x + 1, self.current_y):
            self.current_x += 1

    def move_down(self, event=None):
        if not self.check_collision(self.current_shape, self.current_x, self.current_y + 1):
            self.current_y += 1
        else:
            self.merge_shape()
            self.clear_lines()
            self.new_shape()

    def rotate(self, event):
        rotated_shape = list(zip(*self.current_shape[::-1]))
        if not self.check_collision(rotated_shape, self.current_x, self.current_y):
            self.current_shape = rotated_shape

    def update(self):
        self.move_down()
        self.draw_grid()
        self.draw_shape()
        self.master.after(500, self.update)

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(150, 300, text="Game Over", fill="white", font=("Helvetica", 24))
        self.master.unbind("<Left>")
        self.master.unbind("<Right>")
        self.master.unbind("<Down>")
        self.master.unbind("<Up>")
