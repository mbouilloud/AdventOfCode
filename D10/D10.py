import fileinput

counter = 0

X = 1

in_flight_inst = []

CRT = [["." for i in range(40)] for _ in range(6)]

s = []
 
for f in fileinput.input():
    if(f[-1:] == "\n"):
        line = f[:-1]
    else:
        line = f
    
    counter += 1

    # Update
    if(len(in_flight_inst) != 0):
        v = in_flight_inst.pop()
        X += v

    if(line == "noop"):
        in_flight_inst.insert(0, 0)
    else:
        ele = line.split(" ")
        
        incr = int(ele[1])

        # in_flight_inst.insert(0, 0)
        in_flight_inst.insert(0, 0)
        in_flight_inst.insert(0, incr)

    for j in range(20, 260, 40):
        if(counter == j):
            s.append(counter * X)


    # print("-------")


    line = int((counter - 1) / 40)
    column = (counter - 1) % 40

    # print(counter)
    # print(line)
    # print(column)
    # print(X)

    if(X == column or X - 1 == column or X + 1 == column):
        CRT[line][column] = "#"

    # print("cycle: " + str(counter) +" , X = " + str(X)) 

for i in range(len(in_flight_inst)):
    counter += 1

    # Update
    if(len(in_flight_inst) != 0):
        v = in_flight_inst.pop()
        X += v

    for j in range(20, 260, 40):
        if(counter == j):
            s.append(counter * X)

    line = int((counter - 1) / 40)
    column = (counter - 1) % 40

    if(X == column or X - 1 == column or X + 1 == column):
        CRT[line][column] = "#"

    # print("cycle: " + str(counter) +" , X = " + str(X)) 
print(s)
print(sum(s))

for i in range(len(CRT)):
    string = ""
    for j in range(len(CRT[0])):
        string += CRT[i][j]
    print(string)