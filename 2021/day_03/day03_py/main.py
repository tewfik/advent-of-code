diagnostic = [x.strip() for x in open("input.txt")]

# part 1

gamma_rate = ''
epsilon_rate = ''
for idx in range(len(diagnostic[0])):
    count_1 = 0
    for line in diagnostic:
        count_1 += (line[idx] == '1')

    if count_1 > (len(diagnostic) / 2):
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

print("part 1")
print(gamma_rate)
print(epsilon_rate)

print(int(gamma_rate, 2) * int(epsilon_rate, 2))


# part 2

def find_bit_criteria(diagnostic, idx, least_common=False):
    count_0 = 0
    count_1 = 0
    for line in diagnostic:
        if line[idx] == '1':
            count_1 += 1
        else:
            count_0 += 1

    if count_1 >= count_0:
        if least_common and count_0 > 0:
            bit_criteria = '0'
        else:
            bit_criteria = '1'
    else:
        if least_common and count_1 > 0:
            bit_criteria = '1'
        else:
            bit_criteria = '0'

    return bit_criteria


def find_rating(diagnostic, mode):
    """
    `mode` can be `co2_scrubber_rating` or `oxygen_generator_rating`
    """
    least_common = (mode == "co2_scrubber_rating")
    filtered_diagnostic = diagnostic
    for idx in range(len(diagnostic[0])):
        bit_criteria = find_bit_criteria(filtered_diagnostic, idx, least_common)
        filtered_diagnostic = [line for line in filtered_diagnostic if line[idx] == bit_criteria]

        if len(filtered_diagnostic) == 1:
            return filtered_diagnostic[0]


print("\npart 2")
print(int(find_rating(diagnostic, "oxygen_generator_rating"), 2) * int(find_rating(diagnostic, "co2_scrubber_rating"), 2))
