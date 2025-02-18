'''
Problem id: 1016-B
Statement: You are given two strings $$$s$$$ and $$$t$$$, both consisting only of lowercase Latin letters.

The substring $$$s[l..r]$$$ is the string which is obtained by taking characters $$$s_l, s_{l + 1}, \dots, s_r$$$ without changing the order.

Each of the occurrences of string $$$a$$$ in a string $$$b$$$ is a position $$$i$$$ ($$$1 \le i \le |b| - |a| + 1$$$) such that $$$b[i..i + |a| - 1] = a$$$ ($$$|a|$$$ is the length of string $$$a$$$).

You are asked $$$q$$$ queries: for the $$$i$$$-th query you are required to calculate the number of occurrences of string $$$t$$$ in a substring $$$s[l_i..r_i]$$$.

The first line contains three integer numbers $$$n$$$, $$$m$$$ and $$$q$$$ ($$$1 \le n, m \le 10^3$$$, $$$1 \le q \le 10^5$$$) — the length of string $$$s$$$, the length of string $$$t$$$ and the number of queries, respectively.

The second line is a string $$$s$$$ ($$$|s| = n$$$), consisting only of lowercase Latin letters.

The third line is a string $$$t$$$ ($$$|t| = m$$$), consisting only of lowercase Latin letters.

Each of the next $$$q$$$ lines contains two integer numbers $$$l_i$$$ and $$$r_i$$$ ($$$1 \le l_i \le r_i \le n$$$) — the arguments for the $$$i$$$-th query.

Print $$$q$$$ lines — the $$$i$$$-th line should contain the answer to the $$$i$$$-th query, that is the number of occurrences of string $$$t$$$ in a substring $$$s[l_i..r_i]$$$.

In the first example the queries are substrings: "cod", "deforces", "fo" and "for", respectively.
Tags: bruteforce,implementation,*1300
'''

def count_occurrences(n, m, q, s, t, queries):
    # Step 2: Preprocess occurrences of `t` in `s`
    occurrences = [0] * n
    for i in range(n - m + 1):
        if s[i:i+m] == t:
            occurrences[i] = 1

    # Step 3: Construct a prefix sum array
    prefix = [0] * n
    prefix[0] = occurrences[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + occurrences[i]

    # Step 4: Answer each query
    results = []
    for l, r in queries:
        l_index = l - 1
        r_index = r - 1

        # Calculate occurrences in s[l..r]
        if r - l + 1 < m:
            results.append(0)
        else:
            if l_index == 0:
                count = prefix[r_index - m + 1]
            else:
                count = prefix[r_index - m + 1] - prefix[l_index - 1]
            results.append(count)

    return results

# Test case
n = 8
m = 3
q = 4
s = "codeforces"
t = "for"
queries = [(1, 3), (4, 9), (3, 4), (5, 7)]

# Expected outcome for the queries: [0, 1, 0, 1]
expected = [0, 1, 0, 1]
actual = count_occurrences(n, m, q, s, t, queries)

# Verify output
if actual == expected:
    print('verified')
else:
    print(f'Error: expected {expected}, but got {actual}')