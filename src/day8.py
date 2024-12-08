from util import read_inputs
from itertools import combinations

coords = tuple[int, int]


def calculate_antinodes_a(
    antennas: list[coords], max_x: int, max_y: int
) -> set[coords]:
    antinodes = set()
    for pair in combinations(antennas, 2):
        x1, y1 = pair[0]
        x2, y2 = pair[1]

        dx = x2 - x1
        dy = y2 - y1

        ax1 = x2 + dx
        ay1 = y2 + dy
        ax2 = x1 - dx
        ay2 = y1 - dy

        if 0 <= ax1 <= max_x and 0 <= ay1 <= max_y:
            antinodes.add((ax1, ay1))

        if 0 <= ax2 <= max_x and 0 <= ay2 <= max_y:
            antinodes.add((ax2, ay2))

    return antinodes


def calculate_antinodes_b(
    antennas: list[coords], max_x: int, max_y: int
) -> set[coords]:
    antinodes = set()
    for pair in combinations(antennas, 2):
        x1, y1 = pair[0]
        x2, y2 = pair[1]

        dx = x2 - x1
        dy = y2 - y1

        n = 0
        while True:
            ax = x2 + n * dx
            ay = y2 + n * dy

            if 0 <= ax <= max_x and 0 <= ay <= max_y:
                antinodes.add((ax, ay))
                n += 1
            else:
                break

        n = 0
        while True:
            ax = x1 - n * dx
            ay = y1 - n * dy

            if 0 <= ax <= max_x and 0 <= ay <= max_y:
                antinodes.add((ax, ay))
                n += 1
            else:
                break

    return antinodes


def calculate_all_antinodes(input, fn):
    max_x = len(input[0]) - 1
    max_y = len(input) - 1
    chars = (
        [chr(n) for n in range(48, 58)]
        + [chr(n) for n in range(65, 91)]
        + [chr(n) for n in range(97, 123)]
    )

    antinodes = set()
    for c in chars:
        antennas = []
        for y, l in enumerate(input):
            for x, a in enumerate(l):
                if a == c:
                    antennas.append((x, y))

        if len(antennas) >= 2:
            antinodes.update(fn(antennas, max_x, max_y))

    return antinodes


def part_a(input):
    return len(calculate_all_antinodes(input, calculate_antinodes_a))


def part_b(input):
    return len(calculate_all_antinodes(input, calculate_antinodes_b))


for p, x in zip([part_a, part_b], [14, 34]):
    t, r = read_inputs(8)
    assert p(t) == x
    print(p(r))
