'''
Problem id: 10-D
Statement: This problem differs from one which was on the online contest.

The sequence a1, a2, ..., an is called increasing, if ai < ai + 1 for i < n.

The sequence s1, s2, ..., sk is called the subsequence of the sequence a1, a2, ..., an, if there exist such a set of indexes 1 ≤ i1 < i2 < ... < ik ≤ n that aij = sj. In other words, the sequence s can be derived from the sequence a by crossing out some elements.

You are given two sequences of integer numbers. You are to find their longest common increasing subsequence, i.e. an increasing sequence of maximum length that is the subsequence of both sequences.

The first line contains an integer n (1 ≤ n ≤ 500) — the length of the first sequence. The second line contains n space-separated integers from the range [0, 109] — elements of the first sequence. The third line contains an integer m (1 ≤ m ≤ 500) — the length of the second sequence. The fourth line contains m space-separated integers from the range [0, 109] — elements of the second sequence.

In the first line output k — the length of the longest common increasing subsequence. In the second line output the subsequence itself. Separate the elements with a space. If there are several solutions, output any.
Tags: dp,*2800
'''

def longest_common_increasing_subsequence(n, seq1, m, seq2):
    dp = [0] * m
    parent = [-1] * m

    LCIS_length = 0
    LCIS_end_pos = -1

    for i in range(n):
        current_max_length = 0
        last_valid_j = -1

        for j in range(m):
            if seq1[i] == seq2[j]:
                if current_max_length + 1 > dp[j]:
                    dp[j] = current_max_length + 1
                    parent[j] = last_valid_j
                if dp[j] > LCIS_length:
                    LCIS_length = dp[j]
                    LCIS_end_pos = j

            if seq1[i] > seq2[j]:
                if dp[j] > current_max_length:
                    current_max_length = dp[j]
                    last_valid_j = j

    LCIS = []
    pos = LCIS_end_pos
    while pos != -1:
        LCIS.append(seq2[pos])
        pos = parent[pos]

    LCIS.reverse()
    return LCIS_length, LCIS

# Test the function with a predefined example
n_test = 5
seq1_test = [2, 5, 1, 2, 3]
m_test = 6
seq2_test = [5, 3, 2, 4, 1, 2]
expected_length = 2
expected_sequence = [2, 3]  # Note: This could be different based on valid LCIS

result_length, result_sequence = longest_common_increasing_subsequence(n_test, seq1_test, m_test, seq2_test)

# Verify the output
if result_length == expected_length:
    # Check if the sequence is indeed a subsequence
    it = iter(seq2_test)
    if all(x in it for x in result_sequence) and all(x < y for x, y in zip(result_sequence, result_sequence[1:])):
        print('verified')
    else:
        print('Error: Resulting sequence is not a valid increasing subsequence.')
else:
    print(f'Error: Expected length {expected_length} but got {result_length}')