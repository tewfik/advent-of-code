import re

class Board:
    def __init__(self, data):
        self.numbers = data
        self.marks = [[False for _ in range(5)] for _ in range(5)]
        self.old_winner = False

    def mark(self, number):
        for x in range(5):
            for y in range(5):
                if self.numbers[x][y] == number:
                    self.marks[x][y] = True

    def wins(self):
        # check if there is a winning line
        for row in self.marks:
            if all(row):
                self.old_winner = True
                return True

        # rotate and check if there is a winning row
        for column in zip(*self.marks[::-1]):
            if all(column):
                self.old_winner = True
                return True

        return False

    def unmarked_numbers(self):
        return [
            self.numbers[x][y]
            for x in range(5) for y in range(5)
            if not self.marks[x][y]
        ]


def parse_input():
    with open("input.txt") as fd:
        numbers_drawn = [int(x) for x in fd.readline().strip().split(",")]

        boards = []
        while True:
            board = []

            if not fd.readline():
                # skip empty line and stop when eof reached
                break

            for _ in range(5):
                board.append([
                    int(x)
                    for x in re.split(r'\s+', fd.readline().strip())
                ])

            boards.append(Board(board))

    return numbers_drawn, boards


def bingo():
    numbers_drawn, boards = parse_input()
    for number in numbers_drawn:
        for board in boards:
            board.mark(number)
            if board.wins():
                return number * sum(board.unmarked_numbers())


def loser_bingo():
    numbers_drawn, boards = parse_input()
    for number in numbers_drawn:
        for board in boards:
            board.mark(number)
            if not board.old_winner and board.wins():
                last_score = number * sum(board.unmarked_numbers())

    return last_score


if __name__ == '__main__':
    print("part 1:", bingo())
    print("part 2:", loser_bingo())
