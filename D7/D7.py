import fileinput

class Element():
    def __init__(self, name, previous, level) -> None:
        self.name = name
        self.previous = previous
        self.level = level

class Directory(Element):
    def __init__(self, name, previous, level) -> None:
        self.childs = []
        super().__init__(name, previous, level)

    def __str__(self) -> str:
        s = " " * self.level
        s += "- " + self.name 
        s += " (dir)"
        s += "\n"
        for e in self.childs:
            s += e.__str__()
        return s

class File(Element):
    def __init__(self, name, previous, size, level) -> None:
        self.size = size
        super().__init__(name, previous, level)

    def __str__(self) -> str:
        s = " " * self.level
        s += "- " + self.name 
        s += " (file, size=" + self.size + ")"
        s += "\n"
        return s

current = Directory("/", None, 0)

main = current

for f in fileinput.input():
    line = f[:-1]

    if(line[0] != "$"):
        elems = line.split(" ")

        if(elems[0] == "dir"):
            dir = Directory(elems[1], current, current.level + 1)
            current.childs.append(dir)
        else:
            file = File(elems[1], current, elems[0], current.level + 1)
            current.childs.append(file)

    elif(line == "$ ls"):
        continue

    elif(line == "$ cd .."):
        current = current.previous

    elif(line == "$ cd /"):
        current = main

    else:
        elems = line.split(" ")

        for e in current.childs:
            if(e.name == elems[2]):
                current = e

print(main)