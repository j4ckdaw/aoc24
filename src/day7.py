from util import read_inputs
import time


def check_a(numbers, target):
    if len(numbers) == 1:
        return numbers[0] == target

    nums = numbers.copy()
    n = nums.pop()
    if n > target:
        return False

    res = check_a(nums, target - n) or (
        check_a(nums, target // n) if target % n == 0 else False
    )

    return res


def check_b(numbers, target):
    if len(numbers) == 1:
        return numbers[0] == target

    nums = numbers.copy()
    n = nums.pop()
    if n > target:
        return False

    res = (
        check_b(nums, target - n)
        or (check_b(nums, target // n) if target % n == 0 else False)
        or (
            check_b(nums, int(str(target).removesuffix(str(n))))
            if str(target).endswith(str(n)) and len(str(target)) > len(str(n))
            else False
        )
    )

    return res


def part_a(input):
    problems = [(list(map(int, l.split(" ")[1:])), int(l.split(":")[0])) for l in input]
    return sum([t for p, t in problems if check_a(p, t)])


def part_b(input):
    problems = [(list(map(int, l.split(" ")[1:])), int(l.split(":")[0])) for l in input]
    return sum([t for p, t in problems if check_b(p, t)])


print("\nsolutions: ")
for p, x in zip([part_a, part_b], [3749, 11387]):
    t, r = read_inputs(7)
    assert p(t) == x
    print(" -", p(r))


t, r = read_inputs(7)
times = []
for i in range(500):
    start = time.time()
    part_b(r)
    times.append(time.time() - start)

print(f"\navg time: {sum(times) / len(times) * 1000:.2f}ms")
