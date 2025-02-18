'''
Problem id: 1001-G
Statement: Implement a quantum oracle on N qubits which implements a function f(x) = xk, i.e. the value of the function is the value of the k-th qubit.

For an explanation on how the quantum oracles work, see the tutorial blog post.

You have to implement an operation which takes the following inputs:

The operation doesn't have an output; the "output" of your solution is the state in which it left the qubits.

Your code should have the following signature:
Tags: *specialproblem,*1400
'''

def classical_oracle(N, k, binary_string):
    """
    Simulate the behavior of a quantum oracle that checks the k-th bit.
    
    Args:
    - N: The number of bits (length of the binary string).
    - k: The index of the bit to query (0-indexed).
    - binary_string: A binary string of length N representing the input.
    
    Returns:
    - The value of the k-th bit (0 or 1).
    """
    # Ensure k is within bounds
    if k < 0 or k >= N:
        raise ValueError("k is out of bounds for the binary string provided.")
    # Return the k-th bit
    return int(binary_string[k])


def verify_classical_oracle(N, k, binary_string, expected_result):
    # Execute the classical Oracle
    result = classical_oracle(N, k, binary_string)
    
    # Print verification result
    if result == expected_result:
        print('verified')
    else:
        print(f'incorrect: expected {expected_result}, got {result}')

# Example verification call
# For N = 3, k = 1, binary_string = '010' (which should make the result 1), expected_result = 1
verify_classical_oracle(3, 1, '010', 1)