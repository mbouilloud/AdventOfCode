import fileinput

counter = 0
 
for f in fileinput.input():
    if(f[-1:] == "\n"):
        line = f[:-1]
    else:
        line = f

    print(f)
