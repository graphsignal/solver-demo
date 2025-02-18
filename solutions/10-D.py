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

def lcis(sequence1, sequence2):
    n = len(sequence1)
    m = len(sequence2)

    # DP array to store lengths of increasing subsequences
    dp = [0] * (m + 1)
    
    # To store the previous elements to backtrace the sequence
    prev = [-1] * (m + 1)

    # Auxiliary array to reconstruct the sequence
    max_length = 0
    end_pos = -1

    for i in range(n):
        current_length = 0
        seq_end_index = -1

        for j in range(m):
            if sequence1[i] == sequence2[j]:
                if current_length + 1 > dp[j + 1]:
                    dp[j + 1] = current_length + 1
                    prev[j + 1] = seq_end_index

                    if dp[j + 1] > max_length:
                        max_length = dp[j + 1]
                        end_pos = j

            if sequence1[i] > sequence2[j]:
                if dp[j + 1] > current_length:
                    current_length = dp[j + 1]
                    seq_end_index = j

    # Reconstruct the LCIS
    lcis_sequence = []
    while end_pos != -1:
        lcis_sequence.append(sequence2[end_pos])
        end_pos = prev[end_pos + 1]

    lcis_sequence.reverse()  # To get the sequence in correct order

    return max_length, lcis_sequence


def verify_lcis(sequence1, sequence2, expected_length, expected_seq):
    length, seq = lcis(sequence1, sequence2)
    if length == expected_length and seq == expected_seq:
        print("verified")
    else:
        print("incorrect result")
        print(f"Expected length: {expected_length}, Actual length: {length}")
        print(f"Expected sequence: {expected_seq}, Actual sequence: {seq}")

# Test case
sequence1 = [1, 3, 4, 9]
sequence2 = [1, 2, 4, 6, 9]
expected_length = 3
expected_seq = [1, 4, 9]

verify_lcis(sequence1, sequence2, expected_length, expected_seq)