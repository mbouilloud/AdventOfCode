import fileinput

class Element():
    def __init__(self, name, previous, size, level) -> None:
        self.name = name
        self.previous = previous
        self.level = level
        self.size = size

class Directory(Element):
    def __init__(self, name, previous, level) -> None:
        self.childs = []
        self.size = 0
        super().__init__(name, previous, 0, level)

    def __str__(self) -> str:
        s = " " * self.level
        s += "- " + self.name 
        s += " (dir, size=" + str(self.size) + ")"
        s += "\n"
        for e in self.childs:
            s += e.__str__()
        return s

class File(Element):
    def __init__(self, name, previous, size, level) -> None:
        super().__init__(name, previous, size, level)

    def __str__(self) -> str:
        s = " " * self.level
        s += "- " + self.name 
        s += " (file, size=" + str(self.size) + ")"
        s += "\n"
        return s

def resolve_size(element):
    if isinstance(element, Directory):
        count = 0
        for c in element.childs:
            count += resolve_size(c)
        element.size = count
        return count
    else:
        return element.size

def find_total_size_at_most(directory):
    if isinstance(directory, Directory):
        count = 0

        if(directory.size < 100000):
            count += directory.size
        
        for c in directory.childs:
            count += find_total_size_at_most(c)
        
        return count
    else:
        return 0

def find_directory_to_delete(directory, space, smallest):
    if(directory.size >= space and directory.size < smallest):
        smallest = directory.size
            
    for c in directory.childs:
        if isinstance(c, Directory):
            size = find_directory_to_delete(c, space, smallest)
            if(size < smallest):
                smallest = size

    return smallest

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
            file = File(elems[1], current, int(elems[0]), current.level + 1)
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

resolve_size(main)
# print(main)
# print(find_total_size_at_most(main))

necessary_free_space = 30000000 - (70000000 - main.size)
print(necessary_free_space)
print(find_directory_to_delete(main, necessary_free_space, main.size))

