from typing import List


def read_file(filename: str) -> str:
    with open(filename) as file:
        return file.read()


def parse_input(data: str) -> List[str]:
    return data.split("\n")


def part_one(data: str):
    pass


def part_two(data: str):
    pass


def solve(filename):
    print(filename)
    data = read_file(filename)
    print("part 1:", part_one(data))
    print("part 2:", part_two(data))


solve("test.input.txt")
solve("input.txt")
