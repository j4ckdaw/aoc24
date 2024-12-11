from util import read_inputs

memo = {}


def blink_stone(stone):
    if stone == 0:
        return [1]

    if len(str(stone)) % 2 == 0:
        i = len(str(stone)) // 2
        return [int(str(stone)[:i]), int(str(stone)[i:])]

    return [stone * 2024]


def process_stone(stone, n):
    if n == 0:
        return 1

    if (stone, n) in memo:
        return memo[(stone, n)]

    res = sum([process_stone(s, n - 1) for s in blink_stone(stone)])

    memo[(stone, n)] = res

    return res


def part_a(input):
    stones = [int(n) for n in input[0].split()]
    return sum([process_stone(s, 25) for s in stones])


def part_b(input):
    stones = [int(n) for n in input[0].split()]
    return sum([process_stone(s, 75) for s in stones])


for p, x in zip([part_a, part_b], [55312, 65601038650482]):
    t, r = read_inputs(11)
    assert p(t) == x
    print(p(r))
