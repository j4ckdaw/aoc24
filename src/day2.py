from util import read_inputs
from typing import List


def is_safe(report: List[int]) -> bool:
    differences = [report[i + 1] - report[i] for i in range(0, len(report) - 1)]

    return all([d >= 1 and d <= 3 for d in differences]) or all(
        [d < 0 and abs(d) >= 1 and abs(d) <= 3 for d in differences]
    )


def part_a(input):
    reports = [[int(n) for n in line.split()] for line in input]

    return len(list(filter(is_safe, reports)))


def part_b(input):
    reports = [[int(n) for n in line.split()] for line in input]

    def is_safe_with_dampener(r: List[int]) -> bool:
        if is_safe(r):
            return True

        for i in range(0, len(r)):
            if is_safe(r[:i] + r[i + 1 :]):
                return True

        return False

    return len(list(filter(is_safe_with_dampener, reports)))


for p, x in zip([part_a, part_b], [2, 4]):
    t, r = read_inputs(2)
    assert p(t) == x
    print(p(r))
