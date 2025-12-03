from typing import List


def read_file(filename: str) -> str:
    with open(filename) as file:
        return file.read()


def parse_banks(data: str) -> List[List[int]]:
    lines = data.split("\n")
    return [[int(char) for char in line] for line in lines]


def max_joltage(bank: List[int]) -> int:
    first_digit_index = len(bank) - 2  # second to last digit

    # search for a higher or equal and earlier digit
    for i in range(first_digit_index - 1, -1, -1):
        if bank[i] >= bank[first_digit_index]:
            first_digit_index = i

    first_digit = bank[first_digit_index]
    second_digit = max(bank[first_digit_index + 1 :])
    return first_digit * 10 + second_digit


def part_one(data: str):
    # convert data into banks
    banks = parse_banks(data)
    # map each bank to maximum joltage
    jolts = map(max_joltage, banks)
    # sum max joltage
    return sum(jolts)


def max_joltage_flexible(bank: List[int], number_batteries: int) -> int:
    remaining = number_batteries
    total = 0

    first_available_index = 0

    while remaining > 0:
        last_available_next_index = len(bank) - remaining
        next_digit_index = last_available_next_index

        # find the earliest instance of the highest remaining number
        for i in range(next_digit_index - 1, first_available_index - 1, -1):
            if bank[i] >= bank[next_digit_index]:
                next_digit_index = i

        total = total * 10 + bank[next_digit_index]
        first_available_index = next_digit_index + 1
        remaining -= 1

    return total


PART_TWO_BATTERIES = 12


def part_two(data: str):
    banks = parse_banks(data)
    jolts = map(lambda bank: max_joltage_flexible(bank, PART_TWO_BATTERIES), banks)
    return sum(jolts)


def solve(filename):
    print(filename)
    data = read_file(filename)
    print("part 1:", part_one(data))
    print("part 2:", part_two(data))


solve("test.input.txt")
solve("input.txt")
