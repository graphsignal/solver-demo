'''
Problem id: 1005-B
Statement: You are given two strings $$$s$$$ and $$$t$$$. In a single move, you can choose any of two strings and delete the first (that is, the leftmost) character. After a move, the length of the string decreases by $$$1$$$. You can't choose a string if it is empty.

For example:

You are required to make two given strings equal using the fewest number of moves. It is possible that, in the end, both strings will be equal to the empty string, and so, are equal to each other. In this case, the answer is obviously the sum of the lengths of the initial strings.

Write a program that finds the minimum number of moves to make two given strings $$$s$$$ and $$$t$$$ equal.

The first line of the input contains $$$s$$$. In the second line of the input contains $$$t$$$. Both strings consist only of lowercase Latin letters. The number of letters in each string is between 1 and $$$2\cdot10^5$$$, inclusive.

Output the fewest number of moves required. It is possible that, in the end, both strings will be equal to the empty string, and so, are equal to each other. In this case, the answer is obviously the sum of the lengths of the given strings.

In the first example, you should apply the move once to the first string and apply the move once to the second string. As a result, both strings will be equal to "est".

In the second example, the move should be applied to the string "codeforces" $$$8$$$ times. As a result, the string becomes "codeforces" $$$\to$$$ "es". The move should be applied to the string "yes" once. The result is the same string "yes" $$$\to$$$ "es".

In the third example, you can make the strings equal only by completely deleting them. That is, in the end, both strings will be empty.

In the fourth example, the first character of the second string should be deleted.
Tags: bruteforce,implementation,strings,*900
'''

def min_moves_to_equal(s, t):
    len_s = len(s)
    len_t = len(t)
    common_suffix_length = 0
    
    # Traverse from the end of both strings
    i = len_s - 1
    j = len_t - 1
    
    while i >= 0 and j >= 0 and s[i] == t[j]:
        common_suffix_length += 1
        i -= 1
        j -= 1
    
    # Calculate the minimum moves needed
    min_moves = len_s + len_t - 2 * common_suffix_length
    return min_moves

# Test case verification
s = "prefixest"
t = "latest"
expected_output = 9
actual_output = min_moves_to_equal(s, t)

if actual_output == expected_output:
    print('verified')
else:
    print(f'Failed: expected {expected_output}, got {actual_output}')