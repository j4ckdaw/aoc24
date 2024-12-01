from util import read_inputs


def part_a(input):
    pairs = [[int(n) for n in line.split()] for line in input]
    list_a, list_b = zip(*pairs)

    list_a = sorted(list_a)
    list_b = sorted(list_b)

    return sum([abs(a - b) for a, b in zip(list_a, list_b)])


def part_b(input):
    pairs = [[int(n) for n in line.split()] for line in input]
    list_a, list_b = zip(*pairs)

    list_a = sorted(list_a)
    list_b = sorted(list_b)

    score = 0
    for a in list_a:
        score += a * list_b.count(a)

    return score


for p, x in zip([part_a, part_b], [11, 31]):
    t, r = read_inputs(1)
    assert p(t) == x
    print(p(r))
