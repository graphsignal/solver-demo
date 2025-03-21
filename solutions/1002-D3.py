'''
Problem id: 1002-D3
Statement: Implement a quantum oracle on 3 qubits which implements a majority function. Majority function on 3-bit vectors is defined as follows:  if vector  has two or three 1s, and 0 if it has zero or one 1s.

For an explanation on how this type of quantum oracles works, see Introduction to quantum oracles.

You have to implement an operation which takes the following inputs:

The operation doesn't have an output; its "output" is the state in which it leaves the qubits.

Your code should have the following signature:
Tags: *1600
'''

def majority_oracle_classical(a, b, c):
    # Returns 1 if two or more of the three bits are 1
    return (a & b) | (a & c) | (b & c)


def verify_majority_oracle():
    # Test various input combinations
    test_cases = [
        (0, 0, 0, 0), 
        (0, 0, 1, 0), 
        (0, 1, 0, 0), 
        (0, 1, 1, 1), 
        (1, 0, 0, 0), 
        (1, 0, 1, 1), 
        (1, 1, 0, 1), 
        (1, 1, 1, 1)
    ]
    
    for a, b, c, expected in test_cases:
        result = majority_oracle_classical(a, b, c)
        if result == expected:
            print(f'Input ({a}, {b}, {c}): verified')
        else:
            print(f'Input ({a}, {b}, {c}): Error, expected {expected} got {result}')

# Run verification
verify_majority_oracle()