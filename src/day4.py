from util import read_inputs


a_search_vectors = []
for x in range(-1, 2):
    for y in range(-1, 2):
        if x == 0 and y == 0:
            continue
        a_search_vectors.append((x, y))

string = "XMAS"

b_search_vectors = [
    [(1, 1), (-1, -1)],
    [(1, -1), (-1, 1)],
]


def part_a(input):
    max_y = len(input) - 1
    max_x = len(input[0]) - 1

    def get(coords):
        x, y = coords
        if x < 0 or y < 0 or x > max_x or y > max_y:
            return None
        return input[y][x]

    count = 0
    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            for v in a_search_vectors:
                got_string = ""
                for i in range(0, 4):
                    got = get((x + v[0] * i, y + v[1] * i))
                    if got is None:
                        break
                    got_string += got

                if got_string == string:
                    count += 1

    return count


def part_b(input):
    max_y = len(input) - 1
    max_x = len(input[0]) - 1

    def get(coords):
        x, y = coords
        if x < 0 or y < 0 or x > max_x or y > max_y:
            return None
        return input[y][x]

    count = 0
    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if get((x, y)) != "A":
                continue

            pairs = []
            for v in b_search_vectors:
                pair = []
                for vv in v:
                    pair.append(get((x + vv[0], y + vv[1])))
                pairs.append(pair)

            if all([set(pair) == set(["S", "M"]) for pair in pairs]):
                count += 1

    return count


for p, x in zip([part_a, part_b], [18, 9]):
    t, r = read_inputs(4)
    assert p(t) == x
    print(p(r))
