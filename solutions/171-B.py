'''
Problem id: 171-B
Statement: The input contains a single integer a (1 ≤ a ≤ 18257).

Print a single integer output (1 ≤ output ≤ 2·109).
Tags: *specialproblem,combinatorics,*1300
'''

def solution(a: int) -> int:
    # Applying the triangular number formula T(a) = a * (a + 1) / 2
    return a * (a + 1) // 2

# Test for verification
# Let's use some known triangular numbers for verification
# T_1 = 1, T_2 = 3, T_3 = 6, T_4 = 10, ..., T_n = n(n+1)/2

# Verification cases: (input, expected_output)
test_cases = [
    (1, 1),   # T_1
    (2, 3),   # T_2
    (3, 6),   # T_3
    (4, 10),  # T_4
    (5, 15),  # T_5
    (100, 5050), # a larger case to check the pattern 
    (18257, 166730653) # Checking the upper bound case
]

# Verification
for a, expected in test_cases:
    result = solution(a)
    if result == expected:
        print(f'Case {a} verified.')
    else:
        print(f'Case {a} incorrect: expected {expected}, got {result}')