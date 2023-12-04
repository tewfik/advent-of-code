from collections import defaultdict
import functools
import operator


def main():
    print("part 1:", solve_part1())
    print("part 2:", solve_part2())


def solve_part1():
    games = parse_input()
    target = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    return sum(game_id + 1 for game_id, game in enumerate(games) if is_possible(game, target))


def solve_part2():
    games = parse_input()

    return sum(functools.reduce(operator.mul, get_max_count(game).values()) for game in games)


def parse_input():
    raw_games = [line.strip().split(":")[1] for line in open("input.txt")]
    games = []
    for game in raw_games:
        raw_game_turns = game.split(";")

        game_turns = []
        for game_turn in raw_game_turns:
            raw_reaches = [reach.strip() for reach in game_turn.split(",")]
            reaches = {}
            for reach in raw_reaches:
                count, color = reach.split(" ")
                reaches[color] = int(count)

            game_turns.append(reaches)

        games.append(game_turns)

    return games


def is_possible(game: list[dict], target: dict[str, int]) -> bool:
    max_count = get_max_count(game)

    for color, count in max_count.items():
        try:
            if target[color] < count:
                return False
        except KeyError:
            return False

    return True


def get_max_count(game):
    max_count = defaultdict(lambda: 0)
    for turn in game:
        for color, count in turn.items():
            max_count[color] = max(max_count[color], count)

    return max_count


if __name__ == '__main__':
    main()
