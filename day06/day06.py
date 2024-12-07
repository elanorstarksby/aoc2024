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
    been_to = set()
    current = (start, di)
    while True:
        # this is probably overcomplicated because I read the problem wrong at first and I can't be
        # bothered to fix it now. Fortunately I read it wrong in a way that was helpful for part 2
        been_to.add(current)
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
    # for l in locations_set:
    #     values[l[0]] = values[l[0]][:l[1]] + "X" + values[l[0]][l[1] + 1:]
    # for v in values:
    #     print(v)
    return locations_set, len(locations_set)


def does_loop(values):
    start = find("^", values)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    di = 0  # direction index
    been_to = set()
    current = (start, di)
    while current not in been_to:
        been_to.add(current)
        candidate_next = (current[0][0] + directions[di][0], current[0][1] + directions[di][1])
        if leaves(candidate_next, values):
            return False
        if blocked(candidate_next, values):
            next_place = current[0]
            di = (di + 1) % 4
        else:
            candidate_next = (current[0][0] + directions[di][0], current[0][1] + directions[di][1])
            next_place = candidate_next
        current = (next_place, di)
    return True


def p2(values, locations):
    p2_total = 0
    for r, c in locations:
        if values[r][c] == ".":
            new_r = values[r][:c] + "#" + values[r][c + 1:]
            new_values = [r for r in values]
            new_values[r] = new_r
            if does_loop(new_values):
                p2_total += 1
    return p2_total


def main():
    values = read_in()
    # print(values)
    locations, p1_count = p1(values.copy())
    print(p1_count)
    print(p2(values, locations))


if __name__ == '__main__':
    main()
