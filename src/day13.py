from util import read_inputs
import re, math

# button a, button b, prize
machine = tuple[tuple[int, int], tuple[int, int], tuple[int, int]]

r_button = "Button \w: X\+(\d+), Y\+(\d+)"
r_prize = "Prize: X=(\d+), Y=(\d+)"


def parse_machine(input) -> machine:
    button_a = tuple(map(int, re.match(r_button, input[0]).groups()))
    button_b = tuple(map(int, re.match(r_button, input[1]).groups()))
    prize = tuple(map(int, re.match(r_prize, input[2]).groups()))
    return (button_a, button_b, prize)


def parse_machines(input) -> list[machine]:
    machines = [input[i : i + 3] for i in range(0, len(input), 4)]
    return [parse_machine(m) for m in machines]


def solve_machine(machine) -> int:
    button_a, button_b, prize = machine
    ax, ay = button_a
    bx, by = button_b
    px, py = prize

    b = ((py * ax) - (px * ay)) / ((by * ax) - (bx * ay))

    if b < 0 or not b.is_integer():
        return 0

    a = (px - (bx * b)) / ax

    if a < 0 or not a.is_integer():
        return 0

    return (3 * a) + b


def part_a(input):
    machines = parse_machines(input)
    return sum([solve_machine(m) for m in machines])


def part_b(input):
    machines = parse_machines(input)
    machines = [
        (m[0], m[1], (10000000000000 + m[2][0], 10000000000000 + m[2][1]))
        for m in machines
    ]
    return sum([solve_machine(m) for m in machines])


for p, x in zip([part_a, part_b], [480, 875318608908]):
    t, r = read_inputs(13)
    assert p(t) == x
    print(p(r))
