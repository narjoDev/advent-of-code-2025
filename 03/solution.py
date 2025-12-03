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


def part_two(data: str):
    pass


def solve(filename):
    print(filename)
    data = read_file(filename)
    print("part 1:", part_one(data))
    print("part 2:", part_two(data))


solve("test.input.txt")
solve("input.txt")
