import random
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#list of options where "0"=alive cell and "."=dead cell
list_of_options = ["0", "."]
row_number=6
column_number=6

class GameOfLife:
    def __init__(self):
        """
        init function that declares randomly generated board with values "0" meaning alive cell and 
        "." meaning dead cell. Function also declares tkinter widgets like buttons, canvas and frame
        
        """
        self.board = [[random.choice(list_of_options) for _ in range(column_number)] for _ in range(row_number)] #randomly generated board
        self.how_many_iterations = 0 #number of iterations
        self.how_many_alive = [] #numbers of alive cells at iteration number index
        self.how_many_alive.append(self.chech_how_many_alive()) #adds 0 iteration index value of alive cells

        #root
        self.root = tk.Tk()
        self.root.title("Game of Life")

        #frame
        self.canvas_frame = tk.Frame(self.root) 
        self.canvas_frame.pack(side=tk.TOP)

        #canvas
        self.canvas = tk.Canvas(self.canvas_frame, width=300, height=300) 
        self.canvas.pack()

        #board button
        self.show_board_button = tk.Button(self.root, text="Show Board", command=self.show_board)
        self.show_board_button.pack(side=tk.LEFT)


        #do 1 iteration button
        self.one_iteration_button = tk.Button(self.root, text="Do 1 Iteration", command=self.do_one_iteration)
        self.one_iteration_button.pack(side=tk.LEFT)

        
        #show evolution button
        self.show_evolution_button = tk.Button(self.root, text="Show Evolution", command=self.make_a_plot)
        self.show_evolution_button.pack(side=tk.LEFT)


        #exit button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.end)
        self.exit_button.pack(side=tk.LEFT)

    def show(self):
        """
        function that prints board
        """
        for row in self.board:
            print(" ".join(row))
        print()

    def show_board(self):
        self.draw_board()

    def end(self):
        """
        function that exits program
        """
        self.root.destroy()

    def make_a_plot(self):
        """Function that makes a graph based on number of iteration and number of alive cells
        """
        x = np.array([i for i in range(0, self.how_many_iterations + 1)])
        y = np.array(self.how_many_alive)
        plt.scatter(x, y)
        plt.title("Plot")
        plt.xlabel("Iteration number")
        plt.ylabel("Number of alive cells")
        plt.show()

    def how_many_neighbours(self, column_index, row_index):
        """function checks how many neighbours each cell have

        Args:
            column_index (int): cell column index
            row_index (int): cell row index

        Returns:
            int: number of neighbours
        """
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
        """function that returns how many alive cells are in each iteration

        Returns:
            int: number of alive cells in iteration
        """
        n = 0
        for i in self.board:
            for j in i:
                if j == "0":
                    n += 1
        return n

    def one_iteration(self):
        """function that does one iteration,checks how many neighbours each cell have and based
        on that change them based on game criteria
        """
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
        """function that does one iteration and shows the gui board
        """
        self.one_iteration()
        self.show_board()

    def draw_board(self):
        """function that draws board
        """
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
        """function that runs mainloop
        """
        self.root.mainloop()


if __name__ == "__main__":
    game = GameOfLife()
    game.run_gui()
