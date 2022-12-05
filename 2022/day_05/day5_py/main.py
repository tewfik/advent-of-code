from collections import defaultdict

def main():
    print(solve(9000))
    print(solve(9001))


def solve(crane):
    stacks, instructions = parse_input()

    for instruction in instructions:
        if crane == 9000:
            execute9000(instruction, stacks)
        elif crane == 9001:
            execute9001(instruction, stacks)
        else:
            raise ValueError("Crane unknown")

    return "".join(stack[-1] for stack in stacks)


def parse_input():
    input_ = open("input.txt")

    # parse stacks input data
    reversed_stacks = defaultdict(list)
    for row in input_:
        if row.startswith(" 1"):
            # end of stacks data
            next(input_)  # skip the blank line
            break

        for idx, crate in enumerate(row[1::4]):
            if crate != " ":
                reversed_stacks[idx + 1].append(crate)

    stacks = []
    for idx in range(1, len(reversed_stacks) + 1):
        stacks.append(reversed_stacks[idx][::-1])


    # parse instructions input dataflow
    instructions = []
    for row in input_:
        row = row.strip().split(" ")
        instructions.append((
            int(row[1]),
            int(row[3]) - 1,  # count from zero
            int(row[5]) - 1,  # count from zero
        ))

    return stacks, instructions


def execute9000(instruction, stacks):
    nb_crates, source, destination = instruction
    for _ in range(nb_crates):
        stacks[destination].append(stacks[source].pop())


def execute9001(instruction, stacks):
    nb_crates, source, destination = instruction

    crates = []
    for _ in range(nb_crates):
        crates.append(stacks[source].pop())

    stacks[destination].extend(crates[::-1])


if __name__ == '__main__':
    main()
