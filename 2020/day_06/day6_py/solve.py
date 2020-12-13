def parse_input():
    return [x.strip() for x in open("input.txt").read().split("\n\n")]


def part_1():
    groups = parse_input()
    print(sum(len(set(group.replace("\n", ""))) for group in groups))


def part_2():
    groups = [group.split("\n") for group in parse_input()]
    count = sum(common_questions(group) for group in groups)
    print(count)


def common_questions(group_questions):
    commonly_answered_questions_count = 0

    for question in group_questions[0]:
        everybody_answered_the_question = True
        for people_answers in group_questions:
            if question not in people_answers:
                everybody_answered_the_question = False
        if everybody_answered_the_question:
            commonly_answered_questions_count += 1

    return commonly_answered_questions_count


if __name__ == '__main__':
    part_1()
    part_2()
