'''
Problem id: 1007-B
Statement: You are given a rectangular parallelepiped with sides of positive integer lengths $$$A$$$, $$$B$$$ and $$$C$$$. 

Find the number of different groups of three integers ($$$a$$$, $$$b$$$, $$$c$$$) such that $$$1\leq a\leq b\leq c$$$ and parallelepiped $$$A\times B\times C$$$ can be paved with parallelepipeds $$$a\times b\times c$$$. Note, that all small parallelepipeds have to be rotated in the same direction.

For example, parallelepiped $$$1\times 5\times 6$$$ can be divided into parallelepipeds $$$1\times 3\times 5$$$, but can not be divided into parallelepipeds $$$1\times 2\times 3$$$.

The first line contains a single integer $$$t$$$ ($$$1 \leq t \leq 10^5$$$) — the number of test cases.

Each of the next $$$t$$$ lines contains three integers $$$A$$$, $$$B$$$ and $$$C$$$ ($$$1 \leq A, B, C \leq 10^5$$$) — the sizes of the parallelepiped.

For each test case, print the number of different groups of three points that satisfy all given conditions.

In the first test case, rectangular parallelepiped $$$(1, 1, 1)$$$ can be only divided into rectangular parallelepiped with sizes $$$(1, 1, 1)$$$.

In the second test case, rectangular parallelepiped $$$(1, 6, 1)$$$ can be divided into rectangular parallelepipeds with sizes $$$(1, 1, 1)$$$, $$$(1, 1, 2)$$$, $$$(1, 1, 3)$$$ and $$$(1, 1, 6)$$$.

In the third test case, rectangular parallelepiped $$$(2, 2, 2)$$$ can be divided into rectangular parallelepipeds with sizes $$$(1, 1, 1)$$$, $$$(1, 1, 2)$$$, $$$(1, 2, 2)$$$ and $$$(2, 2, 2)$$$. 
Tags: bitmasks,bruteforce,combinatorics,math,numbertheory,*2400
'''

from math import isqrt

def count_groups(test_cases):
    def get_divisors(n):
        divisors = set()
        for i in range(1, isqrt(n) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
        return sorted(divisors)

    results = []
    for A, B, C in test_cases:
        # Sort dimensions
        A, B, C = sorted((A, B, C))
        # Generate all divisors
        a_divisors = get_divisors(A)
        b_divisors = get_divisors(B)
        c_divisors = get_divisors(C)

        count = 0
        # Check all valid combinations of a, b, c
        for a in a_divisors:
            for b in b_divisors:
                for c in c_divisors:
                    if a <= b <= c:
                        # Check if the larger parallelepiped can be fully divided
                        if (A % a == 0 and B % b == 0 and C % c == 0):
                            if ((A // a) * (B // b) * (C // c)) > 0:
                                count += 1

        results.append(count)

    return results

def test_solution():
    # Example test cases with expected results
    test_cases = [
        ((1, 1, 1), 1),
        ((1, 6, 1), 4),
        ((2, 2, 2), 4)
    ]

    input_cases = [case[0] for case in test_cases]
    expected_results = [case[1] for case in test_cases]
    actual_results = count_groups(input_cases)

    for i, (actual, expected) in enumerate(zip(actual_results, expected_results)):
        if actual == expected:
            print(f'Test case #{i+1}: verified')
        else:
            print(f'Test case #{i+1}: failed - Expected {expected}, got {actual}')

# Run the test

test_solution()