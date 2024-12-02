def read_in():
    with open("input.txt", "r") as input_file:
        lines = [[int(a) for a in line.strip().split(" ")] for line in input_file]
    return lines


def is_safe(report):
    if report[0] > report[1]:
        for i in range(0, len(report)-1):
            if not 1 <= report[i] - report[i+1] <= 3:
                return False
    else:
        for i in range(0, len(report)-1):
            if not 1 <= report[i+1] - report[i] <= 3:
                return False
    return True

def p1(values):
    p1_total = 0
    for report in values:
        if is_safe(report):
            p1_total += 1
    return p1_total

def p2(values):
    p1_total = 0
    for report in values:
        if is_safe(report):
            p1_total += 1
        else:
            for i in range(0, len(report)):
                copy_report = report.copy()
                copy_report.pop(i)
                if is_safe(copy_report):
                    p1_total += 1
                    break

    return p1_total


def main():
    values = read_in()
    print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
