def read_in():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
    return lines


def visit(grid, r, c, region, visited):
    visited.add((r, c))
    region.add((r, c))
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if (not (0 <= r + dr < len(grid))) or (not (0 <= c + dc < len(grid[0]))):
            continue
        if grid[r][c] == grid[r + dr][c + dc] and ((r + dr), (c + dc)) not in visited:
            visit(grid, r + dr, c + dc, region, visited)


def find_regions(grid):
    visited = set()
    regions = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if (r, c) not in visited:
                region = set()
                visit(grid, r, c, region, visited)
                regions.append(region)
    return regions


def calculate_perimeter(region):
    perimeter = 0
    for (r, c) in region:
        to_add = 4
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if (r + dr, c + dc) in region:
                to_add -= 1
        perimeter += to_add
    return perimeter


def calculate_total(region):
    return len(region) * calculate_perimeter(region)


def p1(grid):
    regions = find_regions(grid)
    p1_total = 0
    for region in regions:
        p1_total += calculate_total(region)
    return p1_total


def visit_2(grid, r, c, region, visited, directions):
    visited.add((r, c))
    region.add((r, c))
    for i, (dr, dc) in enumerate(((0, 1), (0, -1), (1, 0), (-1, 0))):
        if (not (0 <= r + dr < len(grid))) or (not (0 <= c + dc < len(grid[0]))):
            directions[i].add((r + dr, c + dc))
            continue
        if grid[r][c] == grid[r + dr][c + dc]:
            if ((r + dr), (c + dc)) not in visited:
                visit_2(grid, r + dr, c + dc, region, visited, directions)
        else:
            directions[i].add((r + dr, c + dc))


def remove_neighbour(d: set, point):
    r, c = point
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        neighbour = (r + dr, c + dc)
        if neighbour in d:
            d.remove(neighbour)
            remove_neighbour(d, neighbour)


def p2(grid):
    visited = set()
    total_cost = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if (r, c) not in visited:
                directions = [set() for _ in range(4)]
                region = set()

                visit_2(grid, r, c, region, visited, directions)

                sides = 0
                for d in directions:
                    while d:
                        point = d.pop()
                        remove_neighbour(d, point)
                        sides += 1

                total_cost += len(region) * sides
    return total_cost


def main():
    values = read_in()
    print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
