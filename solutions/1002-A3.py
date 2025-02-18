'''
Problem id: 1002-A3
Statement: You are given N qubits (1 ≤ N ≤ 8) in zero state . You are also given two bitstrings bits0 and bits1 which describe two different basis states on N qubits  and .

Your task is to generate a state which is an equal superposition of the given basis states:

You have to implement an operation which takes the following inputs:

The operation doesn't have an output; its "output" is the state in which it leaves the qubits.

Your code should have the following signature:
Tags: *1500
'''

import math

# Function to create a quantum superposition state vector
def create_superposition(bits0, bits1):
    # Determine the number of qubits
    N = len(bits0)
    
    # Calculate the indices for the basis states
    index0 = int(bits0, 2)
    index1 = int(bits1, 2)
    
    # Ensure they represent different states
    assert index0 != index1, "bits0 and bits1 should not be the same."

    # Initialize a state vector with complex number tuples (real, imaginary)
    state_vector = [(0.0, 0.0)] * (2**N)

    # Define sqrt(1/2) for superposition amplitude
    amplitude = 1 / math.sqrt(2)

    # Set the amplitudes for the two basis states
    state_vector[index0] = (amplitude, 0.0)
    state_vector[index1] = (amplitude, 0.0)
    
    return state_vector

# Function to verify the superposition result
def verify_superposition(bits0, bits1):
    # Generate the superposition state vector
    state_vector = create_superposition(bits0, bits1)

    # Calculate expected indices
    N = len(bits0)
    index0 = int(bits0, 2)
    index1 = int(bits1, 2)
    expected = [(0.0, 0.0)] * (2**N)
    amplitude = 1 / math.sqrt(2)
    expected[index0] = (amplitude, 0.0)
    expected[index1] = (amplitude, 0.0)

    # Verify if the state vector matches the expected result
    if state_vector == expected:
        print('verified')
    else:
        print('Verification failed')
        print(f'Actual state vector: {state_vector}')
        print(f'Expected state vector: {expected}')

# Test the verify_superposition function
verify_superposition('110', '101')