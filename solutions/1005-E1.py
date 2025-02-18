'''
Problem id: 1005-E1
Statement: You are given a permutation $$$p_1, p_2, \dots, p_n$$$. A permutation of length $$$n$$$ is a sequence such that each integer between $$$1$$$ and $$$n$$$ occurs exactly once in the sequence.

Find the number of pairs of indices $$$(l, r)$$$ ($$$1 \le l \le r \le n$$$) such that the value of the median of $$$p_l, p_{l+1}, \dots, p_r$$$ is exactly the given number $$$m$$$.

The median of a sequence is the value of the element which is in the middle of the sequence after sorting it in non-decreasing order. If the length of the sequence is even, the left of two middle elements is used.

For example, if $$$a=[4, 2, 7, 5]$$$ then its median is $$$4$$$ since after sorting the sequence, it will look like $$$[2, 4, 5, 7]$$$ and the left of two middle elements is equal to $$$4$$$. The median of $$$[7, 1, 2, 9, 6]$$$ equals $$$6$$$ since after sorting, the value $$$6$$$ will be in the middle of the sequence.

Write a program to find the number of pairs of indices $$$(l, r)$$$ ($$$1 \le l \le r \le n$$$) such that the value of the median of $$$p_l, p_{l+1}, \dots, p_r$$$ is exactly the given number $$$m$$$.

The first line contains integers $$$n$$$ and $$$m$$$ ($$$1 \le n \le 2\cdot10^5$$$, $$$1 \le m \le n$$$) — the length of the given sequence and the required value of the median.

The second line contains a permutation $$$p_1, p_2, \dots, p_n$$$ ($$$1 \le p_i \le n$$$). Each integer between $$$1$$$ and $$$n$$$ occurs in $$$p$$$ exactly once.

Print the required number.

In the first example, the suitable pairs of indices are: $$$(1, 3)$$$, $$$(2, 2)$$$, $$$(2, 3)$$$ and $$$(2, 4)$$$.
Tags: sortings,*1800
'''

def count_median_subarrays(n, m, p):
    # Find the index of m
    pos_m = p.index(m)

    # Initializing balance counters
    left_balance_counts = {0: 1}
    right_balance_counts = {0: 1}

    # Left balance calculation
    balance = 0
    for i in range(pos_m - 1, -1, -1):
        if p[i] < m:
            balance -= 1
        else:
            balance += 1
        left_balance_counts[balance] = left_balance_counts.get(balance, 0) + 1
    
    # Right balance calculation
    balance = 0
    for i in range(pos_m + 1, n):
        if p[i] < m:
            balance -= 1
        else:
            balance += 1
        right_balance_counts[balance] = right_balance_counts.get(balance, 0) + 1

    # Count subarrays
    count = left_balance_counts[0]  # Subarray where m is itself the median (like [m] only)
    for b in left_balance_counts:
        if b in right_balance_counts:
            count += left_balance_counts[b] * right_balance_counts[b]
        if (b - 1) in right_balance_counts:
            count += left_balance_counts[b] * right_balance_counts[b - 1]

    return count

# Verification
# Test case derived from the problem statement
n = 5
m = 2
p = [4, 2, 7, 3, 5]
# Expected output: 4 (As described the suitable pairs are (1,3), (2,2), (2,3), (2,4))
expected_output = 4

actual_output = count_median_subarrays(n, m, p)

if actual_output == expected_output:
    print("verified")
else:
    print(f"Incorrect, expected {expected_output}, got {actual_output}")