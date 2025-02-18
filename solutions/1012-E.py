'''
Problem id: 1012-E
Statement: You are given an array of $$$n$$$ positive integers $$$a_1, a_2, \dots, a_n$$$. You can perform the following operation any number of times: select several distinct indices $$$i_1, i_2, \dots, i_k$$$ ($$$1 \le i_j \le n$$$) and move the number standing at the position $$$i_1$$$ to the position $$$i_2$$$, the number at the position $$$i_2$$$ to the position $$$i_3$$$, ..., the number at the position $$$i_k$$$ to the position $$$i_1$$$. In other words, the operation cyclically shifts elements: $$$i_1 \to i_2 \to \ldots i_k \to i_1$$$.

For example, if you have $$$n=4$$$, an array $$$a_1=10, a_2=20, a_3=30, a_4=40$$$, and you choose three indices $$$i_1=2$$$, $$$i_2=1$$$, $$$i_3=4$$$, then the resulting array would become $$$a_1=20, a_2=40, a_3=30, a_4=10$$$.

Your goal is to make the array sorted in non-decreasing order with the minimum number of operations. The additional constraint is that the sum of cycle lengths over all operations should be less than or equal to a number $$$s$$$. If it's impossible to sort the array while satisfying that constraint, your solution should report that as well.

The first line of the input contains two integers $$$n$$$ and $$$s$$$ ($$$1 \leq n \leq 200\,000$$$, $$$0 \leq s \leq 200\,000$$$)—the number of elements in the array and the upper bound on the sum of cycle lengths.

The next line contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$—elements of the array ($$$1 \leq a_i \leq 10^9$$$).

If it's impossible to sort the array using cycles of total length not exceeding $$$s$$$, print a single number "-1" (quotes for clarity).

Otherwise, print a single number $$$q$$$— the minimum number of operations required to sort the array.

On the next $$$2 \cdot q$$$ lines print descriptions of operations in the order they are applied to the array. The description of $$$i$$$-th operation begins with a single line containing one integer $$$k$$$ ($$$1 \le k \le n$$$)—the length of the cycle (that is, the number of selected indices). The next line should contain $$$k$$$ distinct integers $$$i_1, i_2, \dots, i_k$$$ ($$$1 \le i_j \le n$$$)—the indices of the cycle.

The sum of lengths of these cycles should be less than or equal to $$$s$$$, and the array should be sorted after applying these $$$q$$$ operations.

If there are several possible answers with the optimal $$$q$$$, print any of them.

In the first example, it's also possible to sort the array with two operations of total length 5: first apply the cycle $$$1 \to 4 \to 1$$$ (of length 2), then apply the cycle $$$2 \to 3 \to 5 \to 2$$$ (of length 3). However, it would be wrong answer as you're asked to use the minimal possible number of operations, which is 1 in that case.

In the second example, it's possible to the sort the array with two cycles of total length 4 ($$$1 \to 2 \to 1$$$ and $$$3 \to 4 \to 3$$$). However, it's impossible to achieve the same using shorter cycles, which is required by $$$s=3$$$.

In the third example, the array is already sorted, so no operations are needed. Total length of empty set of cycles is considered to be zero.
Tags: dsu,math,*3100
'''

from typing import List, Tuple

def solve_sorting_problem(n: int, s: int, array: List[int]) -> Tuple[int, List[Tuple[int, List[int]]]]:
    indexed_array = [(value, index) for index, value in enumerate(array)]
    indexed_array.sort()  # Sort by value, maintain original indexes

    used = [False] * n
    operations = []
    total_cycle_length = 0

    # Find cycles
    for i in range(n):
        if used[i]:
            continue
        cycle = []
        current = i
        while not used[current]:
            used[current] = True
            cycle.append(current + 1)  # Convert to 1-based index
            current = indexed_array[current][1]

        if len(cycle) > 1:
            operations.append((len(cycle), cycle))
            total_cycle_length += len(cycle)

    if total_cycle_length > s:
        return -1, []  # Impossible to perform within the given sum of cycle lengths

    return len(operations), operations

# Test verification function
n = 4
s = 3
array = [10, 40, 20, 30]

# Expected result: Any correct cycle combination that sorts the array and respects the constraints
expected_possible_results = [
    (1, [(3, [1, 3, 4])]),
    (1, [(3, [2, 3, 4])])
]

# Run the solution
actual_result = solve_sorting_problem(n, s, array)

# Verification logic
if actual_result in expected_possible_results:
    print('verified')
else:
    print(f'Failed! Expected one of: {expected_possible_results}, but got: {actual_result}')