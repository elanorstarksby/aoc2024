import functools


def read_in():
    with open("input.txt", "r") as input_file:
        lines = input_file.read().split('\n')
    return lines


number_pad = [["7", "8", "9"],
              ["4", "5", "6"],
              ["1", "2", "3"],
              ["X", "0", "A"]]

direction_pad = [["X", "^", "A"],
                 ["<", "v", ">"]]


@functools.cache
def num_codes(d1, d2):
    dr1, dc1 = next(((r, c) for r, row in enumerate(number_pad) for c, val in enumerate(row) if val == d1))
    dr2, dc2 = next(((r, c) for r, row in enumerate(number_pad) for c, val in enumerate(row) if val == d2))

    # print(d1, d2, "", d1, dr1, dc1, "", d2, dr2, dc2)
    n_path = ""
    options = []
    if dr1 == dr2:
        # print("Only l/r")
        if dc1 > dc2:
            n_path += ("<" * (dc1 - dc2))
        else:
            n_path += (">" * (dc2 - dc1))
    elif dc1 == dc2:
        # print("Only up/down")
        if dr1 > dr2:
            n_path += ("^" * (dr1 - dr2))
        else:
            n_path += ("v" * (dr2 - dr1))
    elif dc1 == 0 and dr2 == 3:
        # print("Avoid empty")
        n_path += (">" * (dc2 - dc1))
        n_path += ("v" * (dr2 - dr1))
    elif dr1 == 3 and dc2 == 0:
        # print("Avoid empty")
        n_path += ("^" * (dr1 - dr2))
        n_path += ("<" * (dc1 - dc2))
    else:
        # print("Corner")
        # have to try both options
        parts = []
        if dr1 > dr2:
            parts.append("^" * (dr1 - dr2))
        else:
            parts.append("v" * (dr2 - dr1))
        if dc1 > dc2:
            parts.append("<" * (dc1 - dc2))
        else:
            parts.append(">" * (dc2 - dc1))
        options = ["".join(parts), "".join([parts[1], parts[0]])]
        # print(options)
    if not options:
        options = [n_path]
    return options


@functools.cache
def dir_codes(d1, d2, robot_level):
    dr1, dc1 = next(((r, c) for r, row in enumerate(direction_pad) for c, val in enumerate(row) if val == d1))
    dr2, dc2 = next(((r, c) for r, row in enumerate(direction_pad) for c, val in enumerate(row) if val == d2))

    # print(d1, d2, "", d1, dr1, dc1, "", d2, dr2, dc2)
    n_path = ""
    options = []
    if dr1 == dr2:
        # print("Only l/r")
        if dc1 > dc2:
            n_path += ("<" * (dc1 - dc2))
        else:
            n_path += (">" * (dc2 - dc1))
    elif dc1 == dc2:
        # print("Only up/down")
        if dr1 > dr2:
            n_path += ("^" * (dr1 - dr2))
        else:
            n_path += ("v" * (dr2 - dr1))
    elif dc1 == 0 and dr2 == 0:
        # print("Avoid empty")
        n_path += (">" * (dc2 - dc1))
        n_path += ("^" * (dr1 - dr2))
    elif dr1 == 0 and dc2 == 0:
        # print("Avoid empty")
        n_path += ("v" * (dr2 - dr1))
        n_path += ("<" * (dc1 - dc2))
    else:
        # print("Corner")
        # have to try both options
        parts = []
        if dr1 > dr2:
            parts.append("^" * (dr1 - dr2))
        else:
            parts.append("v" * (dr2 - dr1))
        if dc1 > dc2:
            parts.append("<" * (dc1 - dc2))
        else:
            parts.append(">" * (dc2 - dc1))
        options = ["".join(parts), "".join([parts[1], parts[0]])]
        # print(options)

    if not options:
        options = [n_path]

    # print((27 - robot_level) * "  ", d1, options, d2)
    if robot_level == 0:
        return len(options[0]) + 1
    else:
        min_length = float("inf")
        for path in options:
            if path:
                length = dir_codes("A", path[0], robot_level - 1)
                for i in range(len(path) - 1):
                    length += dir_codes(path[i], path[i + 1], robot_level - 1)
                length += dir_codes(path[-1], "A", robot_level - 1)
                min_length = min(length, min_length)
            else:
                min_length = 1
        return min_length


def type_code(code, robot_count):
    code = "A" + code
    total_length = 0
    for digit in range(len(code) - 1):
        options = num_codes(code[digit], code[digit + 1])
        # print(code[digit], options, code[digit + 1])
        min_length = float("inf")
        for path in options:
            length = dir_codes("A", path[0], robot_count - 1)
            for i in range(len(path) - 1):
                length += dir_codes(path[i], path[i + 1], robot_count - 1)
            length += dir_codes(path[-1], "A", robot_count - 1)
            min_length = min(length, min_length)
        # print(min_length)
        total_length += min_length
    # print("length", total_length)
    return total_length


def p1(codes):
    total = 0
    for code in codes:
        # print("\n" + code)
        total += int(code[:3]) * type_code(code, 2)
    return total


def p2(codes):
    total = 0
    for code in codes:
        # print("\n" + code)
        total += int(code[:3]) * type_code(code, 25)
    return total


def main():
    values = read_in()
    print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
