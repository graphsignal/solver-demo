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

def solve_tshirt_problem(n, a, b):
    from collections import Counter
    
    # Count frequencies of each size in both lists
    counter_a = Counter(a)
    counter_b = Counter(b)
    
    # Calculate differences
    extra_a = counter_a - counter_b  # Sizes in `a` that are extra
    extra_b = counter_b - counter_a  # Sizes in `b` that are needed
    
    # Initialize changes counter
    changes = 0
    
    # Convert to lists of sizes with counts needed
    extra_a_items = list(extra_a.items())
    extra_b_items = list(extra_b.items())

    # Create variables to track current indices in extra_a and extra_b
    i, j = 0, 0

    while i < len(extra_a_items) and j < len(extra_b_items):
        a_size, a_count = extra_a_items[i]
        b_size, b_count = extra_b_items[j]
        
        # Find the minimum count we can change for the current pair
        min_count = min(a_count, b_count)

        # Calculate the number of changes: since the size strings are the same length, the change count is for each character
        changes += min_count * len(a_size)

        # Update the counts
        a_count -= min_count
        b_count -= min_count

        # If we've used up all counts for a_size, move to the next extra_a
        if a_count == 0:
            i += 1
        else:
            extra_a_items[i] = (a_size, a_count)  # Update the count

        # If we've fulfilled all needs for b_size, move to the next extra_b
        if b_count == 0:
            j += 1
        else:
            extra_b_items[j] = (b_size, b_count)  # Update the count

    return changes

# Test the function with a given test case
n = 5
previous_year = ['M', 'S', 'XS', 'XL', 'XXXL']
current_year = ['S', 'XS', 'M', 'L', 'XXXL']

# Expected result is 2
actual_result = solve_tshirt_problem(n, previous_year, current_year)
expected_result = 2

# Verification
if actual_result == expected_result:
    print('verified')
else:
    print(f'verification failed: expected {expected_result}, got {actual_result}')