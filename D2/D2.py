import fileinput

score = 0
 
for f in fileinput.input():
    first = f[0]
    second = f[2]

    if(first == 'A'):
        if(second == 'X'):
            score += 3
        elif(second == 'Y'):
            score += 4
        else:
            score += 8
    elif(first == 'B'):
        if(second == 'X'):
            score += 1
        elif(second == 'Y'):
            score += 5
        else:
            score += 9
    else:
        if(second == 'X'):
            score += 2
        elif(second == 'Y'):
            score += 6
        else:
            score += 7

print(score)