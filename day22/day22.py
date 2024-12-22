def read_in():
    with open("input.txt", "r") as input_file:
        lines = [int(a) for a in input_file.read().split('\n')]
    return lines


def calculate_next(current):
    current = ((current * 64) ^ current) % 16777216
    current = ((current // 32) ^ current) % 16777216
    current = ((current * 2048) ^ current) % 16777216
    return current


COUNT = 2000


def p1(values):
    total = 0
    for buyer_number in values:
        for i in range(COUNT):
            buyer_number = calculate_next(buyer_number)
        total += buyer_number
    return total


def p2(values):
    all_ones = []
    all_deltas = []
    sequences = {}
    for buyer_number in values:
        deltas = []
        ones = []
        previous = int(str(buyer_number)[-1])
        for i in range(COUNT):
            buyer_number = calculate_next(buyer_number)
            one = int(str(buyer_number)[-1])
            ones.append(one)
            delta = one - previous
            deltas.append(delta)
            previous = one
        all_ones.append(ones)
        all_deltas.append(deltas)
        this_buyers_sequences = set()
        for i in range(COUNT - 3):
            seq = (deltas[i], deltas[i + 1], deltas[i + 2], deltas[i + 3])
            if seq in this_buyers_sequences:
                continue
            this_buyers_sequences.add(seq)
            if seq not in sequences:
                sequences[seq] = 0
            sequences[seq] += ones[i + 3]
    most = max(sequences.values())
    return most


def main():
    values = read_in()
    print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
