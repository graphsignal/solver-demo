'''
Problem id: 1005-C
Statement: A sequence $$$a_1, a_2, \dots, a_n$$$ is called good if, for each element $$$a_i$$$, there exists an element $$$a_j$$$ ($$$i \ne j$$$) such that $$$a_i+a_j$$$ is a power of two (that is, $$$2^d$$$ for some non-negative integer $$$d$$$).

For example, the following sequences are good:

Note that, by definition, an empty sequence (with a length of $$$0$$$) is good.

For example, the following sequences are not good:

You are given a sequence $$$a_1, a_2, \dots, a_n$$$. What is the minimum number of elements you need to remove to make it good? You can delete an arbitrary set of elements.

The first line contains the integer $$$n$$$ ($$$1 \le n \le 120000$$$) — the length of the given sequence.

The second line contains the sequence of integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 10^9$$$).

Print the minimum number of elements needed to be removed from the given sequence in order to make it good. It is possible that you need to delete all $$$n$$$ elements, make it empty, and thus get a good sequence.

In the first example, it is enough to delete one element $$$a_4=5$$$. The remaining elements form the sequence $$$[4, 7, 1, 4, 9]$$$, which is good.
Tags: bruteforce,greedy,implementation,*1300
'''

def min_removals_to_make_good(n, sequence):
    # Precompute powers of two up to 2^31 (since 2 billion < 2^31)
    powers_of_two = set()
    power = 1
    while power <= 2 * 10**9:
        powers_of_two.add(power)
        power *= 2

    # Frequency map of the sequence
    freq_map = {}
    for num in sequence:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    # Determine the number of elements to remove
    # Unpaired elements counter
    unpaired_elements = 0
    used_elements = set()

    for num in sequence:
        if num in used_elements:
            # If already paired as a good sequence, skip
            continue
        
        found_pair = False
        for power in powers_of_two:
            # Check if there's another number in the sequence that pairs with num
            needed_pair = power - num
            if needed_pair in freq_map:
                if needed_pair != num or freq_map[num] > 1:
                    found_pair = True
                    break

        if not found_pair:
            unpaired_elements += 1

        # Mark all occurrences of this number as used
        used_elements.add(num)

    return unpaired_elements

# Test case
sequence = [4, 7, 1, 5, 4, 9]
n = len(sequence)
expected_result = 1
actual_result = min_removals_to_make_good(n, sequence)

if actual_result == expected_result:
    print("verified")
else:
    print(f"Test case failed: expected {expected_result}, got {actual_result}")