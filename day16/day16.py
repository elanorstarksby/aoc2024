import sys

sys.setrecursionlimit(9999999)


def read_in():
    with open("input.txt", "r") as input_file:
        lines = input_file.read().split('\n')
    return lines


def search(grid, location, facing, score, cutoff, visited):
    if (location, facing) in visited and visited[(location, facing)] < score:
        return cutoff
    visited[(location, facing)] = score
    if score > cutoff:
        return cutoff

    next_l = (location[0] + facing[0], location[1] + facing[1])
    if grid[next_l[0]][next_l[1]] == "E":
        return min(cutoff, score + 1)
    if grid[next_l[0]][next_l[1]] == ".":
        cutoff = min(cutoff, search(grid, next_l, facing, score + 1, cutoff, visited))

    for d in ((facing[1], facing[0]), (-1 * facing[1], -1 * facing[0])):
        next_l = (location[0] + d[0], location[1] + d[1])
        if grid[next_l[0]][next_l[1]] == "E":
            return min(cutoff, score + 1001)
        if grid[next_l[0]][next_l[1]] == ".":
            cutoff = min(cutoff, search(grid, next_l, d, score + 1001, cutoff, visited))
    return cutoff


def p1(values):
    s = (0, 0)
    for ri, r in enumerate(values):
        for ci, c in enumerate(list(r)):
            if c == "S":
                s = (ri, ci)
    return search(values, s, (0, 1), 0, float("inf"), {})


def find_best_paths(grid, location, facing, score, best_path_score, current_path, on_best_path, visited):
    if score > best_path_score:
        return
    if (location, facing) in visited and visited[(location, facing)] < score:
        return
    visited[(location, facing)] = score

    if grid[location[0]][location[1]] == "E" or (
            (location, facing) in on_best_path and score == on_best_path[(location, facing)]):
        on_best_path[(location, facing)] = score
        for l, s in current_path.items():
            on_best_path[l] = s
        return

    if (location, facing) in current_path:
        return
    current_path[(location, facing)] = score

    next_l = (location[0] + facing[0], location[1] + facing[1])
    if grid[next_l[0]][next_l[1]] != "#":
        find_best_paths(grid, next_l, facing, score + 1, best_path_score, current_path.copy(), on_best_path, visited)

    for d in ((facing[1], facing[0]), (-1 * facing[1], -1 * facing[0])):
        next_l = (location[0] + d[0], location[1] + d[1])
        if grid[next_l[0]][next_l[1]] != "#":
            find_best_paths(grid, next_l, d, score + 1001, best_path_score, current_path.copy(), on_best_path, visited)

    # print("")


def p2(values, best_path_score):
    s = (0, 0)
    for ri, r in enumerate(values):
        for ci, c in enumerate(list(r)):
            if c == "S":
                s = (ri, ci)
    on_best_path = {}
    find_best_paths(values, s, (0, 1), 0, best_path_score, {}, on_best_path, {})
    return len(set(l for l, f in on_best_path))


def main():
    values = read_in()
    print(values)
    best_path_score = p1(values)
    print(best_path_score)
    print(p2(values, best_path_score))


if __name__ == '__main__':
    main()
