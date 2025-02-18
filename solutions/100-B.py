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

def are_friends(integers):
    """
    Determine if the group of integers is friendly.

    Parameters:
    integers (list): A list of sorted non-zero integers.

    Returns:
    str: "FRIENDS" if the group is friendly, otherwise "NOT FRIENDS".
    """
    n = len(integers)

    if n == 1:
        # A single integer group is always friendly.
        return "FRIENDS"

    # Check divisibility condition
    for i in range(n - 1):
        if integers[i + 1] % integers[i] != 0:
            return "NOT FRIENDS"

    return "FRIENDS"

def test_solution():
    # Test case: Expected result is "FRIENDS"
    test1 = [3, 6, 12]
    expected1 = "FRIENDS"
    result1 = are_friends(test1)
    
    # Test case: Expected result is "NOT FRIENDS"
    test2 = [5, 20, 45]
    expected2 = "NOT FRIENDS"
    result2 = are_friends(test2)
    
    # Verification
    if result1 == expected1:
        print("Test 1 verified")
    else:
        print(f"Test 1 failed: got {result1}, expected {expected1}")

    
    if result2 == expected2:
        print("Test 2 verified")
    else:
        print(f"Test 2 failed: got {result2}, expected {expected2}")

# Run the test function
test_solution()