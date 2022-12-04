def main():
    print(part1())
    print(part2())


def part1():
    count = 0

    for pair1, pair2 in parse_input():
        if (
                (pair1[0] <= pair2[0]) and (pair1[1] >= pair2[1])
                or (pair2[0] <= pair1[0]) and (pair2[1] >= pair1[1])
        ):
            count += 1

    return count


def part2():
    count = 0

    for pair1, pair2 in parse_input():
        if not (pair1[0] > pair2[1] or pair2[0] > pair1[1]):
            count += 1

    return count


def parse_input():
    for row in open("input.txt"):
        pair1, pair2 = row.strip().split(",")
        a1, a2 = pair1.split("-")
        b1, b2 = pair2.split("-")
        yield (
            (int(a1), int(a2)),
            (int(b1), int(b2)),
        )


if __name__ == '__main__':
    main()
