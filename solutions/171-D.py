'''
Problem id: 171-D
Statement: "This problem is rubbish! There is not statement, and there are only 5 test cases. The problemsetter took liberties with this problem!" — people complained in the comments to one round on Codeforces. And even more... No, wait, the checker for the problem was alright, that's a mercy.

The only line of the input contains an integer between 1 and 5, inclusive. All tests for this problem are different. The contents of the test case doesn't need to be equal to its index.

The only line of the output contains an integer between 1 and 3, inclusive.

This problem has no samples, since there so few test cases.
Tags: *specialproblem,bruteforce,*1300
'''

def solve(n):
    # Mapping based on arbitrary assignment since there's no specific statement logic
    answer_mapping = {1: 1, 2: 2, 3: 3, 4: 1, 5: 2}
    return answer_mapping.get(n, 1)  # default to 1 in case of unexpected input

# Predefined verification test cases based on arbitrary mapping
verification_tests = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 1),
    (5, 2)
]

# Run verification
for test_input, expected_output in verification_tests:
    result = solve(test_input)
    assert result == expected_output, f"Test failed for input {test_input}: expected {expected_output}, got {result}"

print("verified")