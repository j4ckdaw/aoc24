from util import read_inputs


def permutation_a(n: int):
    if n == 1:
        return ["+", "*"]
    else:
        ops = permutation_a(n - 1)
        return [o + "+" for o in ops] + [o + "*" for o in ops]


def permutation_b(n: int):
    if n == 1:
        return ["+", "*", "|"]
    else:
        ops = permutation_b(n - 1)
        return [o + "+" for o in ops] + [o + "*" for o in ops] + [o + "|" for o in ops]


def check(numbers, operators, target):
    acc = numbers.pop(0)
    while operators:
        op = operators.pop(0)
        n = numbers.pop(0)
        if op == "+":
            acc += n
        elif op == "*":
            acc *= n
        elif op == "|":
            acc = int(str(acc) + str(n))

    return acc == target


def part_a(input):

    sum = 0
    for l in input:
        target = int(l.split(":")[0])
        numbers = list(map(int, l.split(" ")[1:]))

        for ops in permutation_a(len(numbers) - 1):
            if check(numbers.copy(), list(ops), target):
                sum += target
                break

    return sum


def part_b(input):
    sum = 0
    for l in input:
        target = int(l.split(":")[0])
        numbers = list(map(int, l.split(" ")[1:]))

        for ops in permutation_b(len(numbers) - 1):
            if check(numbers.copy(), list(ops), target):
                sum += target
                break

    return sum


for p, x in zip([part_a, part_b], [3749, 11387]):
    t, r = read_inputs(7)
    assert p(t) == x
    print(p(r))
