import random
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

list_of_options = ["0", "."]


class GameOfLife:
    def __init__(self):
        self.board = [[random.choice(list_of_options) for _ in range(6)] for _ in range(6)]
        self.how_many_iterations = 0
        self.how_many_alive = []
        self.how_many_alive.append(self.chech_how_many_alive())

        self.root = tk.Tk()
        self.root.title("Game of Life")

        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(side=tk.TOP)

        self.canvas = tk.Canvas(self.canvas_frame, width=300, height=300)
        self.canvas.pack()

        self.show_board_button = tk.Button(self.root, text="Show Board", command=self.show_board)
        self.show_board_button.pack(side=tk.LEFT)

        self.one_iteration_button = tk.Button(self.root, text="Do 1 Iteration", command=self.do_one_iteration)
        self.one_iteration_button.pack(side=tk.LEFT)

        self.show_evolution_button = tk.Button(self.root, text="Show Evolution", command=self.make_a_plot)
        self.show_evolution_button.pack(side=tk.LEFT)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.end)
        self.exit_button.pack(side=tk.LEFT)

    def show(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def show_board(self):
        self.draw_board()

    def end(self):
        self.root.destroy()

    def make_a_plot(self):
        x = np.array([i for i in range(0, self.how_many_iterations + 1)])
        y = np.array(self.how_many_alive)
        plt.scatter(x, y)
        plt.title("Plot")
        plt.xlabel("Iteration number")
        plt.ylabel("Number of alive cells")
        plt.show()

    def how_many_neighbours(self, column_index, row_index):
        neighbours = 0
        if column_index - 1 >= 0:  # left
            if self.board[row_index][column_index - 1] == "0":
                neighbours += 1
            if row_index - 1 >= 0:  # lefttop
                if self.board[row_index - 1][column_index - 1] == "0":
                    neighbours += 1
            if row_index + 1 < 6:  # leftbottom
                if self.board[row_index + 1][column_index - 1] == "0":
                    neighbours += 1
        if column_index + 1 < 6:  # right
            if self.board[row_index][column_index + 1] == "0":
                neighbours += 1
            if row_index - 1 >= 0:  # righttop
                if self.board[row_index - 1][column_index + 1] == "0":
                    neighbours += 1
            if row_index + 1 < 6:  # rightbottom
                if self.board[row_index + 1][column_index + 1] == "0":
                    neighbours += 1
        if row_index - 1 >= 0:  # top
            if self.board[row_index - 1][column_index] == "0":
                neighbours += 1
        if row_index + 1 < 6:  # bottom
            if self.board[row_index + 1][column_index] == "0":
                neighbours += 1
        return neighbours

    def chech_how_many_alive(self):
        n = 0
        for i in self.board:
            for j in i:
                if j == "0":
                    n += 1
        return n

    def one_iteration(self):
        for row_index, row in enumerate(self.board):
            for column_index, column in enumerate(row):
                # checking how many neighbours
                neighbours = self.how_many_neighbours(column_index, row_index)
                # is it dead or alive
                if column == "0":
                    if neighbours < 2:
                        self.board[row_index][column_index] = "."
                    elif neighbours > 3:
                        self.board[row_index][column_index] = "."
                else:
                    if neighbours == 3:
                        self.board[row_index][column_index] = "0"
        self.how_many_alive.append(self.chech_how_many_alive())
        self.how_many_iterations += 1

    def do_one_iteration(self):
        self.one_iteration()
        self.show_board()

    def draw_board(self):
        self.canvas.delete("all")
        tile_size = 50
        for row_index, row in enumerate(self.board):
            for column_index, column in enumerate(row):
                x1 = column_index * tile_size
                y1 = row_index * tile_size
                x2 = x1 + tile_size
                y2 = y1 + tile_size
                color = "green" if column == "0" else "red"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    def run_gui(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = GameOfLife()
    game.run_gui()
