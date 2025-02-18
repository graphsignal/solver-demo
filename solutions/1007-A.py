'''
Problem id: 1007-A
Statement: You are given an array of integers. Vasya can permute (change order) its integers. He wants to do it so that as many as possible integers will become on a place where a smaller integer used to stand. Help Vasya find the maximal number of such integers.

For instance, if we are given an array $$$[10, 20, 30, 40]$$$, we can permute it so that it becomes $$$[20, 40, 10, 30]$$$. Then on the first and the second positions the integers became larger ($$$20>10$$$, $$$40>20$$$) and did not on the third and the fourth, so for this permutation, the number that Vasya wants to maximize equals $$$2$$$. Read the note for the first example, there is one more demonstrative test case.

Help Vasya to permute integers in such way that the number of positions in a new array, where integers are greater than in the original one, is maximal.

The first line contains a single integer $$$n$$$ ($$$1 \leq n \leq 10^5$$$) — the length of the array.

The second line contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \leq a_i \leq 10^9$$$) — the elements of the array.

Print a single integer — the maximal number of the array's elements which after a permutation will stand on the position where a smaller element stood in the initial array.

In the first sample, one of the best permutations is $$$[1, 5, 5, 3, 10, 1, 1]$$$. On the positions from second to fifth the elements became larger, so the answer for this permutation is 4.

In the second sample, there is no way to increase any element with a permutation, so the answer is 0.
Tags: combinatorics,datastructures,math,sortings,twopointers,*1300
'''

def maximize_positions(n, a):
    # Step 2: Sort the array to get the ordered elements
    sorted_a = sorted(a)

    # Split the sorted array into two halves
    left = sorted_a[:n//2]
    right = sorted_a[n//2:]

    # Initialize pointers for each half
    i, j = 0, 0
    max_count = 0

    # Step 4 & 5: Use two pointers to count the maximal number of elements
    while i < len(left) and j < len(right):
        if right[j] > left[i]:
            max_count += 1
            i += 1
        j += 1

    return max_count

# Verification call
# Test Case: Example from problem statement
n = 7
array = [1, 5, 3, 5, 10, 1, 1]
expected_result = 4

# Get actual result from the function
actual_result = maximize_positions(n, array)

# Check and print verification result
if actual_result == expected_result:
    print("verified")
else:
    print(f"incorrect: got {actual_result}, expected {expected_result}")

# Additional Test Case: No possible increase scenario
n = 4
array = [10, 10, 10, 10]
expected_result = 0

# Get actual result from the function
actual_result = maximize_positions(n, array)

# Check and print verification result
if actual_result == expected_result:
    print("verified")
else:
    print(f"incorrect: got {actual_result}, expected {expected_result}")