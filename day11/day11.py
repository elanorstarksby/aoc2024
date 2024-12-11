def read_in():
    with open("input.txt", "r") as input_file:
        lines = [int(a) for a in input_file.readline().strip().split(' ')]
    return lines


def add_to_v(v, add, map_values):
    if v not in map_values:
        map_values[v] = 0
    map_values[v] = map_values[v] + add

def stones(values, times):
    map_values = {}
    for v in values:
        add_to_v(v, 1, map_values)
    # print(map_values)
    for i in range(times):
        new_map_values = {}
        for v, count in map_values.items():
            digit_count = len(str(v))
            if v == 0:
                add_to_v(1, count, new_map_values)
            elif digit_count % 2 == 0:
                add_to_v(int(str(v)[:digit_count // 2]), count, new_map_values)
                add_to_v(int(str(v)[digit_count // 2:]), count, new_map_values)
            else:
                add_to_v(v * 2024, count, new_map_values)
        map_values = new_map_values
    return sum(map_values.values())


def p1(values):
    return stones(values, 25)

def p2(values):
    return stones(values, 75)


def main():
    values = read_in()
    print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()