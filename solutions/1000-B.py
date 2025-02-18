'''
Problem id: 1000-B
Statement: Recently, you bought a brand new smart lamp with programming features. At first, you set up a schedule to the lamp. Every day it will turn power on at moment $$$0$$$ and turn power off at moment $$$M$$$. Moreover, the lamp allows you to set a program of switching its state (states are "lights on" and "lights off"). Unfortunately, some program is already installed into the lamp.

The lamp allows only good programs. Good program can be represented as a non-empty array $$$a$$$, where $$$0 < a_1 < a_2 < \dots < a_{|a|} < M$$$. All $$$a_i$$$ must be integers. Of course, preinstalled program is a good program.

The lamp follows program $$$a$$$ in next manner: at moment $$$0$$$ turns power and light on. Then at moment $$$a_i$$$ the lamp flips its state to opposite (if it was lit, it turns off, and vice versa). The state of the lamp flips instantly: for example, if you turn the light off at moment $$$1$$$ and then do nothing, the total time when the lamp is lit will be $$$1$$$. Finally, at moment $$$M$$$ the lamp is turning its power off regardless of its state.

Since you are not among those people who read instructions, and you don't understand the language it's written in, you realize (after some testing) the only possible way to alter the preinstalled program. You can insert at most one element into the program $$$a$$$, so it still should be a good program after alteration. Insertion can be done between any pair of consecutive elements of $$$a$$$, or even at the begining or at the end of $$$a$$$.

Find such a way to alter the program that the total time when the lamp is lit is maximum possible. Maybe you should leave program untouched. If the lamp is lit from $$$x$$$ till moment $$$y$$$, then its lit for $$$y - x$$$ units of time. Segments of time when the lamp is lit are summed up.

First line contains two space separated integers $$$n$$$ and $$$M$$$ ($$$1 \le n \le 10^5$$$, $$$2 \le M \le 10^9$$$) — the length of program $$$a$$$ and the moment when power turns off.

Second line contains $$$n$$$ space separated integers $$$a_1, a_2, \dots, a_n$$$ ($$$0 < a_1 < a_2 < \dots < a_n < M$$$) — initially installed program $$$a$$$.

Print the only integer — maximum possible total time when the lamp is lit.

In the first example, one of possible optimal solutions is to insert value $$$x = 3$$$ before $$$a_1$$$, so program will be $$$[3, 4, 6, 7]$$$ and time of lamp being lit equals $$$(3 - 0) + (6 - 4) + (10 - 7) = 8$$$. Other possible solution is to insert $$$x = 5$$$ in appropriate place.

In the second example, there is only one optimal solution: to insert $$$x = 2$$$ between $$$a_1$$$ and $$$a_2$$$. Program will become $$$[1, 2, 10]$$$, and answer will be $$$(1 - 0) + (10 - 2) = 9$$$.

In the third example, optimal answer is to leave program untouched, so answer will be $$$(3 - 0) + (7 - 4) = 6$$$.
Tags: greedy,*1500
'''

def calculate_lit_time(n, M, a):
    # Calculate initial lit time without any insertion
    lit_time = 0
    last_on_time = 0
    for i in range(n):
        if i % 2 == 0:
            # Lit interval
            lit_time += a[i] - last_on_time
        last_on_time = a[i]
    if n % 2 == 0:
        # If n is even, add the period from the last element to M
        lit_time += M - last_on_time

    # Maximum lit time when inserting no additional point
    max_lit_time = lit_time

    # Explore inserting a new point

    # Check inserting after 0
    if n == 0 or a[0] > 1:
        max_lit_time = max(max_lit_time, (a[0] - 1) + (M - a[-1]))

    # Check inserting in between any two points a[i] and a[i+1]
    for i in range(n-1):
        if (i+1) % 2 == 1:  # In between lit periods
            additional_lit = a[i+1] - a[i]
            new_lit_time = lit_time + additional_lit
            max_lit_time = max(max_lit_time, new_lit_time)

    # Check inserting after the last element
    if n == 0 or a[-1] < M - 1:
        max_lit_time = max(max_lit_time, lit_time + (M - a[-1]))

    return max_lit_time


# Verification function
def verify_solution():
    # Test cases
    test_cases = [
        # Format: (n, M, a, expected_result)
        (3, 10, [4, 6, 7], 8),    # Possible insertion at 3 or 5 or no insertion
        (2, 10, [1, 10], 9),      # Optimal insertion at x=2
        (2, 7, [3, 4], 6),        # Leave program untouched
    ]

    for i, (n, M, a, expected) in enumerate(test_cases):
        result = calculate_lit_time(n, M, a)
        if result == expected:
            print(f'Test case {i} verified')
        else:
            print(f'Test case {i} failed. Expected {expected}, got {result}')

verify_solution()  # Run the verification function to check correctness