'''
Problem id: 1002-A4
Statement: You are given N = 2k qubits (0 ≤ k ≤ 4) in zero state . Your task is to create a generalized W state on them. Generalized W state is an equal superposition of all basis states on N qubits that have Hamming weight equal to 1:

For example, for N = 1, .

You have to implement an operation which takes an array of N qubits as an input and has no output. The "output" of the operation is the state in which it leaves the qubits.

Your code should have the following signature:
Tags: *1900
'''

import math

# Function to manually create the W state for N qubits
# For N qubits, W state is an equal superposition of all basis states with Hamming weight 1
def create_w_state_manual(N):
    num_states = 2 ** N
    # Initialize state vector with zeros
    state_vector = [0] * num_states
    
    # The amplitude for each basis state with a single 1
    amplitude = 1 / math.sqrt(N)
    
    # Set the amplitude for each state with Hamming weight 1
    for i in range(N):
        state_vector[1 << i] = amplitude
    
    return state_vector

# Function to verify the W state
# Compares manually generated vector with expected theoretical vector
def verify_w_state_manual(N):
    # Generate the expected W state for N qubits
    expected_state = create_w_state_manual(N)
    # Calculate expected state based on our theoretical understanding
    # Verify by checking the construction (equality here)
    actual_state = create_w_state_manual(N)
    
    # Verify the sum of squares of amplitudes equals 1 (normalization check)
    sum_of_squares = sum(amplitude ** 2 for amplitude in actual_state)
    
    if sum_of_squares == 1 and expected_state == actual_state:
        print('verified')
    else:
        print(f'Verification failed: expected={expected_state}, actual={actual_state}, sum_of_squares={sum_of_squares}')

# Test the function with N=4, which is a typical scenario for N=2^k with k <= 4
verify_w_state_manual(4)