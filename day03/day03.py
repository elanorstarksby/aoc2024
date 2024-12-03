import re

def read_in():
    with open("input.txt", "r") as input_file:
        lines = input_file.read()
    return lines


def p1(values):
    multiplies = re.findall("mul\(\d+,\d+\)",values)
    p1_total = 0
    for m in multiplies:
        (v1,v2) = (int(v) for v in m[4:-1].split(","))
        p1_total += v1 * v2
    return p1_total


def p2(values):
    multiplies = re.findall("mul\(\d+,\d+\)|do\(\)|don\'t\(\)",values)
    print(multiplies)
    p2_total = 0
    do = True
    for m in multiplies:
        instr, vals = m.split("(")
        if instr == "don't":
            do = False
        elif instr == "do":
            do = True
        elif instr == "mul" and do == True:
            (v1,v2) = (int(v) for v in vals[:-1].split(","))
            p2_total += v1 * v2
    return p2_total


def main():
    values = read_in()
    # print(values)
    print(p1(values))
    eg = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    print("e.g.",p2(eg))
    print(p2(values))


if __name__ == '__main__':
    main()
