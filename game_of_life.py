import random
import sys
import os
import numpy as np
import matplotlib.pyplot as plt 

list_of_options=["0","."]

class GameOfLife:
    def __init__(self):
        self.board=[[random.choice(list_of_options) for _ in range(6)] for _ in range(6)]
        self.how_many_iterations=0
        self.how_many_alive=[]
    
    def show(self):
        a=np.array(self.board)
        print(str(a.reshape(6,6)).replace("[","").replace("]","").replace("'"," "))
        
    
    def make_a_plot(self):
        x=np.array([i for i in range(0,self.how_many_iterations+1)])
        y=np.array(self.how_many_alive)
        plt.scatter(x, y)
        plt.title("plot")
        plt.xlabel("iteration number")
        plt.ylabel("number of alive cells")
        plt.legend()
        plt.show()
        
        
    
    def how_many_neighbours(self,column_index,row_index):
        neighbours=0
        if column_index-1>=0: #left
            if self.board[row_index][column_index-1]=="0":
                neighbours+=1
            if row_index-1>=0: #lefttop
                if self.board[row_index-1][column_index-1]=="0":
                    neighbours+=1
            if row_index+1<6: #leftbottom
                if self.board[row_index+1][column_index-1]=="0":
                    neighbours+=1
        if column_index+1<6: #right
            if self.board[row_index][column_index+1]=="0":
                neighbours+=1
            if row_index-1>=0: #righttop
                if self.board[row_index-1][column_index+1]=="0":
                    neighbours+=1
            if row_index+1<6: #rightbottom
                if self.board[row_index+1][column_index+1]=="0":
                    neighbours+=1
        if row_index-1>=0: #top
            if self.board[row_index-1][column_index]=="0":
                neighbours+=1
        if row_index+1<6: #bottom
            if self.board[row_index+1][column_index]=="0":
                neighbours+=1
        return neighbours
    
    def chech_how_many_alive(self):
        n=0
        for i in self.board:
            for j in i:
                if j=="0":
                    n+=1
        return n
    
    def one_iteration(self):
        for row_index,row in enumerate(self.board):
            for column_index,column in enumerate(row):
                #checking how many neighbours
                neighbours=self.how_many_neighbours(column_index,row_index)
                #is it dead or alive
                if column=="0":
                    if neighbours<2:
                        self.board[row_index][column_index]="."
                    elif neighbours>3:
                        self.board[row_index][column_index]="."
                else:
                    if neighbours==3:
                        self.board[row_index][column_index]="0"
        self.how_many_alive.append(self.chech_how_many_alive())
        
        
    def menu(self):
        self.how_many_alive.append(self.chech_how_many_alive())
        while True:
            os.system("cls")
            print("1.show a board")
            print("2. Do 1 iteration")
            print("3.show a evolution")
            print("4.Exit \n")
            choice=input(": ")
            os.system("cls")
            match choice:
                case "1":
                    self.show()
                    input()
                case "2":
                    self.one_iteration()
                    self.how_many_iterations+=1
                case "3":
                    self.make_a_plot()
                case "4":
                    sys.exit()
                case _:
                    continue
                    
            

if __name__=="__main__":
    game=GameOfLife()
    game.menu()
