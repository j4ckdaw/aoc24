from util import read_inputs
import re


def part_a(input):
    pattern = "mul\((\d*),(\d*)\)"
    matches = re.findall(pattern, input)
    return sum([int(a) * int(b) for a, b in matches])


def part_b(input):
    pattern = "mul\((\d*),(\d*)\)|(do)\(\)|(don't)\(\)"
    matches = re.findall(pattern, input)

    do = True
    sum = 0
    for m in matches:
        if m[2]:
            do = True
        elif m[3]:
            do = False
        elif do:
            sum += int(m[0]) * int(m[1])

    return sum


for p, l, x in zip([part_a, part_b], [0, 1], [161, 48]):
    t, r = read_inputs(3)
    assert p(t[l]) == x
    input = "".join(r)
    print(p(input))
