'''
Problem id: 1003-B
Statement: You are given three integers $$$a$$$, $$$b$$$ and $$$x$$$. Your task is to construct a binary string $$$s$$$ of length $$$n = a + b$$$ such that there are exactly $$$a$$$ zeroes, exactly $$$b$$$ ones and exactly $$$x$$$ indices $$$i$$$ (where $$$1 \le i < n$$$) such that $$$s_i \ne s_{i + 1}$$$. It is guaranteed that the answer always exists.

For example, for the string "01010" there are four indices $$$i$$$ such that $$$1 \le i < n$$$ and $$$s_i \ne s_{i + 1}$$$ ($$$i = 1, 2, 3, 4$$$). For the string "111001" there are two such indices $$$i$$$ ($$$i = 3, 5$$$).

Recall that binary string is a non-empty sequence of characters where each character is either 0 or 1.

The first line of the input contains three integers $$$a$$$, $$$b$$$ and $$$x$$$ ($$$1 \le a, b \le 100, 1 \le x < a + b)$$$.

Print only one string $$$s$$$, where $$$s$$$ is any binary string satisfying conditions described above. It is guaranteed that the answer always exists.

All possible answers for the first example: 

All possible answers for the second example: 
Tags: constructivealgorithms,*1300
'''

def generate_binary_string(a, b, x):
    result = []

    # Determine starting character
    if a > b:
        start_with_0 = True
    else:
        start_with_0 = False
    
    # Create alternating pattern
    current_char = '0' if start_with_0 else '1'
    for _ in range(x):
        result.append(current_char)
        current_char = '1' if current_char == '0' else '0'
    
    # Add last part having same starting char if x is odd
    result.append(current_char)
    
    result = ''.join(result)
    
    # Count usage in pattern
    used_a = result.count('0')
    used_b = result.count('1')

    # Calculate remaining zeros and ones
    remaining_a = a - used_a
    remaining_b = b - used_b

    # Allocate remaining zeros and ones
    if start_with_0:
        # Add remaining zeros and ones
        result = ('0' * remaining_a) + result
        result = result + ('1' * remaining_b)
    else:
        result = ('1' * remaining_b) + result
        result = result + ('0' * remaining_a)
    
    return result

# Test and verification
a, b, x = 5, 4, 5
expected_transitions = x

result = generate_binary_string(a, b, x)
actual_a = result.count('0')
actual_b = result.count('1')
actual_transitions = sum(1 for i in range(len(result) - 1) if result[i] != result[i + 1])

# Check if the result satisfies all conditions
if actual_a == a and actual_b == b and actual_transitions == expected_transitions:
    print('verified')
else:
    print(f'Incorrect solution. Expected a={a}, b={b}, x={expected_transitions}. Got a={actual_a}, b={actual_b}, x={actual_transitions}.')
    print(f'Constructed string: {result}')