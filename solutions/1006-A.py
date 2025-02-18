'''
Problem id: 1006-A
Statement: Mishka got an integer array $$$a$$$ of length $$$n$$$ as a birthday present (what a surprise!).

Mishka doesn't like this present and wants to change it somehow. He has invented an algorithm and called it "Mishka's Adjacent Replacements Algorithm". This algorithm can be represented as a sequence of steps:

Note that the dots in the middle of this algorithm mean that Mishka applies these replacements for each pair of adjacent integers ($$$2i - 1, 2i$$$) for each $$$i \in\{1, 2, \ldots, 5 \cdot 10^8\}$$$ as described above.

For example, for the array $$$a = [1, 2, 4, 5, 10]$$$, the following sequence of arrays represents the algorithm: 

$$$[1, 2, 4, 5, 10]$$$ $$$\rightarrow$$$ (replace all occurrences of $$$1$$$ with $$$2$$$) $$$\rightarrow$$$ $$$[2, 2, 4, 5, 10]$$$ $$$\rightarrow$$$ (replace all occurrences of $$$2$$$ with $$$1$$$) $$$\rightarrow$$$ $$$[1, 1, 4, 5, 10]$$$ $$$\rightarrow$$$ (replace all occurrences of $$$3$$$ with $$$4$$$) $$$\rightarrow$$$ $$$[1, 1, 4, 5, 10]$$$ $$$\rightarrow$$$ (replace all occurrences of $$$4$$$ with $$$3$$$) $$$\rightarrow$$$ $$$[1, 1, 3, 5, 10]$$$ $$$\rightarrow$$$ (replace all occurrences of $$$5$$$ with $$$6$$$) $$$\rightarrow$$$ $$$[1, 1, 3, 6, 10]$$$ $$$\rightarrow$$$ (replace all occurrences of $$$6$$$ with $$$5$$$) $$$\rightarrow$$$ $$$[1, 1, 3, 5, 10]$$$ $$$\rightarrow$$$ $$$\dots$$$ $$$\rightarrow$$$ $$$[1, 1, 3, 5, 10]$$$ $$$\rightarrow$$$ (replace all occurrences of $$$10$$$ with $$$9$$$) $$$\rightarrow$$$ $$$[1, 1, 3, 5, 9]$$$. The later steps of the algorithm do not change the array.

Mishka is very lazy and he doesn't want to apply these changes by himself. But he is very interested in their result. Help him find it.

The first line of the input contains one integer number $$$n$$$ ($$$1 \le n \le 1000$$$) — the number of elements in Mishka's birthday present (surprisingly, an array).

The second line of the input contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 10^9$$$) — the elements of the array.

Print $$$n$$$ integers — $$$b_1, b_2, \dots, b_n$$$, where $$$b_i$$$ is the final value of the $$$i$$$-th element of the array after applying "Mishka's Adjacent Replacements Algorithm" to the array $$$a$$$. Note that you cannot change the order of elements in the array.

The first example is described in the problem statement.
Tags: implementation,*800
'''

def mishkas_algorithm(n, array):
    # Initialize result array
    result = []
    
    # Process each element in the array
    for element in array:
        if element % 2 == 0:
            # Element is even
            result.append(element - 1)
        else:
            # Element is odd
            result.append(element + 1)
    
    return result

# Test function with an example
n_test = 5
array_test = [1, 2, 4, 5, 10]
expected_result_test = [2, 1, 3, 6, 9]

# Execute the solution function
actual_result_test = mishkas_algorithm(n_test, array_test)

# Verify the result
if actual_result_test == expected_result_test:
    print('verified')
else:
    print(f'incorrect result: actual {actual_result_test}, expected {expected_result_test}')