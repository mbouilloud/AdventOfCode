import fileinput

calories = []

counter = 0
 
for f in fileinput.input():
    line = f[:-1]

    if(len(line) == 0):
        calories.append(counter)
        counter = 0
    else:
        counter += int(line)

print(sum(sorted(calories, reverse = True)[:3]))