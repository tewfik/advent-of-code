def parse_input():
    fishes = [int(fish) for fish in open("input.txt").readline().strip().split(",")]
    fishes_by_timer = [0] * 9
    for fish in fishes:
        fishes_by_timer[fish] += 1

    return fishes_by_timer


def next_generation(fishes_by_timer):
    new_generation = [0] * 9

    newborns = fishes_by_timer[0]
    new_generation[6] = fishes_by_timer[0]

    for idx in range(1, len(fishes_by_timer)):
        new_generation[idx - 1] += fishes_by_timer[idx]

    new_generation[8] = newborns

    return new_generation


def n_generations(days):
    fishes = parse_input()
    for _ in range(days):
        fishes = next_generation(fishes)

    return sum(fishes)


if __name__ == '__main__':
    print("part 1:", n_generations(80))
    print("part 2:", n_generations(256))
