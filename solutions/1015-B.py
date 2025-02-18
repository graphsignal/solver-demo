'''
Problem id: 1015-B
Statement: You are given two strings $$$s$$$ and $$$t$$$. Both strings have length $$$n$$$ and consist of lowercase Latin letters. The characters in the strings are numbered from $$$1$$$ to $$$n$$$.

You can successively perform the following move any number of times (possibly, zero):

You can't apply a move to the string $$$t$$$. The moves are applied to the string $$$s$$$ one after another.

Your task is to obtain the string $$$t$$$ from the string $$$s$$$. Find any way to do it with at most $$$10^4$$$ such moves.

You do not have to minimize the number of moves, just find any sequence of moves of length $$$10^4$$$ or less to transform $$$s$$$ into $$$t$$$.

The first line of the input contains one integer $$$n$$$ ($$$1 \le n \le 50$$$) — the length of strings $$$s$$$ and $$$t$$$.

The second line of the input contains the string $$$s$$$ consisting of $$$n$$$ lowercase Latin letters.

The third line of the input contains the string $$$t$$$ consisting of $$$n$$$ lowercase Latin letters.

If it is impossible to obtain the string $$$t$$$ using moves, print "-1".

Otherwise in the first line print one integer $$$k$$$ — the number of moves to transform $$$s$$$ to $$$t$$$. Note that $$$k$$$ must be an integer number between $$$0$$$ and $$$10^4$$$ inclusive.

In the second line print $$$k$$$ integers $$$c_j$$$ ($$$1 \le c_j < n$$$), where $$$c_j$$$ means that on the $$$j$$$-th move you swap characters $$$s_{c_j}$$$ and $$$s_{c_j + 1}$$$.

If you do not need to apply any moves, print a single integer $$$0$$$ in the first line and either leave the second line empty or do not print it at all.

In the first example the string $$$s$$$ changes as follows: "abcdef" $$$\rightarrow$$$ "abdcef" $$$\rightarrow$$$ "abdcfe" $$$\rightarrow$$$ "abdfce" $$$\rightarrow$$$ "abdfec".

In the second example there is no way to transform the string $$$s$$$ into the string $$$t$$$ through any allowed moves.
Tags: implementation,*1200
'''

def transform_string(n, s, t):
    # Step 1: Check if transformation is impossible
    if sorted(s) != sorted(t):
        return -1, []

    # Step 2: Perform transformation
    operations = []  # List to store the operations (swap indices)

    # We use a bubble-sort-like method to move each character of s to the desired position
    s = list(s)  # Convert string to list for easier swapping
    for i in range(n):
        if s[i] != t[i]:
            # Find the position j > i where s[j] == t[i]
            j = i
            while s[j] != t[i]:
                j += 1
            # Move s[j] to s[i] by swapping adjacent elements
            for k in range(j, i, -1):
                s[k], s[k - 1] = s[k - 1], s[k]
                operations.append(k)  # Append the 1-based index

    # Return number of operations and the operations themselves
    return len(operations), operations

# Verification code
n = 6
s = "abcdef"
t = "abdfec"
k, operations = transform_string(n, s, t)

# Expected output is transformation possible with a number of moves
expected_k = 4  # This may vary depending on the exact sequence of swaps
expected_operations_length = 4  # The number of moves required to transform

if k == expected_k and len(operations) == expected_operations_length:
    print("verified")
else:
    print(f"Incorrect result: k = {k}, operations length = {len(operations)}. Expected: k = {expected_k}, operations length = {expected_operations_length}.")
    print("Actual operations:", operations)