from util import read_inputs

coords = tuple[int, int]

vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get(input, coord, max_coords):
    max_x, max_y = max_coords
    x, y = coord
    if x < 0 or x > max_x or y < 0 or y > max_y:
        return None
    return input[y][x]


def get_region(input, start, max_coords) -> set[coords]:
    region = set()
    stack = [start]
    crop = get(input, start, max_coords)
    while stack:
        x, y = stack.pop()
        if (x, y) in region:
            continue

        region.add((x, y))

        for dx, dy in vectors:
            if get(input, (x + dx, y + dy), max_coords) == crop:
                stack.append((x + dx, y + dy))

    return region


def get_regions(input) -> list[list[coords]]:
    max_x = len(input[0]) - 1
    max_y = len(input) - 1

    tiles = set([(x, y) for y in range(max_y + 1) for x in range(max_x + 1)])
    regions = []

    while tiles:
        start = tiles.pop()
        region = get_region(input, start, (max_x, max_y))
        tiles -= region
        regions.append(region)

    return regions


def perimeter(region: set[coords]) -> int:
    perimeter = 0
    for x, y in region:
        for dx, dy in vectors:
            if (x + dx, y + dy) not in region:
                perimeter += 1
    return perimeter


def sides(region: set[coords]) -> int:
    edges = set()
    n = 0
    for x, y in region:
        for dx, dy in vectors:
            if (x + dx, y + dy) not in region:
                if ((x, y), (x + dx, y + dy)) in edges:
                    continue

                # we have a new side
                edges.add(((x, y), (x + dx, y + dy)))
                n += 1

                # we now need to ensure we don't also count any of the other edges that make up the side
                idx = vectors.index((dx, dy))
                for odx, ody in [vectors[(idx - 1) % 4], vectors[(idx + 1) % 4]]:
                    for i in range(1, len(region)):
                        ox, oy = x + i * odx, y + i * ody
                        if (ox, oy) in region and (ox + dx, oy + dy) not in region:
                            edges.add(((ox, oy), (ox + dx, oy + dy)))
                        else:
                            break

    return n


def part_a(input):
    regions = get_regions(input)
    return sum([len(r) * perimeter(r) for r in regions])


def part_b(input):
    regions = get_regions(input)
    return sum([len(r) * sides(r) for r in regions])


for p, x in zip([part_a, part_b], [1930, 1206]):
    t, r = read_inputs(12)
    assert p(t) == x
    print(p(r))
