DIGITS_MAPPING = (
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
)


def main():
    print(solve_part1())
    print(solve_part2())


def solve_part1():
    result = 0
    for line in parse_input():
        first = next(c for c in line if c.isdigit())
        last = next(c for c in line[::-1] if c.isdigit())
        result += int(first + last)

    return result


def solve_part2():
    result = 0
    for line in parse_input():
        adjusted_line = digitalize(line)
        result += int(adjusted_line[0] + adjusted_line[-1])

    return result


def parse_input():
    return (line.strip() for line in open("input.txt"))


def digitalize(line):
    result = []

    for idx in range(len(line)):
        if line[idx].isdigit():
            result.append(line[idx])
        else:
            for spelled, number in DIGITS_MAPPING:
                if line[idx:].startswith(spelled):
                    result.append(number)
                    break

    return result


if __name__ == '__main__':
    main()
