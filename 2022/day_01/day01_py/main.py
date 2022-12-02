def part1():
    max_calories = 0
    current_elf_calories = 0

    for row in open("input.txt"):
        if not row.strip():
            max_calories = max(max_calories, current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(row.strip())

    print(f"max calories = {max_calories}")

def part2():
    top3_max_calories = [0] * 3
    current_elf_calories = 0

    for row in open("input.txt"):
        if not row.strip():
            top3_max_calories = sorted(top3_max_calories + [current_elf_calories], reverse=True)[:3]
            current_elf_calories = 0
        else:
            current_elf_calories += int(row.strip())

    print(f"top 3 max calories = {sum(top3_max_calories)}")

if __name__ == '__main__':
    part1()
    part2()
