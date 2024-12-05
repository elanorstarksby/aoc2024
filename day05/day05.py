def read_in():
    with open("input.txt", "r") as input_file:
        values = [{}, []]
        line = input_file.readline().strip()
        while not line == "":
            x,y = tuple(int(a) for a in line.split("|"))
            if x not in values[0]:
                values[0][x] = []
            print(values[0][x])
            values[0][x] = values[0][x].append(y)
            line = input_file.readline().strip()
        line = input_file.readline()
        while not line == "":
            values[1].append([int(a) for a in line.split(",")])
            line = input_file.readline().strip()
    return values


def follows_rules(i, update, rules):
    for j in range(i + 1, len(update)):
        for r in rules:
            if update[i] == r[1] and update[j] == r[0]:
                return False, j
    return True, -1


def valid_update(update, rules):
    for i in range(0, len(update)):
        f, j = follows_rules(i, update, rules)
        if not f:
            return False, i, j
    return True, -1, -1


def p1(values):
    updates = values[1]
    rules = values[0]
    p1_total = 0
    invalid_i = []
    for ui, u in enumerate(updates):
        valid, _, _ = valid_update(u, rules)
        if valid:
            p1_total += u[(len(u)) // 2]
        else:
            invalid_i.append(ui)
    return p1_total, invalid_i


def reorder(update, rules):
    valid, i, j = valid_update(update, rules)
    while not valid:
        valid, i, j = valid_update(update, rules)
        update[i], update[j] = update[j], update[i]
    return update


def p2(values, invalid):
    updates = values[1]
    rules = values[0]
    p2_total = 0
    for i in invalid:
        update = reorder(updates[i], rules)
        p2_total += update[(len(update)) // 2]
    return p2_total


def main():
    values = read_in()
    print(values)
    p1_result, invalid = p1(values)
    print(p1_result)
    print(p2(values, invalid))


if __name__ == '__main__':
    main()
