count = 0
sonar_data = [int(line) for line in open("input.txt")]

a = sonar_data[0]
b = sonar_data[1]
c = sonar_data[2]

idx = 1

while True:
    try:
        next_a = sonar_data[idx + 1]
        next_b = sonar_data[idx + 2]
        next_c = sonar_data[idx + 3]

        if a + b + c < next_a + next_b + next_c:
            count += 1

        a, b, c = next_a, next_b, next_c

        idx += 1
    except IndexError:
        break

print(count)
