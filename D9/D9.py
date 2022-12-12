import fileinput
import numpy as np

counter = 0

class Extendable_Grid():

    def __init__(self) -> None:
        self.grid = np.array([[1]])
        self.index_head = np.array([0, 0])
        self.index_tails = np.vstack([[0, 0]]*9)
        self.counter = 1

    def go_left(self):
        if(self.index_head[1] == 0):
            self.grid = np.concatenate((np.zeros((len(self.grid), 1)), self.grid), axis = 1)
            for i in range(9):
                self.index_tails[i][1] += 1
            self.index_head[1] += 1
        self.index_head[1] -= 1
        self.adjust_all_tails()        

    def go_right(self):
        if(self.index_head[1] == len(self.grid[0]) - 1):
            self.grid = np.concatenate((self.grid, np.zeros((len(self.grid), 1))), axis = 1)
        self.index_head[1] += 1
        self.adjust_all_tails()        

    def go_up(self):
        if(self.index_head[0] == 0):
            self.grid = np.concatenate((np.zeros((1, len(self.grid[0]))), self.grid), axis = 0)
            for i in range(9):
                self.index_tails[i][0] += 1
            self.index_head[0] += 1
        self.index_head[0] -= 1
        self.adjust_all_tails()        

    def go_down(self):
        if(self.index_head[0] == len(self.grid) - 1):
            self.grid = np.concatenate((self.grid, np.zeros((1, len(self.grid[0])))), axis = 0)
        self.index_head[0] += 1
        self.adjust_all_tails()   

    def adjust_all_tails(self):
        # Head and first tail
        X_tail, Y_tail = self.adjust_tail_with_respect_to_other(tuple(self.index_head), tuple(self.index_tails[0]), 1)
        self.index_tails[0][0] = X_tail
        self.index_tails[0][1] = Y_tail

        for i in range(0, 8):
            if(i == 7):
                last = True
            else:
                last = False
                
            X_tail, Y_tail = self.adjust_tail_with_respect_to_other(tuple(self.index_tails[i]), tuple(self.index_tails[i+1]), i + 2, last)
            self.index_tails[i+1][0] = X_tail
            self.index_tails[i+1][1] = Y_tail

    def adjust_tail_with_respect_to_other(self, first, second,  i, last = False):
        X_head, Y_head = first
        X_tail, Y_tail = second

        # self.grid[X_tail, Y_tail] = 0
        
        if(abs(Y_head - Y_tail) == 2):
            # Right
            if(X_head == X_tail and Y_head > Y_tail):
                Y_tail += 1
            
            # Left
            elif(X_head == X_tail and Y_head < Y_tail):
                Y_tail -= 1

        if(abs(X_head - X_tail) == 2):
            # Down
            if(Y_head == Y_tail and X_head > X_tail):
                X_tail += 1

            # Up
            elif(Y_head == Y_tail and X_head < X_tail):
                X_tail -= 1

        if(abs(X_head - X_tail) == 2 or abs(Y_head - Y_tail) == 2):
            # Diag right-up
            if(X_head < X_tail and Y_head > Y_tail):
                X_tail -= 1
                Y_tail += 1

            # Diag left-up
            if(X_head < X_tail and Y_head < Y_tail):
                X_tail -= 1
                Y_tail -= 1

            # Diag right-down
            if(X_head > X_tail and Y_head > Y_tail):
                X_tail += 1
                Y_tail += 1

            # Diag left-down
            if(X_head > X_tail and Y_head < Y_tail):
                X_tail += 1
                Y_tail -= 1

        if(last):
            if(self.grid[X_tail, Y_tail] != 1):
                self.counter += 1
            self.grid[X_tail, Y_tail] = 1
        # self.grid[X_tail, Y_tail] = i

        return X_tail, Y_tail

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
        # print(grid.grid)

print(grid.counter)
