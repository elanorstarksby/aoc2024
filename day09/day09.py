from datetime import datetime


def read_in():
    with open("input.txt", "r") as input_file:
        lines = input_file.readline()
    return lines


def read_compact(values):
    blocks = []
    for vi, v in enumerate(values):
        if vi % 2 == 0:
            blocks.append((vi // 2, int(v)))
        else:
            blocks.append((".", int(v)))
    return blocks


def done(blocks):
    seen_dot = False
    for (b, _) in blocks:
        if seen_dot and b != ".":
            return False
        if b == ".":
            seen_dot = True
    return True


def find_last_block_i(blocks):
    i = len(blocks) - 1
    while i >= 0 and (blocks[i][0] == "." or blocks[i][1] == 0):
        i -= 1
    return i


def find_first_dot_i(blocks):
    i = 0
    while i < len(blocks) and (blocks[i][0] != "." or blocks[i][1] == 0):
        i += 1
    return i


def move_block(blocks):
    lbi = find_last_block_i(blocks)
    fdi = find_first_dot_i(blocks)
    fd = blocks[fdi]
    lb = blocks[lbi]
    if lbi < fdi:
        return
    move_c = min(fd[1], lb[1])
    blocks[lbi] = (lb[0], lb[1] - move_c)
    blocks[fdi] = (fd[0], fd[1] - move_c)
    blocks.insert(fdi, (lb[0], move_c))
    for i in range(len(blocks) - 1, -1, -1):
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
    blocks = read_compact(values)
    # print(blocks)
    while not done(blocks):
        move_block(blocks)
    return checksum(blocks)


def find_block_by_id(blocks, block_id):
    for i, block in enumerate(blocks):
        if block[0] == block_id:
            return i
    return -1


def get_block_of_minimum_size(blocks, min_size):
    for i, block in enumerate(blocks):
        if block[0] == "." and block[1] >= min_size:
            return i
    return -1


def merge_dots(blocks):
    changes = True
    while changes:
        changes = False
        for i in range(len(blocks) -1):
            b = blocks[i]

            if b[0] == "." and blocks[i+1][0] == ".":
                    blocks[i] = (blocks[i][0], blocks[i][1] + blocks[i+1][1])
                    blocks.pop(i+1)
                    changes = True
                    break


def move_whole_block(blocks, block_id):
    bi = find_block_by_id(blocks, block_id)
    (bid, count) = blocks[bi]
    di = get_block_of_minimum_size(blocks, count)
    if di == -1 or di > bi:
        return
    block = blocks[bi]
    dot = blocks[di]
    move_c = blocks[bi][1]
    blocks[bi] = (blocks[bi][0], blocks[bi][1] - move_c)
    blocks[di] = (blocks[di][0], blocks[di][1] - move_c)
    blocks.insert(di, (block[0], move_c))
    blocks.insert(bi+1, (dot[0], move_c))
    merge_dots(blocks)
    for i in range(len(blocks) - 1, -1, -1):
        if blocks[i][1] == 0:
            blocks.pop(i)



def p2(values):
    blocks = read_compact(values)
    for i in range(len(blocks) // 2 + 1, -1, -1):
        move_whole_block(blocks, i)

    return checksum(blocks)


def main():
    values = read_in()
    # print(values)
    t = datetime.now()
    # print(p1(values))
    print(datetime.now() - t)
    # t = datetime.now()
    print(p2(values))
    print(datetime.now() - t)


if __name__ == '__main__':
    main()
