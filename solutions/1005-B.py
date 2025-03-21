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

def min_moves_to_equal_strings(s: str, t: str) -> int:
    # Initialize the counter for the common suffix length
    common_suffix_length = 0
    
    # Indices to iterate from the end of strings s and t
    i, j = len(s) - 1, len(t) - 1
    
    # While characters are the same in the suffix
    while i >= 0 and j >= 0 and s[i] == t[j]:
        # Increment the common suffix length counter
        common_suffix_length += 1
        # Move to the next characters
        i -= 1
        j -= 1
    
    # Calculate the number of moves needed
    moves = (len(s) + len(t) - 2 * common_suffix_length)
    return moves

# Test cases and verification
# Test case 1
s1 = "test"
t1 = "best"
expected1 = 2
result1 = min_moves_to_equal_strings(s1, t1)
assert result1 == expected1, f"Test 1 Failed: Expected {expected1}, got {result1}"

# Test case 2
s2 = "codeforces"
t2 = "yes"
expected2 = 9
result2 = min_moves_to_equal_strings(s2, t2)
assert result2 == expected2, f"Test 2 Failed: Expected {expected2}, got {result2}"

# Test case 3 (completely different strings)
s3 = "abcdef"
t3 = "uvwxyz"
expected3 = len(s3) + len(t3)
result3 = min_moves_to_equal_strings(s3, t3)
assert result3 == expected3, f"Test 3 Failed: Expected {expected3}, got {result3}"

# Test case 4 (one string is a suffix of the other)
s4 = "abracadabra"
t4 = "cadabra"
expected4 = len(s4) - len(t4)
result4 = min_moves_to_equal_strings(s4, t4)
assert result4 == expected4, f"Test 4 Failed: Expected {expected4}, got {result4}"

print('verified')