import fileinput

sensors = []
beacons = []

for line in fileinput.input():
    line = line.replace(",", "").replace(":", "").replace("x=", "").replace("y=", "").strip().split(" ")
    x_beacon = int(line[8])
    y_beacon = int(line[9])
    x_sensor = int(line[2])
    y_sensor = int(line[3])

    beacons.append((x_beacon, y_beacon))
    sensors.append((x_sensor, y_sensor))

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))


x_min = max(min([x[0] for x in sensors]), 0)
x_max = min(max([x[0] for x in sensors]), 4000000)

y_min = max(min([x[1] for x in sensors]), 0)
y_max = min(max([x[1] for x in sensors]), 4000000)


for y in range(y_min, y_max):
    for x in range(x_min, x_max):
        pos = (x, y)
        can = True

        for s, b in zip(sensors, beacons):
            if(manhattan(s, pos) <= manhattan(s, b)):
                can = False
                break

        if(can):
            print(pos)
            exit()