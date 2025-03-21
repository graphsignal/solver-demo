'''
Problem id: 1-A
Statement: Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a × a.

What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.

The input contains three positive integer numbers in the first line: n,  m and a (1 ≤  n, m, a ≤ 109).

Write the needed number of flagstones.
Tags: math,*1000
'''

def calculate_flagstones(n, m, a):
    # Calculate the number of flagstones needed along each dimension
    num_flagstones_length = (n + a - 1) // a
    num_flagstones_width = (m + a - 1) // a
    
    # Total number of flagstones is the product of the numbers needed for each dimension
    total_flagstones = num_flagstones_length * num_flagstones_width
    
    return total_flagstones

# Test case where n, m, a are 6, 6, 4 respectively,
# Expected output is 4 flagstones
n, m, a = 6, 6, 4
expected_output = 4

# Call the function with the test case
result = calculate_flagstones(n, m, a)

# Verify the result
if result == expected_output:
    print('verified')
else:
    print(f'incorrect result: expected {expected_output}, but got {result}')