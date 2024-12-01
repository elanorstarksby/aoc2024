def read_in():
    with open("input.txt", "r") as input_file:
        lines = [[int(a) for a in line.strip().split("   ")] for line in input_file]
    values = [[],[]]
    for line in lines:
        values[0].append(line[0])
        values[1].append(line[1])
    return values


def p1(values):
    p1_total = 0
    l1 = values[0]
    l2 = values[1]
    l1.sort()
    l2.sort()
    print(l1)
    for i in range(len(l1)):
        p1_total += abs(l1[i]-l2[i])
    return p1_total


def p2(values):
    p2_total = 0
    l1 = values[0]
    l2 = values[1]
    cache = {}
    for l in l1:
        count_l = 0
        if l in cache:
            count_l = cache[l]
        else:
            while l in l2:
                l2.remove(l)
                count_l += 1
        cache[l] = count_l
        p2_total += l * count_l
    return p2_total


def main():
    values = read_in()
    print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()