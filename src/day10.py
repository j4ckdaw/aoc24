from util import read_inputs

coords = tuple[int, int]

search_vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get(input, coords):
    x, y = coords
    return int(input[y][x])


def get_trailheads(input) -> set[coords]:
    trailheads = set()
    for y, row in enumerate(input):
        for x, cell in enumerate(row):
            if cell == "0":
                trailheads.add((x, y))
    return trailheads


def find_peaks(input, start) -> coords:
    x, y = start
    n = get(input, start)
    if n == 9:
        return set([start])

    next = [
        (x + dx, y + dy)
        for dx, dy in search_vectors
        if 0 <= x + dx < len(input[0])
        and 0 <= y + dy < len(input)
        and get(input, (x + dx, y + dy)) == n + 1
    ]

    return set().union(*[find_peaks(input, n) for n in next])


def count_trails(input, start) -> int:
    x, y = start
    n = get(input, start)
    if n == 9:
        return 1

    next = [
        (x + dx, y + dy)
        for dx, dy in search_vectors
        if 0 <= x + dx < len(input[0])
        and 0 <= y + dy < len(input)
        and get(input, (x + dx, y + dy)) == n + 1
    ]

    return sum([count_trails(input, n) for n in next])


def part_a(input):
    trailheads = get_trailheads(input)
    n_peaks = [find_peaks(input, t) for t in trailheads]
    return sum(list(map(len, n_peaks)))


def part_b(input):
    trailheads = get_trailheads(input)
    return sum([count_trails(input, t) for t in trailheads])


for p, x in zip([part_a, part_b], [36, 81]):
    t, r = read_inputs(10)
    assert p(t) == x
    print(p(r))
