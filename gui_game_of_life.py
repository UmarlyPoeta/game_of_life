import random
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

list_of_options = ["0", "."]
row_number = 6
column_number = 6

class GameOfLife:
    def __init__(self):
        self.board = [[random.choice(list_of_options) for _ in range(column_number)] for _ in range(row_number)]
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

        self.one_iteration_button = tk.Button(self.root, text="Do Iterations", command=self.do_one_iteration)
        self.one_iteration_button.pack(side=tk.LEFT)

        self.show_evolution_button = tk.Button(self.root, text="Show Evolution", command=self.make_a_plot)
        self.show_evolution_button.pack(side=tk.LEFT)

        self.clear_board_button = tk.Button(self.root, text="Clear Board", command=self.clear_board)
        self.clear_board_button.pack(side=tk.LEFT)

        self.random_fill_button = tk.Button(self.root, text="Random Fill", command=self.random_fill)
        self.random_fill_button.pack(side=tk.LEFT)

        self.save_board_button = tk.Button(self.root, text="Save Board", command=self.save_board)
        self.save_board_button.pack(side=tk.LEFT)

        self.load_board_button = tk.Button(self.root, text="Load Board", command=self.load_board)
        self.load_board_button.pack(side=tk.LEFT)

        self.speed_scale = tk.Scale(self.root, label="Animation Speed", from_=1, to=10, orient=tk.HORIZONTAL)
        self.speed_scale.set(5)
        self.speed_scale.pack(side=tk.LEFT)

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
            if row_index + 1 < row_number:  # leftbottom
                if self.board[row_index + 1][column_index - 1] == "0":
                    neighbours += 1
        if column_index + 1 < column_number:  # right
            if self.board[row_index][column_index + 1] == "0":
                neighbours += 1
            if row_index - 1 >= 0:  # righttop
                if self.board[row_index - 1][column_index + 1] == "0":
                    neighbours += 1
            if row_index + 1 < row_number:  # rightbottom
                if self.board[row_index + 1][column_index + 1] == "0":
                    neighbours += 1
        if row_index - 1 >= 0:  # top
            if self.board[row_index - 1][column_index] == "0":
                neighbours += 1
        if row_index + 1 < row_number:  # bottom
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
                neighbours = self.how_many_neighbours(column_index, row_index)
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
        speed = self.speed_scale.get()
        for _ in range(speed):
            self.one_iteration()
            self.draw_board()
            self.root.update()
            self.root.after(100)  # Pause for a short while between iterations

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

    def clear_board(self):
        self.board = [["." for _ in range(column_number)] for _ in range(row_number)]
        self.how_many_iterations = 0
        self.how_many_alive = []
        self.how_many_alive.append(self.chech_how_many_alive())
        self.draw_board()

    def random_fill(self):
        self.board = [[random.choice(list_of_options) for _ in range(column_number)] for _ in range(row_number)]
        self.how_many_iterations = 0
        self.how_many_alive = []
        self.how_many_alive.append(self.chech_how_many_alive())
        self.draw_board()

    def save_board(self):
        with open("saved_board.txt", "w") as file:
            for row in self.board:
                file.write(" ".join(row) + "\n")

    def load_board(self):
        try:
            with open("saved_board.txt", "r") as file:
                loaded_board = [list(line.strip()) for line in file]
            if len(loaded_board) == row_number and all(len(row) == column_number for row in loaded_board):
                self.board = loaded_board
                self.how_many_iterations = 0
                self.how_many_alive = []
                self.how_many_alive.append(self.chech_how_many_alive())
                self.draw_board()
            else:
                print("Invalid file format.")
        except FileNotFoundError:
            print("No saved board found.")

    def change_size(self):
        global row_number, column_number
        new_row_number = int(input("Enter the new number of rows: "))
        new_column_number = int(input("Enter the new number of columns: "))
        self.board = [[random.choice(list_of_options) for _ in range(new_column_number)] for _ in range(new_row_number)]
        row_number, column_number = new_row_number, new_column_number
        self.how_many_iterations = 0
        self.how_many_alive = []
        self.how_many_alive.append(self.chech_how_many_alive())
        self.draw_board()

    def run_gui(self):
        self.root.mainloop()

def main():
    game = GameOfLife()
    game.run_gui()

if __name__ == "__main__":
    main()
