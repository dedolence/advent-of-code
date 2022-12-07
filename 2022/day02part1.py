ordered_scores_part1 = ["BX", "CY", "AZ", "AX", "BY", "CZ", "CX", "AY", "BZ"]
ordered_scores_part2 = ["BX", "CX", "AX", "AY", "BY", "CY", "CZ", "AZ", "BZ"]

def get_score(input_list):
    with open("inputs/day02.txt") as input:
        return sum(map(lambda pair: input_list.index(pair) + 1, map(lambda line: ''.join(line.strip().split()), input.readlines())))

print(get_score(ordered_scores_part1))
print(get_score(ordered_scores_part2))
"""
    X = lose
    y = draw
    z = win

    AY: rock + draw = rock = (outcome + choice) = 3 + 1 = 4
    BX: paper + loss = rock = 0 + 1 = 1
    CZ: scissors + win = rock = 6 + 1 = 7

    OpponentOutcome -> Our choice = Outcome + Choice = Score
    AX -> Z = 0 + 3 = 3
    AY -> X = 3 + 1 = 4
    AZ -> Y = 6 + 2 = 8

    BX -> X = 0 + 1 = 1
    BY -> Y = 3 + 2 = 5
    BZ -> Z = 6 + 3 = 9

    CX -> Y = 0 + 2 = 2
    CY -> Z = 3 + 3 = 6
    CZ -> X = 6 + 1 = 7

    ordered_scores = ["BX", "CX", "AX", "AY", "BY", "CY", "CZ", "AZ", "BZ"]
"""