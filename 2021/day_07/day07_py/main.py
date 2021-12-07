def parse_input():
    return [
        int(position)
        for position in open("input.txt").readline().strip().split(",")
    ]


def total_fuel_to_position(crabs_positions, target_position):
    return sum(
        abs(position - target_position)
        for position in crabs_positions
    )


def solve_part_1():
    crabs_positions = parse_input()
    min_position = min(crabs_positions)
    max_position = max(crabs_positions)

    min_fuel = None
    for position in range(min_position, max_position + 1):
        fuel = total_fuel_to_position(crabs_positions, position)
        if (min_fuel is None) or (fuel < min_fuel):
            min_fuel = fuel

    print("part 1:", min_fuel)


def real_fuel_to_position(base_position, target_position):
    n = abs(base_position - target_position)
    return n * (n + 1) // 2


def real_total_fuel_to_position(crabs_positions, target_position):
    return sum(
        real_fuel_to_position(position, target_position)
        for position in crabs_positions
    )


def solve_part_2():
    crabs_positions = parse_input()
    min_position = min(crabs_positions)
    max_position = max(crabs_positions)

    min_fuel = None
    for position in range(min_position, max_position + 1):
        fuel = real_total_fuel_to_position(crabs_positions, position)
        if (min_fuel is None) or (fuel < min_fuel):
            min_fuel = fuel

    print("part 2:", min_fuel)


if __name__ == '__main__':
    solve_part_1()
    solve_part_2()
