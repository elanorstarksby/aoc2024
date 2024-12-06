def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def find(ch, values):
    for r in range(0, len(values)):
        for c in range(0, len(values[0])):
            if values[r][c] == ch:
                return r, c
    return -1, -1


def leaves(location, values):
    if location[0] < 0 or location[0] >= len(values):
        return True
    if location[1] < 0 or location[1] >= len(values[0]):
        return True
    return False

def blocked(location, values):
    if values[location[0]][location[1]] == "#":
        return True
    return False


def p1(values):
    start = find("^", values)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    di = 0  # direction index
    been_to = []
    current = (start, di)
    while True:
        print(current)
        been_to.append(current)
        candidate_next = (current[0][0] + directions[di][0], current[0][1] + directions[di][1])
        if leaves(candidate_next, values):
            break
        if blocked(candidate_next, values):
            next_place = current[0]
            di = (di + 1) % 4
        else:
            candidate_next = (current[0][0] + directions[di][0], current[0][1] + directions[di][1])
            next_place = candidate_next
        current = (next_place, di)
    locations_set = set([a[0] for a in been_to])
    for l in locations_set:
        values[l[0]] = values[l[0]][:l[1]] + "X" + values[l[0]][l[1] + 1:]
    for v in values:
        print(v)
    return len(locations_set)


def p2(values):
    p1_total = 0

    return p1_total


def main():
    values = read_in()
    print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
