import fileinput

count = 0

for f in fileinput.input():
    line = f[:-1]

    first = line.split(",")[0]
    second = line.split(",")[1]

    f_r_s = int(first.split("-")[0])
    f_r_e = int(first.split("-")[1])

    s_r_s = int(second.split("-")[0])
    s_r_e = int(second.split("-")[1])

    first = set(range(f_r_s, f_r_e + 1))
    second = set(range(s_r_s, s_r_e + 1))

    if(len(first.intersection(second)) != 0):
        count += 1 

print(count)