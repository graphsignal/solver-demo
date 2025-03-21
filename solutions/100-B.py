'''
Problem id: 100-B
Statement: Kiana thinks two integers are friends if and only if one of them divides the other one. For example, 12 and 4 are friends, also 6 and 6 are friends too, but 120 and 36 are not.

A group of non-zero integers is called friendly, if each pair of its integers form a friend pair.

You are given a group of non-zero integers. See if they're friendly.

The first line contains n (1 ≤ n ≤ 1000), where n — the number of integers in the group.

The next line contains the elements, sorted in the non-decreasing order. The numbers are comma separated, they have at most 7 digits in their decimal notation and do not have any leading zeros.

If the group is friendly write "FRIENDS", else write "NOT FRIENDS".
Tags: *specialproblem,implementation,*1500
'''

def are_friends(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[j] % numbers[i] != 0:
                return "NOT FRIENDS"
    return "FRIENDS"

# Verification function

def verify_solution():
    test_cases = [
        # Already sorted friendly group
        ([2, 4, 8, 16], "FRIENDS"),
        # Unfriendly group, 120 and 36 are not friends
        ([12, 24, 36, 120], "NOT FRIENDS"),
        # Single element is trivially friendly
        ([7], "FRIENDS"),
        # Friendly group, one divides the next one
        ([1, 2, 4, 8, 16, 32], "FRIENDS"),
        # Mixed numbers not entirely friendly
        ([3, 5, 15], "NOT FRIENDS"),
        # Edge case: larger numbers, not friendly
        ([1000000, 2000000, 3000000], "NOT FRIENDS"),
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        result = are_friends(nums)
        if result == expected:
            print(f"Test case {i+1}: verified")
        else:
            print(f"Test case {i+1}: failed - expected {expected}, got {result}")

# Run verification
verify_solution()