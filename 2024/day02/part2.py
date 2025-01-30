"""
Rules:
all ascending or all descending
0 < gaps between numbers < 4
safe if 1 number can be removed to fulfill above rules
"""


def full_test(report):
    # test the report as-is, it might not need alteration.
    if individual_test(report):
        return True
    else:
        # for each index in the report list, prepare a new list without that index
        # test that new list in the same way. if any of these sub-tests pass, return True
        # if none of them pass, return False.
        for n in range(len(report)):
            new_report = report[:n] + report[n + 1:]
            if individual_test(new_report):
                return True
        return False


def individual_test(report, direction=None):
    if len(report) == 1:
        return True
    
    a, b = report[0], report[1]

    dif = abs(a - b)
    if dif < 1 or dif > 3:
        return False
    
    if direction == None:
        # False evaluates to 0, True to 1, so they can be used as indices
        direction = ("<", ">")[a - b > 0]

    if eval(f"{a}{direction}{b}"):
        return individual_test(report[1:], direction)  # direction is consistent, call again with next two
    else:
        return False


with open("input.txt") as input:
    safe_reports = 0
    reports = [line.strip() for line in input.readlines()]
    for report in reports:
        report = [int(i) for i in report.split(" ")]    # convert to integers
        if full_test(report):
            safe_reports += 1

    print(safe_reports)
        