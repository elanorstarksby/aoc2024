import re
import z3
from z3 import Solver


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [[int(b) for b in re.findall("\D(\d+)(?:\D|$)", a)] for a in input_file.read().split('\n\n')]
    return lines


def p1(games):
    p1_total = 0
    for game in games:
        min_tokens = 600
        found_solution = False
        for a in range(100):
            after_a = (a * game[0], a * game[1])
            b = (game[4] - after_a[0]) / game[2]
            if b % 1 == 0 and after_a[1] + (game[3] * b) == game[5]:
                if 3 * a + b < min_tokens:
                    min_tokens = 3 * a + (b // 1)
                    found_solution = True
        if found_solution:
            p1_total += min_tokens
    return p1_total


def p2(games):
    p2_total = 0
    z3.set_option()
    for game in games:
        a = z3.Int('a')
        b = z3.Int('b')
        ax, ay, bx, by, tx, ty = game
        tx += 10000000000000
        ty += 10000000000000
        s = Solver()
        s.add((a*ax) + (b*bx) == tx, (a*ay) + (b*by) == ty, a >= 0, b >= 0)
        if s.check() == z3.sat:
            m = s.model()
            print(m)
            if int(str(m[a])) < 0 or int(str(m[b])) < 0:
                return -1
            p2_total += int(str(m[a])) * 3 + int(str(m[b]))

    return p2_total


def main():
    values = read_in()
    print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
