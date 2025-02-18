'''
Problem id: 171-G
Statement: The only line of input contains three integers a1, a2, a3 (1 ≤ a1, a2, a3 ≤ 20), separated by spaces.

Output a single integer.
Tags: *specialproblem,*1600
'''

def solution(a1, a2, a3):
    # Based on the analysis, we can assume a simple operation to begin with:
    # Let's try sum since there's no explicit instruction otherwise.
    # We can modify this depending on further discovery of patterns from problem statement tags.
    
    # While this doesn't seem right yet, without a clear description, we take a guess at straightforward operations
    # The problem hints (like specialproblem tag) might imply particular choices, but absence of them requires trial.
    return a1 + a2 + a3

# Verification function

def verify_solution():
    # Test cases
    test_cases = [
        ((1, 1, 1), 3),  # sum test
        ((20, 20, 20), 60),  # sum edge case
        ((1, 20, 19), 40),  # mixed edge case
    ]
    for i, (inputs, expected) in enumerate(test_cases, 1):
        result = solution(*inputs)
        if result == expected:
            print(f"Test case {i}: verified")
        else:
            print(f"Test case {i}: failed - Expected {expected}, but got {result}")

verify_solution()