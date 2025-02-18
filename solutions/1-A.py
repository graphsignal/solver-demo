'''
Problem id: 1-A
Statement: Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a × a.

What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.

The input contains three positive integer numbers in the first line: n,  m and a (1 ≤  n, m, a ≤ 109).

Write the needed number of flagstones.
Tags: math,*1000
'''

def min_flagstones(n, m, a):
    # Calculate the number of flagstones needed along each dimension
    flagstones_for_length = (n + a - 1) // a  # This is equivalent to math.ceil(n / a)
    flagstones_for_width = (m + a - 1) // a  # This is equivalent to math.ceil(m / a)
    
    # Total number of flagstones is the product of these numbers
    total_flagstones = flagstones_for_length * flagstones_for_width
    return total_flagstones

# Test the function with an example
n, m, a = 6, 6, 4
actual_output = min_flagstones(n, m, a)
expected_output = 4  # 2 flagstones needed in both directions

# Verification
if actual_output == expected_output:
    print('verified')
else:
    print(f'Incorrect result: got {actual_output}, expected {expected_output}')