import numpy as np
import fileinput
import re

X = 700
cave = np.zeros((600, X))

y_max = 0
 
for f in fileinput.input():
    line = f[:-1]
    s = line.split("->")

    for i in range(len(s) - 1):
        ele1 = [int(c) for c in s[i].split(",")]
        ele2 = [int(c) for c in s[i + 1].split(",")]

        if(ele1[1] > y_max):
            y_max = ele1[1]

        if(ele2[1] > y_max):
            y_max = ele2[1]

        if(ele1[0] > ele2[0]):
            for j in range(ele2[0], ele1[0] + 1):
                cave[ele1[1], j] = 1
        elif(ele1[0] < ele2[0]):
            for j in range(ele1[0], ele2[0] + 1):
                cave[ele1[1], j] = 1
        elif(ele1[1] > ele2[1]):
            for j in range(ele2[1], ele1[1] + 1):
                cave[j, ele1[0]] = 1
        elif(ele1[1] < ele2[1]):
            for j in range(ele1[1], ele2[1] + 1):
                cave[j, ele1[0]] = 1

y_max += 2

for i in range(X):
    cave[y_max, i] = 1 

i = 0
while(True):
    can_moove = True
    x_pos = 500
    y_pos = 0
    cave[y_pos, x_pos] = -1

    try:
        while(can_moove):
                
            if(cave[y_pos + 1, x_pos] == 0):
                cave[y_pos, x_pos] = 0
                cave[y_pos + 1, x_pos] = -1
                y_pos += 1

            elif(cave[y_pos + 1, x_pos - 1] == 0):
                cave[y_pos, x_pos] = 0
                cave[y_pos + 1, x_pos - 1] = -1
                y_pos += 1
                x_pos -= 1

            elif(cave[y_pos + 1, x_pos + 1] == 0):
                cave[y_pos, x_pos] = 0
                cave[y_pos + 1, x_pos + 1] = -1
                y_pos += 1
                x_pos += 1

            else:
                can_moove = False

    except IndexError:
        break

    if(cave[0, 500] == -1):
        print(i  + 1)
        break

    i += 1

# for i in range(0, y_max  + 1):
#     string = ""
#     for j in range(300, X):
#         v = cave[i][j]
#         if(v == 0):
#             string += "."
#         elif(v == 1):
#             string += "#"
#         else:
#             string += "o"
#     print(string)
