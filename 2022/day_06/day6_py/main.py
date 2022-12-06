def main():
    print(solve(4))
    print(solve(14))


def solve(n: int):
    stream = parse_input()

    for idx in range(len(stream)):
        if len(set(stream[idx: idx + n])) == n:
            return idx + n



def parse_input():
    return open("input.txt").readline().strip()


if __name__ == '__main__':
    main()
