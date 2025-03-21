'''
Problem id: 1000-A
Statement: Codehorses has just hosted the second Codehorses Cup. This year, the same as the previous one, organizers are giving T-shirts for the winners.

The valid sizes of T-shirts are either "M" or from $$$0$$$ to $$$3$$$ "X" followed by "S" or "L". For example, sizes "M", "XXS", "L", "XXXL" are valid and "XM", "Z", "XXXXL" are not.

There are $$$n$$$ winners to the cup for both the previous year and the current year. Ksenia has a list with the T-shirt sizes printed for the last year cup and is yet to send the new list to the printing office. 

Organizers want to distribute the prizes as soon as possible, so now Ksenia is required not to write the whole list from the scratch but just make some changes to the list of the previous year. In one second she can choose arbitrary position in any word and replace its character with some uppercase Latin letter. Ksenia can't remove or add letters in any of the words.

What is the minimal number of seconds Ksenia is required to spend to change the last year list to the current one?

The lists are unordered. That means, two lists are considered equal if and only if the number of occurrences of any string is the same in both lists.

The first line contains one integer $$$n$$$ ($$$1 \le n \le 100$$$) — the number of T-shirts.

The $$$i$$$-th of the next $$$n$$$ lines contains $$$a_i$$$ — the size of the $$$i$$$-th T-shirt of the list for the previous year.

The $$$i$$$-th of the next $$$n$$$ lines contains $$$b_i$$$ — the size of the $$$i$$$-th T-shirt of the list for the current year.

It is guaranteed that all the sizes in the input are valid. It is also guaranteed that Ksenia can produce list $$$b$$$ from the list $$$a$$$.

Print the minimal number of seconds Ksenia is required to spend to change the last year list to the current one. If the lists are already equal, print 0.

In the first example Ksenia can replace "M" with "S" and "S" in one of the occurrences of "XS" with "L".

In the second example Ksenia should replace "L" in "XXXL" with "S".

In the third example lists are equal.
Tags: greedy,implementation,*1200
'''

from collections import defaultdict

# Function to determine the minimum number of changes required to transform list a into list b

def min_changes_to_match(a, b):
    # Count occurrences of each size in list a and list b
    count_a = defaultdict(int)
    count_b = defaultdict(int)
    
    for size in a:
        count_a[size] += 1
    for size in b:
        count_b[size] += 1
        
    # Calculate the total number of changes required
    changes = 0
    all_sizes = set(count_a.keys()).union(set(count_b.keys()))
    
    for size in all_sizes:
        if size in count_a or size in count_b:
            changes += abs(count_a[size] - count_b[size])

    # Each change fixes two mismatches, so divide by 2
    return changes // 2

# Test the solution function

def test_solution():
    # Test case 1
    a1 = ["M", "S", "XS"]
    b1 = ["S", "M", "L"]
    expected1 = 2  # Change one "M" to "S" and one "S" to "L"
    result1 = min_changes_to_match(a1, b1)
    if result1 == expected1:
        print('Test 1 verified')
    else:
        print(f'Test 1 failed: expected {expected1}, but got {result1}')

    # Test case 2
    a2 = ["XXL", "XXXL", "L"]
    b2 = ["XXL", "L", "M"]
    expected2 = 1  # Change "XXXL" to "M"
    result2 = min_changes_to_match(a2, b2)
    if result2 == expected2:
        print('Test 2 verified')
    else:
        print(f'Test 2 failed: expected {expected2}, but got {result2}')
    
    # Test case 3
    a3 = ["L", "M"]
    b3 = ["M", "L"]
    expected3 = 0  # Lists are already equivalent
    result3 = min_changes_to_match(a3, b3)
    if result3 == expected3:
        print('Test 3 verified')
    else:
        print(f'Test 3 failed: expected {expected3}, but got {result3}')

# Run the test

# The code is designed not to take external input, just to run these tests
test_solution()