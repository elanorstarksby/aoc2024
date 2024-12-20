def read_in():
    with open("input.txt", "r") as input_file:
        lines = input_file.read().split('\n')
    return lines


def search(grid, s):
    distances = {s: 0}
    to_visit = [s]
    while to_visit:
        r, c = to_visit.pop(0)
        if grid[r][c] == "E":
            return distances
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if (not (0 <= r + dr < len(grid))) or (not (0 <= c + dc < len(grid[0]))):
                continue
            if grid[r + dr][c + dc] in (".", "E") and (r + dr, c + dc) not in distances:
                distances[(r + dr, c + dc)] = distances[(r, c)] + 1
                to_visit.append((r + dr, c + dc))


def p1(grid):
    s = (0, 0)
    for ri, r in enumerate(grid):
        for ci, c in enumerate(list(r)):
            if c == "S":
                s = (ri, ci)
    # print(s)
    distances = search(grid, s)
    # print(distances)
    total = 0
    for r, c in distances:
        for dr, dc in ((0, 2), (0, -2), (2, 0), (-2, 0)):
            if (r + dr, c + dc) not in distances:
                continue
            better_by = distances[(r + dr, c + dc)] - distances[(r, c)] - 2
            if better_by >= 100:
                total += 1

    return total


def p2(grid):
    s = (0, 0)
    for ri, r in enumerate(grid):
        for ci, c in enumerate(list(r)):
            if c == "S":
                s = (ri, ci)
    # print(s)
    distances = search(grid, s)
    # print(distances)
    total = 0
    for r, c in distances:
        for dr in range(-20, 21):
            for dc in range(-20, 21):
                if abs(dr) + abs(dc) > 20:
                    continue
                if (r + dr, c + dc) not in distances:
                    continue
                better_by = distances[(r + dr, c + dc)] - distances[(r, c)] - (abs(dr) + abs(dc))
                if better_by >= 100:
                    total += 1

    return total


def main():
    values = read_in()
    # print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
