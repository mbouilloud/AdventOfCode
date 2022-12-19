import fileinput

class Monkey():

    def __init__(self, items, operation, test) -> None:
        self.items = items
        self.operation = operation
        self.test = test

def create_lambda_op(line):
    line = line[:-1]

    ele = line.split(":")[1].split(" ")[3:]
    op = ele[1]

    if(ele[2].isnumeric()):
        v = int(ele[2])
        if(op == "*"):
            return lambda old: old * v
        elif(op == "+"):
            return lambda old: old + v
    else:
        if(op == "*"):
            return lambda old: old * old
        elif(op == "+"):
            return lambda old: old + old

def create_lambda_test(line_test, true, false):
    line_test = line_test[:-1]
    true = true[:-1]
    false = false[:-1]

    div = int(line_test.split(" ")[-1])
    monkey_true = int(true.split(" ")[-1])
    monkey_false = int(false.split(" ")[-1])
    return lambda v: monkey_true if(v % div == 0) else monkey_false
 
monkeys = []

with open("input.txt") as myfile:

    while True:
        head = [next(myfile) for x in range(6)]

        l = head[1].split(":")[1].split(",")

        items = [int(c) for c in l if len(c) > 0]
        op = create_lambda_op(head[2])
        test = create_lambda_test(*(head[3:]))
        
        monkeys.append(Monkey(items, op, test))

        try:
            c = next(myfile)
        except StopIteration:
            break