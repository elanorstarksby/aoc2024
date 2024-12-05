def read_in():
    with open("input.txt", "r") as input_file:
        lines = [[a for a in line.strip()] for line in input_file]
    return lines


def search_xmas(grid, current_letter, ri, ci, dr):
    next_letter = {"X": "M", "M": "A", "A": "S", "S": 0}
    if current_letter not in next_letter:
        return False
    expect = next_letter[current_letter]
    if expect == 0:
        return True
    else:
        if ri + dr[0] >= len(grid) or ri + dr[0] < 0 or ci + dr[1] >= len(grid[0]) or ci + dr[1] < 0:
            return False
        if grid[ri + dr[0]][ci + dr[1]] == expect:
            return search_xmas(grid, expect, ri + dr[0], ci + dr[1], dr)
        else:
            return False


def p1(grid):
    p1_total = 0
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
    for row_i, row in enumerate(grid):
        for col_i, letter in enumerate(row):
            if letter == "X":
                for dr in dirs:
                    xmas = search_xmas(grid, "X", row_i, col_i, dr)
                    if xmas:
                        p1_total += 1
    return p1_total


def find(grid, letter, ri, ci, dr):
    if dr == "up":
        if grid[ri - 1][ci - 1] == letter and grid[ri - 1][ci + 1] == letter:
            return True
    if dr == "down":
        if grid[ri + 1][ci - 1] == letter and grid[ri + 1][ci + 1] == letter:
            return True
    if dr == "left":
        if grid[ri - 1][ci - 1] == letter and grid[ri + 1][ci - 1] == letter:
            return True
    if dr == "right":
        if grid[ri - 1][ci + 1] == letter and grid[ri + 1][ci + 1] == letter:
            return True
    return False


def search_cross(grid, ri, ci):
    if ri==0 or ri==len(grid)-1 or ci ==0 or ci==len(grid[0])-1:
        return False
    return (find(grid, "M", ri, ci, "up") and find(grid, "S", ri, ci, "down")) or (
                find(grid, "M", ri, ci, "down") and find(grid, "S", ri, ci, "up")) or (
                find(grid, "M", ri, ci, "left") and find(grid, "S", ri, ci, "right")) or (
                find(grid, "M", ri, ci, "right") and find(grid, "S", ri, ci, "left"))


def p2(grid):
    p2_total = 0
    for row_i, row in enumerate(grid):
        for col_i, letter in enumerate(row):
            if letter == "A":
                if search_cross(grid, row_i, col_i):
                    p2_total += 1
    return p2_total


def main():
    values = read_in()
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
