import fileinput

line_c = 0
lines = []
count = 0

for f in fileinput.input():
    line_c += 1
    lines.append(f[:-1])

    if(line_c == 3):
        comp1 = set(lines[0])
        comp2 = set(lines[1])
        comp3 = set(lines[2])

        item = next(iter(comp1.intersection(comp2).intersection(comp3)))

        if(item.islower()):
            count += ord(item) - ord('a') + 1
        else:
            count += ord(item) - ord('A') + 27

        lines = []
        line_c = 0

print(count)