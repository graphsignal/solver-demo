'''
Problem id: 1013-F
Statement: There are two strings s and t, consisting only of letters a and b. You can make the following operation several times: choose a prefix of s, a prefix of t and swap them. Prefixes can be empty, also a prefix can coincide with a whole string. 

Your task is to find a sequence of operations after which one of the strings consists only of a letters and the other consists only of b letters. The number of operations should be minimized.

The first line contains a string s (1 ≤ |s| ≤ 2·105).

The second line contains a string t (1 ≤ |t| ≤ 2·105).

Here |s| and |t| denote the lengths of s and t, respectively. It is guaranteed that at least one of the strings contains at least one a letter and at least one of the strings contains at least one b letter.

The first line should contain a single integer n (0 ≤ n ≤ 5·105) — the number of operations.

Each of the next n lines should contain two space-separated integers ai, bi — the lengths of prefixes of s and t to swap, respectively.

If there are multiple possible solutions, you can print any of them. It's guaranteed that a solution with given constraints exists.

In the first example, you can solve the problem in two operations:

In the second example, the strings are already appropriate, so no operations are needed.
Tags: constructivealgorithms,strings,*2800
'''

def solve_strings(s, t):
    operations = []
    
    count_a_s = s.count('a')
    count_b_s = s.count('b')
    count_a_t = t.count('a')
    count_b_t = t.count('b')
    
    # Check if transformation is needed
    if (count_a_s == len(s) and count_b_t == len(t)) or (count_b_s == len(s) and count_a_t == len(t)):
        return operations  # No need for operations
    
    # Tracking mismatches
    a_to_b_mismatch = b_to_a_mismatch = 0
    positions_a_to_b = []
    positions_b_to_a = []
    
    # Identify mismatches between s and t
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            if s[i] == 'a':
                a_to_b_mismatch += 1
                positions_a_to_b.append(i)
            else:
                b_to_a_mismatch += 1
                positions_b_to_a.append(i)
    
    # Try to resolve mismatches
    while a_to_b_mismatch > 0 and b_to_a_mismatch > 0:
        # Swapping the first mismatched positions
        operations.append((positions_a_to_b[-1] + 1, positions_b_to_a[-1] + 1))
        positions_a_to_b.pop()
        positions_b_to_a.pop()
        a_to_b_mismatch -= 1
        b_to_a_mismatch -= 1
    
    # If there's still imbalance
    while a_to_b_mismatch >= 2:
        operations.append((positions_a_to_b[-1] + 1, positions_a_to_b[-2] + 1))
        positions_a_to_b.pop()
        positions_a_to_b.pop()
        a_to_b_mismatch -= 2
    
    while b_to_a_mismatch >= 2:
        operations.append((positions_b_to_a[-1] + 1, positions_b_to_a[-2] + 1))
        positions_b_to_a.pop()
        positions_b_to_a.pop()
        b_to_a_mismatch -= 2

    return operations

def verify_solution(s, t, expected_result):
    actual_result = solve_strings(s, t)
    # Manually apply operations and verify
    s_copy = list(s)
    t_copy = list(t)
    for (a_idx, b_idx) in actual_result:
        # Perform the swap operation
        s_prefix = s_copy[:a_idx]
        t_prefix = t_copy[:b_idx]
        s_copy[:a_idx], t_copy[:b_idx] = t_prefix, s_prefix
    
    # Check if the result matches expectation
    if s_copy.count('a') == len(s_copy) and t_copy.count('b') == len(t_copy):
        if len(actual_result) == expected_result:
            print('verified')
        else:
            print(f'Incorrect number of operations: Expected {expected_result}, got {len(actual_result)}')
    else:
        expected_s = 'a' * len(s)
        expected_t = 'b' * len(t)
        actual_s = ''.join(s_copy)
        actual_t = ''.join(t_copy)
        print(f'Resulting strings not as expected: Expected ({expected_s}, {expected_t}), got ({actual_s}, {actual_t})')

# Example verification call
# Example where two operations are needed
verify_solution("ababa", "babab", 2)
# Example where no operations are needed
verify_solution("aaa", "bbb", 0)