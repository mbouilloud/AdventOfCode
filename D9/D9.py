import fileinput
import numpy as np

counter = 0

class Extendable_Grid():

    def __init__(self) -> None:
        self.grid = np.array([[1]])
        self.index_head = np.array([0, 0])
        self.index_tail = np.array([0, 0])
        self.counter = 1

    def go_left(self):
        if(self.index_head[1] == 0):
            self.grid = np.concatenate((np.zeros((len(self.grid), 1)), self.grid), axis = 1)
            self.index_tail[1] += 1
            self.index_head[1] += 1
        self.index_head[1] -= 1
        self.ajust_tail()        

    def go_right(self):
        if(self.index_head[1] == len(self.grid[0]) - 1):
            self.grid = np.concatenate((self.grid, np.zeros((len(self.grid), 1))), axis = 1)
        self.index_head[1] += 1
        self.ajust_tail()        

    def go_up(self):
        if(self.index_head[0] == 0):
            self.grid = np.concatenate((np.zeros((1, len(self.grid[0]))), self.grid), axis = 0)
            self.index_tail[0] += 1
            self.index_head[0] += 1
        self.index_head[0] -= 1
        self.ajust_tail()        

    def go_down(self):
        if(self.index_head[0] == len(self.grid) - 1):
            self.grid = np.concatenate((self.grid, np.zeros((1, len(self.grid[0])))), axis = 0)
        self.index_head[0] += 1
        self.ajust_tail()        

    def ajust_tail(self):
        X_head, Y_head = tuple(self.index_head)
        X_tail, Y_tail = tuple(self.index_tail)
        
        if(abs(Y_head - Y_tail) == 2):
            # Right
            if(X_head == X_tail and Y_head > Y_tail):
                self.index_tail[1] += 1
            
            # Left
            elif(X_head == X_tail and Y_head < Y_tail):
                self.index_tail[1] -= 1

        if(abs(X_head - X_tail) == 2):
            # Down
            if(Y_head == Y_tail and X_head > X_tail):
                self.index_tail[0] += 1

            # Up
            elif(Y_head == Y_tail and X_head < X_tail):
                self.index_tail[0] -= 1


        if(abs(X_head - X_tail) == 2 or abs(Y_head - Y_tail) == 2):
            # Diag right-up
            if(X_head < X_tail and Y_head > Y_tail):
                self.index_tail[0] -= 1
                self.index_tail[1] += 1

            # Diag left-up
            if(X_head < X_tail and Y_head < Y_tail):
                self.index_tail[0] -= 1
                self.index_tail[1] -= 1

            # Diag right-down
            if(X_head > X_tail and Y_head > Y_tail):
                self.index_tail[0] += 1
                self.index_tail[1] += 1

            # Diag left-down
            if(X_head > X_tail and Y_head < Y_tail):
                self.index_tail[0] += 1
                self.index_tail[1] -= 1

        if(self.grid[tuple(self.index_tail)] != 1):
            self.counter += 1
        self.grid[tuple(self.index_tail)] = 1
        

grid = Extendable_Grid()
# print(grid.grid)

for f in fileinput.input():
    if(f[-1:] == "\n"):
        line = f[:-1]
    else:
        line = f

    ele = line.split(" ")
    direction = ele[0]
    steps = ele[1]

    for i in range(int(steps)):
        if direction == 'L':
            grid.go_left()
        elif direction == 'R':
            grid.go_right()
        elif direction == 'U':
            grid.go_up()
        else:
            grid.go_down()

        # print("----------")
        # print(direction)
        # print(grid.index_head)
        # print(grid.index_tail)
        # print(grid.grid)

print(grid.counter)
