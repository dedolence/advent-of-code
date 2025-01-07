"""
    If a test fails, send it to a new list of inputs to attempt.


    if len(test) == 1: return True  # passed all tests

    if len(test) < 4: return False  # had one removed already, need 4 good tests to pass

    if distance > 2: remove test[i] and return check_test(test)

    if direction != direction: remove test[i] and return check_test(test)

    return check_test(test[1:])


    a, b = test[i], test[i+1]

"""

def check_test(test, i=0, direction=None):
    if i == len(test) - 1:
        return True
    
    if len(test) < 4:
        return False
    
    a, b = test[i], test[i + 1]

    if direction == None:
        # False evaluates to 0, True to 1, so they can be used as indices
        direction = ("<", ">")[a - b > 0]

    diff = (abs(a - b) > 0 and abs(a - b) <= 3)
    dire = eval(f"{a}{direction}{b}")
    
    if diff and dire:
        return check_test(test, i + 1, direction)
    else:    
        no_a = test.copy()
        del no_a[i]
        
        no_b = test.copy()
        del no_b[i+1]
        return check_test(no_a, 0, None) or check_test(no_b, 0, None)



def Xcheck_test(test=list, i=0, direction=None):
    if i == len(test) - 1:
        # checked all the numbers, all good.
        return True
    
    if len(test) < 4:
        # already tried removing a number and still found a failure.
        print(f"test too short...", end=" ")
        return False
    
    a, b = test[i], test[i + 1]

    no_a = test.copy()
    del no_a[i]
    
    no_b = test.copy()
    del no_b[i+1]

    if abs(a - b) < 1 or abs(a - b) > 3:
        # try removing one or the other values and see if that works
        return check_test(no_a, 0, None) or check_test(no_b, 0, None)

    if direction == None:
        # False evaluates to 0, True to 1, so they can be used as indices
        direction = ("<", ">")[a - b > 0]

    if eval(f"{a}{direction}{b}") is False:
        # reversed sign, therefore try removing test[i]
        del test[i+1]
        return check_test(no_a, 0, None) or check_test(no_b, 0, None)

    return check_test(test, i + 1, direction)
    


with open("input.txt") as input:
    safe_tests = 0
    tests = [line.strip() for line in input.readlines()]
    for test in tests:
        test = [int(i) for i in test.split(" ")]    # convert to integers
        print(f"testing {test}...", end=" ")
        if check_test(test):
            print(f"test passed!")
            safe_tests += 1
        else:
            print(f"test failed.")
    
    print(safe_tests)