import fileinput

s = []
line = next(fileinput.input())[:-1]

print(len(line))

for i in range(len(line)):
    s.insert(0, line[i])

    if(len(s) > 14):
        s.pop()

    if(len(set(s)) == 14):
        print(i + 1)
        break