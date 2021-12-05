def parse_input():
    lines = []
    for x in open("input.txt"):
        l1, l2 = x.strip().split(" -> ")
        x1, y1 = l1.split(",")
        x2, y2 = l2.split(",")
        lines.append(
            (int(x1), int(y1), int(x2), int(y2)),
        )

    return lines


def filter_vertical_and_horizontal_lines(lines):
    return [
        (x1, y1, x2, y2)
        for (x1, y1, x2, y2) in lines
        if (x1 == x2) or (y1 == y2)
    ]


def filter_vertical_horizontal_diagonal_lines(lines):
    return [
        (x1, y1, x2, y2)
        for (x1, y1, x2, y2) in lines
        if (x1 == x2) or (y1 == y2) or (((x1 - x2) % (y1 - y2)) == 0)
    ]


def matrix_size(lines):
    max_x = 0
    max_y = 0
    for x1, y1, x2, y2 in lines:
        if x1 > max_x:
            max_x = x1
        if x2 > max_x:
            max_x = x2
        if y1 > max_y:
            max_y = y1
        if y2 > max_y:
            max_y = y2

    return max_x, max_y


def gen_matrix(x, y):
    return [
        [0] * (y + 1)
        for _ in range(x + 1)
    ]


def mark(matrix, line):
    for x, y in list_points(line):
        try:
            matrix[x][y] += 1
        except:
            import pdb; pdb.set_trace()


def list_points(line):
    x1, y1, x2, y2 = line
    if x1 == x2:
        if y1 > y2:
            y_range = range(y2, y1 + 1)
        else:
            y_range = range(y1, y2 + 1)

        points = [(x1, y) for y in y_range]
    elif y1 == y2:
        if x1 > x2:
            x_range = range(x2, x1 + 1)
        else:
            x_range = range(x1, x2 + 1)

        points = [(x, y1) for x in x_range]
    elif (((x1 - x2) % (y1 - y2)) == 0):
        return list_diagonal_points(x1, y1, x2, y2)
    else:
        raise NotImplementedError()

    return points


def list_diagonal_points(x1, y1, x2, y2):
    if x1 < x2:
        if y1 < y2:
            points = [(x1 + idx, y1 + idx) for idx in range(x2 - x1 + 1) ]
        else:
            points = [(x1 + idx, y1 - idx) for idx in range(x2 - x1 + 1) ]
    else:
        if y1 < y2:
            points = [(x1 - idx, y1 + idx) for idx in range(x1 - x2 + 1) ]
        else:
            points = [(x1 - idx, y1 - idx) for idx in range(x1 - x2 + 1) ]

    return points


def bak(x1, y1, x2, y2):
    if x1 < x2:
        if y1 < y2:
            points = [(x1 + idx, y1 + idx) for idx in range(x1 - 1, x2) ]
        else:
            points = [(x1 + idx, y1 - idx) for idx in range(x1 - 1, x2) ]
    else:
        if y1 < y2:
            points = [(x1 - idx, y1 + idx) for idx in range(x2 - 1, x1) ]
        else:
            points = [(x1 - idx, y1 - idx) for idx in range(x2 - 1, x1) ]

    return points


def get_overlap(matrix):
    return [
        cell for row in matrix for cell in row  if cell > 1
    ]


def solve_part_1():
    lines = parse_input()
    vert_hor_lines = filter_vertical_and_horizontal_lines(lines)
    matrix = gen_matrix(*matrix_size(vert_hor_lines))

    for line in vert_hor_lines:
        mark(matrix, line)

    return len(get_overlap(matrix))


def solve_part_2():
    lines = parse_input()
    vert_hor_diag_lines = filter_vertical_horizontal_diagonal_lines(lines)
    matrix = gen_matrix(*matrix_size(vert_hor_diag_lines))

    for line in vert_hor_diag_lines:
        mark(matrix, line)

    return len(get_overlap(matrix))


if __name__ == '__main__':
    print("part 1")
    print(solve_part_1())

    print("part 2")
    print(solve_part_2())
