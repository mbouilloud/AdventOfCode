import fileinput

dict = {}

for f in fileinput.input():
    line = f[:-1]

    elements = line.split(" ")

    if(len(elements) > 1 and elements[0] != "move" and elements[1] != "1"):

        for i in range(len(line)):

            if(line[i] == "["):
                element = line[i+1:i+2]

                index = int(i / 4 + 1)

                if index not in dict.keys():
                    dict[index] = []

                dict[index].insert(0, element)

                i += 2

    if(elements[0] == "move"):
        first = int(elements[1])
        second = int(elements[3])
        third = int(elements[5])

        l = []

        for i in range(first):
            l.append(dict[second].pop())

        for i in range(first):
            v = l.pop()
            dict[third].append(v)

print(dict)