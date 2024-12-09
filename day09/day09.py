from datetime import datetime


def read_in():
    with open("input.txt", "r") as input_file:
        lines = input_file.readline()
    return lines


def read_compact_blocks(values):
    blocks = []
    for vi, v in enumerate(values):
        if vi % 2 == 0:
            blocks.append((vi // 2, int(v)))
        else:
            blocks.append((".", int(v)))
    return blocks


def done_compact(blocks):
    seen_dot = False
    for (b, _) in blocks:
        if seen_dot and b != ".":
            return False
        if b == ".":
            seen_dot = True
    return True


def find_last_block_i_compact(blocks):
    i = len(blocks) - 1
    while i >= 0 and (blocks[i][0] == "." or blocks[i][1] == 0):
        i -= 1
    return i


def find_first_dot_i_compact(blocks):
    i = 0
    while i < len(blocks) and (blocks[i][0] != "." or blocks[i][1] == 0):
        i += 1
    return i


def move_compact(blocks):
    lbi = find_last_block_i_compact(blocks)
    fdi = find_first_dot_i_compact(blocks)
    fd = blocks[fdi]
    lb = blocks[lbi]
    if lbi < fdi:
        return
    move_c = min(fd[1], lb[1])
    blocks[lbi] = (lb[0], lb[1] - move_c)
    blocks[fdi] = (fd[0], fd[1] - move_c)
    blocks.insert(fdi, (lb[0], move_c))
    for i in range(len(blocks)-1, -1, -1):
        if blocks[i][1] == 0:
            blocks.pop(i)


def checksum(blocks):
    index = 0
    total = 0
    for (block_id, count) in blocks:
        if block_id != ".":
            for i in range(count):
                total += block_id * index
                index += 1
        else:
            index += count
    return total

def p1(values):
    blocks = read_compact_blocks(values)
    # print(blocks)
    while not done_compact(blocks):
        move_compact(blocks)
    return checksum(blocks)


def p2(values):
    p2_total = 0

    return p2_total


def main():
    values = read_in()
    # print(values)
    t = datetime.now()
    print(p1(values))
    print(datetime.now() - t)
    t = datetime.now()
    print(p2(values))
    print(datetime.now() - t)


if __name__ == '__main__':
    main()
