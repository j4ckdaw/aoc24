from util import read_inputs
from itertools import takewhile


def parse(disk_map):
    disk = []
    id = 0
    empty = False
    for c in disk_map:
        if empty:
            disk.extend([-1] * int(c))
            empty = False
        else:
            disk.extend([int(id)] * int(c))
            empty = True
            id += 1

    return disk


def frag(disk):
    fragged = []
    j = len(disk) - 1
    for i in range(0, len(disk)):
        if disk[i] != -1:
            fragged.append(disk[i])
        else:
            while disk[j] == -1:
                j -= 1
            fragged.append(disk[j])
            j -= 1

        if j <= i:
            break

    return fragged


def compact(disk):
    compacted = disk.copy()
    id = int(disk[-1])

    empty_block_starts = [
        i for i in range(0, len(disk)) if disk[i] == -1 and disk[i - 1] != -1
    ]
    empty_blocks = {
        i: len(list(takewhile(lambda x: x == -1, disk[i:]))) for i in empty_block_starts
    }

    while id > 0:
        start = disk.index(int(id))
        needed = len(list(takewhile(lambda x: x == int(id), disk[start:])))

        for e in empty_block_starts:
            if e > start:
                break

            if empty_blocks[e] >= needed:
                for j in range(0, needed):
                    compacted[e + j] = int(id)
                    compacted[start + j] = -1

                if empty_blocks[e] > needed:
                    empty_blocks[e + needed] = empty_blocks[e] - needed
                    empty_block_starts = [
                        i if i != e else (e + needed) for i in empty_block_starts
                    ]
                else:
                    empty_block_starts.remove(e)

                empty_blocks.pop(e)

                break

        id -= 1

    return compacted


def checksum(disk):
    return sum([int(i) * int(c) if disk[i] != -1 else 0 for i, c in enumerate(disk)])


def part_a(input):
    disk = parse(input[0])
    disk = frag(disk)
    return checksum(disk)


def part_b(input):
    disk = parse(input[0])
    disk = compact(disk)
    return checksum(disk)


for p, x in zip([part_a, part_b], [1928, 2858]):
    t, r = read_inputs(9)
    assert p(t) == x
    print(p(r))
