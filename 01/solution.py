from typing import List, Tuple


def read_input(filename: str) -> List[str]:
    with open(filename) as file:
        return file.read().split("\n")


def parse_rotation(line: str) -> Tuple[str, int]:
    direction = line[0]
    number = int(line[1:])
    return (direction, number)


EXCLUSIVE_MAXIMUM = 100


def position_after_rotation(position: int, rotation: Tuple[str, int]) -> int:
    direction, number = rotation
    position_delta = number if direction == "R" else -number
    return (position + position_delta) % EXCLUSIVE_MAXIMUM


def solve_part_one(filename: str) -> int:
    lines = read_input(filename)
    rotations = [parse_rotation(line) for line in lines]
    position = 50
    zeroes = 0
    for rotation in rotations:
        position = position_after_rotation(position, rotation)
        if position == 0:
            zeroes += 1

    return zeroes


def position_and_zero_passes_after_rotation(
    position: int, rotation: Tuple[str, int]
) -> Tuple[int, int]:
    direction, number = rotation
    position_delta = number if direction == "R" else -number
    new_position_not_normalized = position + position_delta
    new_position_normalized = new_position_not_normalized % EXCLUSIVE_MAXIMUM
    zero_passes = abs(new_position_not_normalized // EXCLUSIVE_MAXIMUM)
    return (new_position_normalized, zero_passes)


def solve_part_two(filename: str) -> int:
    lines = read_input(filename)
    rotations = [parse_rotation(line) for line in lines]
    position = 50
    zeroes = 0
    for rotation in rotations:
        position, zero_passes = position_and_zero_passes_after_rotation(
            position, rotation
        )
        zeroes += zero_passes

    return zeroes


def solve(filename):
    print(filename)
    print("part 1:", solve_part_one(filename))
    print("part 2:", solve_part_two(filename))


solve("test.input.txt")
solve("input.txt")
