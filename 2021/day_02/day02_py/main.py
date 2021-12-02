raw_instructions = [
    line.strip().split(" ")
    for line in open("input.txt")
]
instructions = [(instruction, int(value)) for instruction, value in raw_instructions]


# part 1

depth, position = 0, 0
for instruction, value in instructions:
    if instruction == "up":
        depth -= value
    elif instruction == "down":
        depth += value
    elif instruction == "forward":
        position += value

print(depth * position)


# part 2
depth, position, aim = 0, 0, 0
for instruction, value in instructions:
    if instruction == "up":
        aim -= value
    elif instruction == "down":
        aim += value
    elif instruction == "forward":
        position += value
        depth += value * aim

print(depth * position)
