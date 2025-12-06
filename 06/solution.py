from functools import reduce
import re
from typing import List, TypeVar


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


def parse_grid(data: str) -> List[List[str]]:
    return [[char for char in line] for line in data.split("\n")]


T = TypeVar("T")


def transpose(matrix: List[List[T]]) -> List[List[T]]:
    number_rows = len(matrix)
    number_columns = len(matrix[0])

    transposed_matrix = []

    for column in range(0, number_columns):
        new_row = []
        for row in range(0, number_rows):
            new_row.append(matrix[row][column])
        transposed_matrix.append(new_row)

    return transposed_matrix


def separate_problems(grid: List[List[str]]) -> List[List[List[str]]]:
    def is_row_empty(row: List[str]) -> bool:
        for char in row:
            if char != " ":
                return False
        return True

    # split on empty rows
    problems = []

    next_start_row = 0
    for row_index in range(1, len(grid)):
        if is_row_empty(grid[row_index]):
            problems.append(grid[next_start_row:row_index])
            next_start_row = row_index + 1
    if next_start_row < len(grid):
        problems.append(grid[next_start_row:])

    return problems


def solve_problem(problem: List[List[str]]) -> int:
    operation = problem[0].pop()
    is_add = operation == "+"
    numbers = [int("".join(row).strip()) for row in problem]
    reducer = ADD_REDUCER if is_add else MULTI_REDUCER
    result = reduce(reducer, numbers)
    return result


def part_two(data: str):
    grid = transpose(parse_grid(data))

    problems = separate_problems(grid)
    results = map(solve_problem, problems)
    return reduce(ADD_REDUCER, results)


def solve(filename):
    print(filename)
    data = read_file(filename)
    print("part 1:", part_one(data))
    print("part 2:", part_two(data))


solve("test.input.txt")
solve("input.txt")
