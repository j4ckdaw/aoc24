from typing import List


def read_inputs(day: int) -> List[str]:
    with open(f"input/day{day}.txt") as f:
        real_input = f.read().splitlines()

    with open(f"test/day{day}.txt") as f:
        test_input = f.read().splitlines()

    return test_input, real_input
