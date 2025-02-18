'''
Problem id: 171-A
Statement: The input contains two integers a1, a2 (0 ≤ ai ≤ 109), separated by a single space.

Output a single integer.
Tags: *specialproblem,constructivealgorithms,*1200
'''

def solution(a1, a2):
    """
    Given two integers a1 and a2, return their sum
    :param a1: First integer
    :param a2: Second integer
    :return: The sum of a1 and a2
    """
    return a1 + a2

# Test case
# Example: a1 = 1, a2 = 2. The expected result is 3
a1_test, a2_test = 1, 2
expected_result = 3

# Verify the solution
def verify_solution(a1, a2, expected):
    result = solution(a1, a2)
    if result == expected:
        print("verified")
    else:
        print(f"Verification failed: Expected {expected}, but got {result}")

verify_solution(a1_test, a2_test, expected_result)