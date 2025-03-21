'''
Problem id: 1002-A2
Statement: You are given N qubits (1 ≤ N ≤ 8) in zero state . You are also given a bitstring bits which describes a non-zero basis state on N qubits .

Your task is to generate a state which is an equal superposition of  and the given basis state:

You have to implement an operation which takes the following inputs:

The operation doesn't have an output; its "output" is the state in which it leaves the qubits.

An array of boolean values represents a basis state as follows: the i-th element of the array is true if the i-th qubit is in state , and false if it is in state . For example, array [true; false] describes 2-qubit state , and in this case the resulting state should be .

Your code should have the following signature:
Tags: *1300
'''

def superpose_qubits(bits):
    n = len(bits)
    
    # Build the base zero state as a string
    base_state = ''.join('0' for _ in range(n))
    
    # Build the target basis state per bits input
    target_basis_state = ''.join('1' if bit else '0' for bit in bits)
    
    # Return the formatted superposition representation
    superposition_state = f"(|{base_state}⟩ + |{target_basis_state}⟩) / √2"
    return superposition_state

# Verification function to test the solution

def verify_superpose_qubits():
    # Test inputs and expected outputs
    test_cases = [
        ([True, False], "(|00⟩ + |10⟩) / √2"),
        ([False, False, True], "(|000⟩ + |001⟩) / √2"),
        ([True, True, False, True], "(|0000⟩ + |1101⟩) / √2"),
        ([False], "(|0⟩ + |0⟩) / √2"),
        ([True], "(|0⟩ + |1⟩) / √2")
    ]

    for i, (input_bits, expected) in enumerate(test_cases):
        result = superpose_qubits(input_bits)
        if result == expected:
            print(f"Test case {i+1} verified: {result}")
        else:
            print(f"Test case {i+1} failed: expected {expected}, got {result}")

# Run the verification to test the function
verify_superpose_qubits()