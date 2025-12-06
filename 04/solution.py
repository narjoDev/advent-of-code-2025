from typing import List


def read_file(filename: str) -> str:
    with open(filename) as file:
        return file.read()


def parse_input(data: str) -> List[str]:
    return data.split("\n")


PAPER_CHARACTER = "@"


def is_inbounds(lines, line_index, col_index):
    return (
        line_index >= 0
        and col_index >= 0
        and line_index < len(lines)
        and col_index < len(lines[0])
    )


def number_adjacent(lines, line_index, col_index):
    offsets = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    total = 0

    for offset in offsets:
        [row, col] = offset
        row += line_index
        col += col_index
        if is_inbounds(lines, row, col) and lines[row][col] == PAPER_CHARACTER:
            total += 1

    return total


ADJACENT_LIMIT = 4


def part_one(data: str):
    lines = parse_input(data)
    total = 0
    for line_index in range(0, len(lines)):
        line = lines[line_index]
        for col_index in range(len(line)):
            char = line[col_index]
            if char == PAPER_CHARACTER:
                if number_adjacent(lines, line_index, col_index) < ADJACENT_LIMIT:
                    total += 1

    return total


def part_two(data: str):
    pass


def solve(filename):
    print(filename)
    data = read_file(filename)
    print("part 1:", part_one(data))
    print("part 2:", part_two(data))


solve("test.input.txt")
solve("input.txt")
