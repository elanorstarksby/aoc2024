from datetime import datetime

def read_in():
    with open("input.txt", "r") as input_file:
        lines = [[int(line.strip().split(": ")[0]), [int(a) for a in line.strip().split(": ")[1].split(" ")]] for line
                 in
                 input_file]
    return lines


def add_vals(count, vals):
    return count + vals[0]


def mul_vals(count, vals):
    return count * vals[0]


def concat_vals(count, vals):
    return int(str(count) + str(vals[0]))


def operators(goal, vals, count, p=1):
    if count > goal:
        return False
    if len(vals) == 1:
        return add_vals(count, vals) == goal or mul_vals(count, vals) == goal or (
                    p == 2 and concat_vals(count, vals) == goal)
    a = add_vals(count, vals)
    m = mul_vals(count, vals)
    c = concat_vals(count, vals)
    return operators(goal, vals[1:], a, p) or operators(goal, vals[1:], m, p) or (p == 2 and operators(goal, vals[1:], c, p))


def p1(values):
    p1_total = 0
    for v in values:
        if operators(v[0], v[1][1:], v[1][0]):
            p1_total += v[0]

    return p1_total


def p2(values):
    p2_total = 0
    for v in values:
        if operators(v[0], v[1][1:], v[1][0], 2):
            p2_total += v[0]

    return p2_total


def main():
    t3 = datetime.now()
    values = read_in()

    print(datetime.now()-t3)
    print(values)
    t = datetime.now()
    print(p1(values))
    print(datetime.now()-t)
    t2 = datetime.now()
    print(p2(values))
    print(datetime.now()-t2)


if __name__ == '__main__':
    main()
