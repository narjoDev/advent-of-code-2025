from typing import List, Tuple


def read_file(filename: str) -> str:
    with open(filename) as file:
        return file.read()


def pair_split(chunk: str) -> Tuple[int, int]:
    parts = chunk.split("-")
    if len(parts) != 2:
        raise ValueError(f"Error splitting chunk. Expected two parts: {parts}")
    return (int(parts[0]), int(parts[1]))


def parse_pairs(data: str) -> List[Tuple[int, int]]:
    pair_chunks = data.split(",")
    return [pair_split(chunk) for chunk in pair_chunks]


def pair_to_range(pair: Tuple[int, int]):
    return range(pair[0], pair[1] + 1)


def is_invalid(id: int) -> bool:
    as_string = str(id)
    middle_index = len(as_string) // 2
    return as_string[0:middle_index] == as_string[middle_index:]


def part_one(data: str):
    pairs = parse_pairs(data)
    ranges = map(pair_to_range, pairs)
    total = 0
    for range in ranges:
        for id in range:
            if is_invalid(id):
                total += id
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
