
def check_test(test, direction=None):
    if len(test) == 1:
        return True
    
    a, b = test[0], test[1]

    dif = abs(a - b)
    if dif < 1 or dif > 3:
        return False
    
    if direction == None:
        # False evaluates to 0, True to 1, so they can be used as indices
        direction = ("<", ">")[a - b > 0]

    if eval(f"{a}{direction}{b}"):
        return check_test(test[1:], direction)  # direction is consistent, call again with next two
    else:
        return False



with open("input.txt") as input:
    safe_tests = 0
    tests = [line.strip() for line in input.readlines()]
    for test in tests:
        test = [int(i) for i in test.split(" ")]    # convert to integers
        if check_test(test):
            safe_tests += 1
    
    print(safe_tests)