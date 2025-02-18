'''
Problem id: 171-H
Statement: The input contains two integers a, b (1 ≤ a ≤ 10, 0 ≤ b ≤ 22·a - 1) separated by a single space.

Output two integers separated by a single space.
Tags: *specialproblem,implementation,*1700
'''

def solution(a, b):
    # The first number is the integer division of b by 22
    first = b // 22
    # The second number is the remainder when b is divided by 22
    second = b % 22
    return (first, second)

# Verification function
# We'll test for a range of inputs within the defined constraints.
def verify_solution():
    test_cases = [
        (1, 0, (0, 0)), # b = 0
        (1, 21, (0, 21)), # b just below 22
        (1, 22, (1, 0)), # b exactly 22
        (2, 22, (1, 0)), # a = 2, b = 22
        (10, 219, (9, 21)), # a = 10, b = 219
        (10, 220, (10, 0)), # Edge case, max b = 22*a - 1
    ]

    all_passed = True
    for a, b, expected in test_cases:
        result = solution(a, b)
        if result == expected:
            print(f"Test passed for a = {a}, b = {b}")
        else:
            all_passed = False
            print(f"Test failed for a = {a}, b = {b}. Expected {expected}, but got {result}.")

    if all_passed:
        print('All tests passed and verified.')
    else:
        print('Some tests failed.')

verify_solution()