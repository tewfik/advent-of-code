from collections import Counter


def main():
    print(part1())
    print(part2())


def priority_from_item(item):
    ord_item = ord(item)

    if ord_item >= ord("a"):
        priority = ord_item - ord("a") + 1
    else:
        priority = ord_item - ord("A") + 1 + 26

    return priority


################################################################################
# part 1

def part1():
    total_priorities = 0
    for compartment1, compartment2 in parse_input_part1():
        common_item = (set(compartment1) & set(compartment2)).pop()
        total_priorities += priority_from_item(common_item)

    return total_priorities

def parse_input_part1():
    for row in open("input.txt"):
        row = row.strip()
        compartment_1 = row[:len(row) // 2]
        compartment_2 = row[len(row) // 2:]
        yield compartment_1, compartment_2


################################################################################
# part 2

def part2():
    rucksacks = parse_input_part2()

    def group_rucksacks(n: int):
        # group rucksacks by chunck of n
        for i in range(0, len(rucksacks), n):
            yield rucksacks[i:i + n]

    common_items = []
    for group in group_rucksacks(3):
        common_items.append(find_common_item(group))

    return sum(priority_from_item(item) for item in common_items)


def parse_input_part2():
    return [row.strip() for row in open("input.txt")]


def find_common_item(group):
    a, b, c = group
    return (set(a) & set(b) & set(c)).pop()


if __name__ == '__main__':
    main()
