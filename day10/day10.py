def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def add_to_ends(ends, item):
    if type(ends) == type(set()):
        ends.add(item)
    else:
        ends.append(item)


def next_point(height_map, location, total, ends):
    if height_map[location[0]][location[1]] == '9':
        add_to_ends(ends, location)
        return
    for direction in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        r = location[0] + direction[0]
        c = location[1] + direction[1]
        if 0 <= r < len(height_map) and 0 <= c < len(height_map[0]):
            current = int(height_map[location[0]][location[1]])
            next_h = int(height_map[r][c])
            if next_h == current + 1:
                next_point(height_map, (r, c), total, ends)


def count_trails(values, part):
    total = 0

    for r in range(len(values)):
        for c in range(len(values[r])):
            if values[r][c] == '0':
                ends = set() if part == 1 else []
                next_point(values, (r, c), 0, ends)
                total += len(ends)

    return total


def main():
    values = read_in()
    print(values)
    print(count_trails(values, 1))
    print(count_trails(values, 2))


if __name__ == '__main__':
    main()
