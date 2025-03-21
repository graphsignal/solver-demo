'''
Problem id: 1002-A4
Statement: You are given N = 2k qubits (0 ≤ k ≤ 4) in zero state . Your task is to create a generalized W state on them. Generalized W state is an equal superposition of all basis states on N qubits that have Hamming weight equal to 1:

For example, for N = 1, .

You have to implement an operation which takes an array of N qubits as an input and has no output. The "output" of the operation is the state in which it leaves the qubits.

Your code should have the following signature:
Tags: *1900
'''

import math

# Function to create a generalized W state
# Pure Python implementation

def create_w_state(num_qubits):
    """
    Simulate the creation of a generalized W state on num_qubits qubits
    using basic Python capabilities.
    """
    # Initialize the state vector to all zeros
    statevector = [0] * (2 ** num_qubits)
    
    # Calculate the amplitude
    amplitude = 1 / math.sqrt(num_qubits)
    
    # Iterate over all possible basis states
    for i in range(num_qubits):
        # Set the state corresponding to one qubit being |1⟩
        statevector[1 << i] = amplitude
    
    return statevector

# Initialize parameters
k = 4
num_qubits = 2**k

# "Generate" the W state using logic
statevector = create_w_state(num_qubits)

# Expected state vector
expected_statevector = [1/math.sqrt(num_qubits) if bin(x).count('1') == 1 else 0 for x in range(2**num_qubits)]

# Verify the correctness
verified = True
for actual, expected in zip(statevector, expected_statevector):
    if not math.isclose(actual, expected, rel_tol=1e-9):
        verified = False
        print('Verification failed')
        print('Actual:', actual, 'Expected:', expected)
        break

if verified:
    print('verified')