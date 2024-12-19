import functools


def read_in():
    with open("input.txt", "r") as input_file:
        lines = [a for a in input_file.read().split("\n\n")]
        lines[0] = lines[0].split(", ")
        lines[1] = lines[1].split("\n")
    return lines


def p1(values):
    towels = values[0]

    @functools.cache
    def search(design):
        if not design:
            return True
        for towel in towels:
            if design.startswith(towel):
                if search(design[len(towel):]):
                    return True
        return False

    count = 0
    for design in values[1]:
        count += 1 if search(design) else 0
    return count


def p2(values):
    towels = values[0]

    @functools.cache
    def search(design):
        if not design:
            return 1
        total = 0
        for towel in towels:
            if design.startswith(towel):
                total += search(design[len(towel):])
        return total

    count = 0
    for design in values[1]:
        count += search(design)
    return count


def main():
    values = read_in()
    print(values)
    print(p1(values))

    print(p2(values))


if __name__ == '__main__':
    main()
