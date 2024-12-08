from util import read_inputs

directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]


def obstacle_ahead(input, x, y, direction, max_x, max_y):
    dx, dy = direction
    if x + dx < 0 or x + dx > max_x or y + dy < 0 or y + dy > max_y:
        return False
    return input[y + dy][x + dx] == "#"


def replace_char(grid, x, y, char):
    s = list(grid[y])
    s[x] = char
    grid[y] = "".join(s)


def part_a(input):
    grid = input.copy()
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    row = list(filter(lambda x: "^" in x, grid))[0]
    y = grid.index(row)
    x = row.index("^")
    direction = (0, -1)

    while x >= 0 and x <= max_x and y >= 0 and y <= max_y:
        if obstacle_ahead(grid, x, y, direction, max_x, max_y):
            direction = directions[(directions.index(direction) + 1) % 4]

        replace_char(grid, x, y, "X")

        dx, dy = direction
        x += dx
        y += dy

    return sum([row.count("X") for row in grid])


def part_b(input):
    grid = input.copy()
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    row = list(filter(lambda x: "^" in x, grid))[0]
    y = grid.index(row)
    x = row.index("^")
    direction = (0, -1)

    def detect_loop(grid, x, y, direction, max_x, max_y):
        visited = set()

        while x >= 0 and x <= max_x and y >= 0 and y <= max_y:
            if (x, y, direction) in visited:
                return True

            visited.add((x, y, direction))

            if obstacle_ahead(grid, x, y, direction, max_x, max_y):
                direction = directions[(directions.index(direction) + 1) % 4]
                continue

            dx, dy = direction
            x += dx
            y += dy

        return False

    total = 0
    for i in range(0, len(grid)):
        row = list(grid[i])
        for j in range(0, len(row)):
            modified_grid = grid.copy()
            replace_char(modified_grid, j, i, "#")
            if detect_loop(modified_grid, x, y, direction, max_x, max_y):
                total += 1

    return total


for p, x in zip([part_a, part_b], [41, 6]):
    t, r = read_inputs(6)
    assert p(t) == x
    print(p(r))
