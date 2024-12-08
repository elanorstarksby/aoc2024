def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def map_nodes(values):
    nodes = {}
    for ri, r in enumerate(values):
        for ci, c in enumerate(r):
            if c != ".":
                if c not in nodes:
                    nodes[c] = []
                nodes[c].append((ri, ci))
    return nodes


def find_antinodes(l1, l2):
    an1 = (l1[0] + (l1[0] - l2[0]), l1[1] + (l1[1] - l2[1]))
    an2 = (l2[0] + (l2[0] - l1[0]), l2[1] + (l2[1] - l1[1]))
    return an1, an2


def p1(values):
    nodes = map_nodes(values)
    rc = len(values)
    cc = len(values[0])
    antinodes = set()
    for n, locs in nodes.items():
        for i, loc1 in enumerate(locs):
            for j, loc2 in enumerate(locs[i + 1:]):
                ra = find_antinodes(loc1, loc2)
                for a in ra:
                    if 0 <= a[0] < rc and 0 <= a[1] < cc:
                        antinodes.add(a)

    return len(antinodes)


def find_antinodes_2(l1, l2, rc, cc):
    antinodes = []
    dy = l2[0] - l1[0]
    dx = l2[1] - l1[1]
    for y in range(0, rc):
        for x in range(0, cc):
            if y - l1[0] == (dy / dx) * (x - l1[1]):
                antinodes.append((y, x))
    return antinodes


def p2(values):
    nodes = map_nodes(values)
    rc = len(values)
    cc = len(values[0])
    antinodes = set()
    for n, locs in nodes.items():
        for i, loc1 in enumerate(locs):
            for j, loc2 in enumerate(locs[i + 1:]):
                ra = find_antinodes_2(loc1, loc2, rc, cc)
                for a in ra:
                    antinodes.add(a)

    return len(antinodes)


def main():
    values = read_in()
    print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
