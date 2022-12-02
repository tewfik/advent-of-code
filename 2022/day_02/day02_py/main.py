ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN = 6


################################################################################
# part 1

def parse_input_part1():
    letters = [row.strip().split(" ") for row in open("input.txt")]
    return [
        (ord(him) - ord("A") + 1, ord(you) - ord("X") + 1)
        for him, you in letters
    ]


def part1():
    total = 0
    for him, you in parse_input_part1():
        total += calculate_score(him, you)

    return total


def calculate_score(him, you):
    if you == him:
        return you + DRAW
    elif (him % SCISSORS) + 1 == you:
        return you + WIN
    else:
        return you + LOSE


################################################################################
# part 2

LETTER2VALUE = {
    "X": LOSE,
    "Y": DRAW,
    "Z": WIN,
}


def part2():
    total = 0
    for him, goal in parse_input_part2():
        total += what_should_i_play(him, goal) + goal

    return total

def parse_input_part2():
    letters = [row.strip().split(" ") for row in open("input.txt")]
    return [
        (ord(him) - ord("A") + 1, LETTER2VALUE[goal])
        for him, goal in letters
    ]

def what_should_i_play(him, goal):
    if goal == WIN:
        return (him % SCISSORS) + 1
    elif goal == LOSE:
        return (him - 1) or SCISSORS
    else:
        return him


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
