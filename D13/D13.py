import fileinput
import json
    
index = []

def check(e1, e2):
    if(len(e1) == 0 and len(e2) > 0):
        return 1
    elif(len(e1) > 0 and len(e2) == 0):
        return 0
    elif(len(e1) == 0 and len(e2) == 0):
        return -1

    v1 = e1[0]
    v2 = e2[0]

    if(isinstance(v1, int) and isinstance(v2, int)):
        if(v1 < v2):
            return 1
        elif(v1 > v2):
            return 0
        else:
            return check(e1[1:], e2[1:])

    elif(isinstance(v1, list) and isinstance(v2, list)):
        v = check(v1, v2)
        if(v == 1 or v == 0):
            return v
        return check(e1[1:], e2[1:])

    elif(isinstance(v1, int) and isinstance(v2, list)):
        e1[0] = [v1]
        return check(e1, e2)

    elif(isinstance(v1, list) and isinstance(v2, int)):
        e2[0] = [v2]
        return check(e1, e2)

    return -1

packets = []
with open("input.txt") as myfile:

    while True:
        head = [next(myfile) for x in range(2)]

        packets.append(json.loads(head[0]))
        packets.append(json.loads(head[1]))

        try:
            c = next(myfile)
        except StopIteration:
            break

sorted_packets = [packets[0]]

for p in packets[1:]:
    found = False

    for i in range(len(sorted_packets)):
        if(check(p, sorted_packets[i]) == 1 and not found):
            sorted_packets.insert(i, p)
            found = True

    if(not found):
        sorted_packets.append(p)

index = []
divider1 = [[2]]
divider2 = [[6]]

for i in range(len(sorted_packets)):
    if(check(divider1, sorted_packets[i]) == 1):
        index.append(i + 1)
        sorted_packets.insert(i, divider1)
        break

for i in range(len(sorted_packets)):
    if(check(divider2, sorted_packets[i]) == 1):
        index.append(i + 1)
        sorted_packets.insert(i, divider2)
        break

print(index[0] * index[1])