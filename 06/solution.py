from functools import reduce
import re
from typing import List


def read_file(filename: str) -> str:
    with open(filename) as file:
        return file.read()


def parse_input(data: str) -> List[List[str]]:
    return [re.split(r"\s+", line.strip()) for line in data.split("\n")]


ADD_REDUCER = lambda a, b: a + b
MULTI_REDUCER = lambda a, b: a * b


def part_one(data: str):
    input = parse_input(data)
    number_rows = len(input)
    number_columns = len(input[0])

    results = []
    for col in range(0, number_columns):
        operation_char = input[-1][col]
        is_add = operation_char == "+"
        numbers = [int(input[row][col]) for row in range(0, number_rows - 1)]
        reducer = ADD_REDUCER if is_add else MULTI_REDUCER
        result = reduce(reducer, numbers)
        results.append(result)

    return reduce(ADD_REDUCER, results)


def part_two(data: str):
    pass


def solve(filename):
    print(filename)
    data = read_file(filename)
    print("part 1:", part_one(data))
    print("part 2:", part_two(data))


solve("test.input.txt")
solve("input.txt")
