def read_in():
    with open("input.txt", "r") as input_file:
        lines = [a.split("\n") for a in input_file.read().split('\n\n')]
    return lines


def swap(grid, a, b):
    ra, ca = a
    rb, cb = b
    va = grid[ra][ca]
    vb = grid[rb][cb]
    grid[ra] = grid[ra][:ca] + vb + grid[ra][ca + 1:]
    grid[rb] = grid[rb][:cb] + va + grid[rb][cb + 1:]


def p1(values):
    grid = values[0]
    sequence = "".join(values[1])
    robot = (-1, -1)
    for ri, r in enumerate(grid):
        for ci, c in enumerate(r):
            if c == "@":
                robot = (ri, ci)
                break
    grid[robot[0]] = grid[robot[0]][:robot[1]] + "." + grid[robot[0]][robot[1] + 1:]
    moves = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
    for move in sequence:
        # print(robot, move)
        # for row in grid:
        #     print(row)
        m = moves[move]
        next_robot = (robot[0] + m[0], robot[1] + m[1])
        if grid[next_robot[0]][next_robot[1]] == "#":
            continue
        if grid[next_robot[0]][next_robot[1]] == ".":
            robot = next_robot
            continue
        search_l = next_robot
        while grid[search_l[0]][search_l[1]] == "O":
            search_l = (search_l[0] + m[0], search_l[1] + m[1])
        if grid[search_l[0]][search_l[1]] == "#":
            continue
        else:
            robot = next_robot
            swap(grid, next_robot, search_l)

    p1_total = 0
    for ri, r in enumerate(grid):
        for ci, c in enumerate(r):
            if c == "O":
                p1_total += (100 * ri) + ci
    return p1_total


def try_move(grid, location, direction):
    lr, lc = location
    if grid[lr][lc] == ".":
        return True

    if grid[lr][lc] == "#":
        return False

    if grid[lr][lc] == "]":
        lc -= 1

    if (try_move(grid, (lr + direction, lc), direction)
            and try_move(grid, (lr + direction, lc + 1), direction)):
        grid[lr + direction][lc] = "["
        grid[lr + direction][lc + 1] = "]"
        grid[lr][lc] = "."
        grid[lr][lc + 1] = "."
        return True
    return False


def p2(values):
    grid = values[0]
    sequence = "".join(values[1])
    double_grid = []
    robot = (-1, -1)
    for ri, r in enumerate(grid):
        double_r = []
        for ci, c in enumerate(r):
            if c == "@":
                robot = (ri, ci * 2)
            double_v = {"#": "##", "O": "[]", ".": "..", "@": ".."}
            double_r.append(double_v[c][0])
            double_r.append(double_v[c][1])
        double_grid.append(double_r)
    # for row in double_grid:
    #     print(row)
    # for row in double_grid:
    #     print("".join(row))
    grid = double_grid
    # print(robot)

    moves = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
    for move in sequence:
        # for row in double_grid:
        #     print("".join(row))
        # print()

        m = moves[move]
        next_robot = (robot[0] + m[0], robot[1] + m[1])
        if m[0] == 0:
            if grid[next_robot[0]][next_robot[1]] == "#":
                continue
            if grid[next_robot[0]][next_robot[1]] == ".":
                robot = next_robot
                continue
            search_l = next_robot
            while grid[search_l[0]][search_l[1]] in ["[", "]"]:
                search_l = (search_l[0] + m[0], search_l[1] + m[1])
            if grid[search_l[0]][search_l[1]] == "#":
                continue
            else:
                grid[next_robot[0]][next_robot[1]], grid[search_l[0]][search_l[1]] = (
                    grid[search_l[0]][search_l[1]], grid[next_robot[0]][next_robot[1]]
                )
                for i in range(next_robot[1] + m[1], search_l[1] + m[1], m[1]):
                    grid[robot[0]][i] = "[" if grid[robot[0]][i] == "]" else "]"
                robot = next_robot

        else:
            proposed_grid = [[value for value in row] for row in grid]
            if try_move(proposed_grid, next_robot, m[0]):
                grid = proposed_grid
                robot = next_robot

    # for row in grid:
    #     print("".join(row))

    p2_total = 0
    for ri, r in enumerate(grid):
        for ci, c in enumerate(r):
            if c == "[":
                p2_total += (100 * ri) + ci
    return p2_total


def main():
    values = read_in()
    print(values)
    print(p1([[b for b in a] for a in values]))
    print(p2(values))


if __name__ == '__main__':
    main()
