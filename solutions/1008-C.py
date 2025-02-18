'''
Problem id: 1008-C
Statement: You are given an array of integers. Vasya can permute (change order) its integers. He wants to do it so that as many as possible integers will become on a place where a smaller integer used to stand. Help Vasya find the maximal number of such integers.

For instance, if we are given an array $$$[10, 20, 30, 40]$$$, we can permute it so that it becomes $$$[20, 40, 10, 30]$$$. Then on the first and the second positions the integers became larger ($$$20>10$$$, $$$40>20$$$) and did not on the third and the fourth, so for this permutation, the number that Vasya wants to maximize equals $$$2$$$. Read the note for the first example, there is one more demonstrative test case.

Help Vasya to permute integers in such way that the number of positions in a new array, where integers are greater than in the original one, is maximal.

The first line contains a single integer $$$n$$$ ($$$1 \leq n \leq 10^5$$$) — the length of the array.

The second line contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \leq a_i \leq 10^9$$$) — the elements of the array.

Print a single integer — the maximal number of the array's elements which after a permutation will stand on the position where a smaller element stood in the initial array.

In the first sample, one of the best permutations is $$$[1, 5, 5, 3, 10, 1, 1]$$$. On the positions from second to fifth the elements became larger, so the answer for this permutation is 4.

In the second sample, there is no way to increase any element with a permutation, so the answer is 0.
Tags: combinatorics,math,*1300
'''

def maximum_elements_greater_than_original(n, array):
    # Step 1: Sort the array
    sorted_array = sorted(array)
    
    # Step 2: Use two pointers
    i, j = 0, (n + 1) // 2  # j starts from the middle point
    count = 0

    # Step 3: Try to place elements from the second half to maximize elements > original
    while i < (n + 1) // 2 and j < n:
        if sorted_array[j] > sorted_array[i]:
            # Successfully found a position where the element from second half is larger
            count += 1
            i += 1
        j += 1

    # Step 4: Return the maximum number of such positions
    return count

# Test Verification Function

def verify_solution():
    # Test case 1
    array1 = [1, 5, 3, 3, 10, 1, 1]
    expected_output1 = 4
    result1 = maximum_elements_greater_than_original(len(array1), array1)
    if result1 == expected_output1:
        print('Test Case 1: Verified')
    else:
        print(f'Test Case 1: Failed (Output: {result1}, Expected: {expected_output1})')

    # Test case 2
    array2 = [5, 5, 5, 5]
    expected_output2 = 0  # No element can be greater than the original since all are the same
    result2 = maximum_elements_greater_than_original(len(array2), array2)
    if result2 == expected_output2:
        print('Test Case 2: Verified')
    else:
        print(f'Test Case 2: Failed (Output: {result2}, Expected: {expected_output2})')

verify_solution()