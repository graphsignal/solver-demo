'''
Problem id: 1002-A1
Statement: You are given N qubits (1 ≤ N ≤ 8) in zero state . 

Your task is to generate an equal superposition of all 2N basis vectors on N qubits:

For example,

You have to implement an operation which takes an array of N qubits as an input and has no output. The "output" of the operation is the state in which it leaves the qubits.

Your code should have the following signature:
Tags: *800
'''

import math

def superposition(n):
    # Start with a basis state |0...0⟩
    num_states = 2 ** n
    state = [0.0] * num_states
    state[0] = 1.0  # All qubits initialized to |0...0>

    # Apply Hadamard transform
    magnitude = math.sqrt(num_states)
    new_state = [1.0 / magnitude] * num_states

    return new_state


def verify_superposition(n):
    # Calculate expected amplitude: 1/sqrt(2^N)
    expected_amplitude = 1 / math.sqrt(2 ** n)
    state = superposition(n)
    
    # Check if each amplitude in the state is as expected
    for amplitude in state:
        if not math.isclose(amplitude, expected_amplitude, rel_tol=1e-9):
            print('Verification failed. Found amplitude:', amplitude, 'Expected:', expected_amplitude)
            return
    
    # Check normalization condition (sum of squares of amplitudes == 1)
    norm = sum(x ** 2 for x in state)
    if not math.isclose(norm, 1.0, rel_tol=1e-9):
        print('Verification failed. Sum of amplitude squares:', norm)
        return
    
    print('verified')

# Test the function with 3 qubits
verify_superposition(3)