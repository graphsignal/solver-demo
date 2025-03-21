'''
Problem id: 1000-D
Statement: The sequence of integers $$$a_1, a_2, \dots, a_k$$$ is called a good array if $$$a_1 = k - 1$$$ and $$$a_1 > 0$$$. For example, the sequences $$$[3, -1, 44, 0], [1, -99]$$$ are good arrays, and the sequences $$$[3, 7, 8], [2, 5, 4, 1], [0]$$$ — are not.

A sequence of integers is called good if it can be divided into a positive number of good arrays. Each good array should be a subsegment of sequence and each element of the sequence should belong to exactly one array. For example, the sequences $$$[2, -3, 0, 1, 4]$$$, $$$[1, 2, 3, -3, -9, 4]$$$ are good, and the sequences $$$[2, -3, 0, 1]$$$, $$$[1, 2, 3, -3 -9, 4, 1]$$$ — are not.

For a given sequence of numbers, count the number of its subsequences that are good sequences, and print the number of such subsequences modulo 998244353.

The first line contains the number $$$n~(1 \le n \le 10^3)$$$ — the length of the initial sequence. The following line contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n~(-10^9 \le a_i \le 10^9)$$$ — the sequence itself.

In the single line output one integer — the number of subsequences of the original sequence that are good sequences, taken modulo 998244353.

In the first test case, two good subsequences — $$$[a_1, a_2, a_3]$$$ and $$$[a_2, a_3]$$$.

In the second test case, seven good subsequences — $$$[a_1, a_2, a_3, a_4], [a_1, a_2], [a_1, a_3], [a_1, a_4], [a_2, a_3], [a_2, a_4]$$$ and $$$[a_3, a_4]$$$.
Tags: combinatorics,dp,*1900
'''

MOD = 998244353

def count_good_subsequences(n, sequence):
    # dp[i] will store the number of ways to partition the subsequence a[1:i+1] into good arrays
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: empty subsequence

    total_good_sequences = 0

    # Iterate over every possible starting point
    for i in range(n):
        current_length = 0
        # Check if a subarray starting from i can be a good array
        for j in range(i, n):
            current_length += 1
            # Check if the subarray a[i...j] is a good array
            if sequence[i] == current_length - 1 and sequence[i] > 0:
                # If true, update the dp array at position j+1
                dp[j + 1] = (dp[j + 1] + dp[i]) % MOD

    # Sum over all dp[j] for j from 1 to n to count all possible good subsequences
    total_good_sequences = sum(dp[1:]) % MOD

    return total_good_sequences

# Test scenario
def test_solution():
    # Example 1
    n1 = 5
    sequence1 = [2, -3, 0, 1, 4]
    expected1 = 2

    # Example 2
    n2 = 4
    sequence2 = [1, 2, 3, 4]
    expected2 = 7

    result1 = count_good_subsequences(n1, sequence1)
    result2 = count_good_subsequences(n2, sequence2)

    if result1 == expected1:
        print('Example 1 verified')
    else:
        print(f'Example 1 incorrect, expected {expected1}, got {result1}')

    if result2 == expected2:
        print('Example 2 verified')
    else:
        print(f'Example 2 incorrect, expected {expected2}, got {result2}')

# Call the test function
test_solution()