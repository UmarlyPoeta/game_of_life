import random
import sys

list_of_options=["0","."]

class GameOfLife:
    def __init__(self):
        self.board=[[random.choice(list_of_options) for i in range(6)] for _ in range(6)]
    
    def show(self):
        for i in self.board:
            for j in i:
                print(f" {j} ",end="")
            print(f"\n")
    
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
        
    def menu(self):
        while True:
            print("1.show a board")
            print("2. Do 1 iteration")
            print("3.Exit \n")
            choice=input(": ")
            match choice:
                case "1":
                    self.show()
                case "2":
                    self.one_iteration()
                case "3":
                    sys.exit()
                case _:
                    continue
                    
            


game=GameOfLife()
game.menu()
