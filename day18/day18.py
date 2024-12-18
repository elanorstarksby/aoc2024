

def read_in():
    with open("input.txt", "r") as input_file:
        lines = [tuple([int(b) for b in a.strip().split(",")]) for a in input_file]
    return lines


def search(blocked, visited, bounds, to_visit):
    while to_visit:
        distance, at = to_visit.pop(0)
        if at == bounds:
            return distance
        for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_at = (at[0] + d[0], at[1] + d[1])
            if next_at in blocked or next_at[0] > bounds[0] or next_at[0] < 0 or next_at[1] > bounds[1] or next_at[1] < 0 or next_at in visited:
                continue
            to_visit.append((distance+1, next_at))
            visited.add(next_at)


def p1(values, bounds, first_amount):
    first_section = values[:first_amount]

    return search(first_section, set(), bounds, [(0,(0,0))])


def p2(values, bounds, first_amount):
    i = first_amount
    while search(set(values[:i]), set(), bounds, [(0,(0,0))]) is not None:
        i+=1
    return ",".join([str(a) for a in values[i-1]])


def main():
    values = read_in()
    if values[0] == (5, 4):
        n = 12
        bounds = (6, 6)
    else:
        n = 1024
        bounds = (70, 70)
    # print(values)
    print(p1(values, bounds, n))

    print(p2(values, bounds, n))


if __name__ == '__main__':
    main()
