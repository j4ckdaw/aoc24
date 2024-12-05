from util import read_inputs
import copy


def is_valid(succ_map, update):

    for i, u in enumerate(update):
        if u not in succ_map:
            continue

        if any([n in succ_map[u] for n in update[:i]]):
            return False

    return True


def order_update(succ_map, update):
    ordered = []
    elements = set(update)

    while elements:
        for e in copy.copy(elements):
            if e not in succ_map or any([n in elements for n in succ_map[e]]):
                ordered.append(e)
                elements.remove(e)
                continue

    return ordered[::-1]


def part_a(input):
    rules, updates = input[: input.index("")], input[input.index("") + 1 :]

    succ_map = {}
    for r in rules:
        k, v = r.split("|")
        succ_map[int(k)] = succ_map.get(int(k), []) + [int(v)]

    updates = [[int(n) for n in u.split(",")] for u in updates]

    valid_updates = [u for u in updates if is_valid(succ_map, u)]

    return sum([u[len(u) // 2] for u in valid_updates])


def part_b(input):
    rules, updates = input[: input.index("")], input[input.index("") + 1 :]

    succ_map = {}
    for r in rules:
        k, v = r.split("|")
        succ_map[int(k)] = succ_map.get(int(k), []) + [int(v)]

    updates = [[int(n) for n in u.split(",")] for u in updates]

    invalid_updates = [u for u in updates if not is_valid(succ_map, u)]

    ordered_updates = [order_update(succ_map, u) for u in invalid_updates]

    return sum([u[len(u) // 2] for u in ordered_updates])


for p, x in zip([part_a, part_b], [143, 123]):
    t, r = read_inputs(5)
    assert p(t) == x
    print(p(r))
