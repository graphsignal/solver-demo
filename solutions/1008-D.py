'''
Problem id: 1008-D
Statement: You are given a rectangular parallelepiped with sides of positive integer lengths $$$A$$$, $$$B$$$ and $$$C$$$. 

Find the number of different groups of three integers ($$$a$$$, $$$b$$$, $$$c$$$) such that $$$1\leq a\leq b\leq c$$$ and parallelepiped $$$A\times B\times C$$$ can be paved with parallelepipeds $$$a\times b\times c$$$. Note, that all small parallelepipeds have to be rotated in the same direction.

For example, parallelepiped $$$1\times 5\times 6$$$ can be divided into parallelepipeds $$$1\times 3\times 5$$$, but can not be divided into parallelepipeds $$$1\times 2\times 3$$$.

The first line contains a single integer $$$t$$$ ($$$1 \leq t \leq 10^5$$$) — the number of test cases.

Each of the next $$$t$$$ lines contains three integers $$$A$$$, $$$B$$$ and $$$C$$$ ($$$1 \leq A, B, C \leq 10^5$$$) — the sizes of the parallelepiped.

For each test case, print the number of different groups of three points that satisfy all given conditions.

In the first test case, rectangular parallelepiped $$$(1, 1, 1)$$$ can be only divided into rectangular parallelepiped with sizes $$$(1, 1, 1)$$$.

In the second test case, rectangular parallelepiped $$$(1, 6, 1)$$$ can be divided into rectangular parallelepipeds with sizes $$$(1, 1, 1)$$$, $$$(1, 1, 2)$$$, $$$(1, 1, 3)$$$ and $$$(1, 1, 6)$$$.

In the third test case, rectangular parallelepiped $$$(2, 2, 2)$$$ can be divided into rectangular parallelepipeds with sizes $$$(1, 1, 1)$$$, $$$(1, 1, 2)$$$, $$$(1, 2, 2)$$$ and $$$(2, 2, 2)$$$. 
Tags: math,numbertheory,*2400
'''

def solve_parallelepiped_problem(test_cases):
    results = []

    for A, B, C in test_cases:
        # Ensure A <= B <= C by sorting
        A, B, C = sorted([A, B, C])
        count = 0

        # Iterate over possible a, b, c
        for a in range(1, A + 1):
            if A % a == 0:  # a divides A
                for b in range(a, B + 1):
                    if B % b == 0:  # b divides B
                        for c in range(b, C + 1):
                            if C % c == 0:  # c divides C
                                count += 1
        results.append(count)

    return results

# Let's test the function with example cases

def test_solve_parallelepiped_problem():
    test_cases = [
        (1, 1, 1),  # Single unit
        (1, 6, 1),  # Thin line
        (2, 2, 2),  # Cube
        (1, 2, 3),  # Small arbitrary case
    ]
    # Expected results:
    # (1, 1, 1) -> 1 (as only itself)
    # (1, 6, 1) -> 4 (e.g., (1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 6))
    # (2, 2, 2) -> 4 (e.g., (1, 1, 1), (1, 1, 2), (1, 2, 2), (2, 2, 2))
    # (1, 2, 3) -> 7 (e.g., (1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 2), (1, 2, 3))

    expected_results = [1, 4, 4, 7]
    results = solve_parallelepiped_problem(test_cases)

    for i, (result, expected) in enumerate(zip(results, expected_results)):
        if result == expected:
            print(f"Test case {i + 1} verified.")
        else:
            print(f"Test case {i + 1} failed. Expected {expected}, got {result}.")

# Run the verification test
test_solve_parallelepiped_problem()