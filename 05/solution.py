from functools import reduce
from typing import List, Tuple


def read_file(filename: str) -> str:
    with open(filename) as file:
        return file.read()


def split_ranges_available(data: str) -> Tuple[str, str]:
    [ranges, available] = data.split("\n\n")
    return (ranges, available)


def parse_ranges(range_data: str) -> List[range]:
    pairs = [[int(x) for x in line.split("-")] for line in range_data.split("\n")]
    return [range(pair[0], pair[1] + 1) for pair in pairs]


def condense_ranges(ranges: List[range]) -> List[range]:
    sorted_by_start = sorted(ranges, key=lambda r: r.start)

    condensed = [sorted_by_start[0]]
    for this_range in sorted_by_start[1:]:
        top_range = condensed[-1]
        # if overlaps with top, combine and replace
        if this_range.start <= top_range.stop:
            new_stop = max(this_range.stop, top_range.stop)
            condensed.pop()
            condensed.append(range(top_range.start, new_stop))
        else:
            condensed.append(this_range)

    return condensed


def full_parse_ranges_available(data: str) -> Tuple[List[range], List[int]]:
    [range_data, available_data] = split_ranges_available(data)
    ranges = parse_ranges(range_data)
    condensed = condense_ranges(ranges)
    available = [int(line.strip()) for line in available_data.split("\n")]
    return (condensed, available)


def in_any_range(number: int, ranges: List[range]) -> bool:
    for range in ranges:
        if number in range:
            return True
    return False


def part_one(data: str):
    [ranges, available] = full_parse_ranges_available(data)
    fresh = [id for id in available if in_any_range(id, ranges)]
    return len(fresh)


def part_two(data: str):
    [ranges, _available] = full_parse_ranges_available(data)
    range_lengths = [len(r) for r in ranges]
    return reduce(lambda a, b: a + b, range_lengths)


def solve(filename):
    print(filename)
    data = read_file(filename)
    print("part 1:", part_one(data))
    print("part 2:", part_two(data))


solve("test.input.txt")
solve("input.txt")
