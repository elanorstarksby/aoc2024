import re


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [[int(b) for b in re.findall("(-?\d+)", a)] for a in input_file.read().split('\n')]
    return lines


def p1(robots, times):
    len_x = 101
    len_y = 103
    qx = len_x // 2
    qy = len_y // 2
    qs = [0, 0, 0, 0]
    for r in robots:
        x = (r[0] + (times * r[2])) % len_x
        y = (r[1] + (times * r[3])) % len_y
        q = -1
        if x < qx and y < qy:
            q = 0
        if x < qx and y >= len_y - qy:
            q = 1
        if x >= len_x - qx and y < qy:
            q = 2
        if x >= len_x - qx and y >= len_y - qy:
            q = 3
        if q != -1:
            qs[q] += 1

    return qs[0] * qs[1] * qs[2] * qs[3]


def search_n(grid, n):
    for r in grid:
        count = 0
        for c in r:
            if c != 0:
                count += 1
            else:
                count = 0
            if count >= n:
                return True
    return False


def p2(robots):
    len_x = 101
    len_y = 103
    i = 0
    while True:
        i += 1
        grid = [[0 for _ in range(len_x)] for _ in range(len_y)]
        for r in robots:
            x = (r[0] + (i * r[2])) % len_x
            y = (r[1] + (i * r[3])) % len_y
            grid[y][x] += 1

        if search_n(grid, 7):
            print(i)
            for row in grid:
                print("".join(["." if r == 0 else "@" for r in row]))
            print()
            break

    return 0


def p2_levels(robots):
    average = p1(robots, 0)
    i = 0
    possible = []
    while True:
        i += 1
        level = p1(robots, i)
        if level < 0.3 * average:
            possible.append((i, level))
            print(possible)
        average = (i * average + level) / (i + 1)


def main():
    values = read_in()
    print(values)
    print(p1(values, 100))
    # print(p2(values))
    print(p2_levels(values))


if __name__ == '__main__':
    main()
