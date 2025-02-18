'''
Problem id: 1001-E
Statement: You are given two qubits which are guaranteed to be in one of the Bell states:

Your task is to perform necessary operations and measurements to figure out which state it was and to return the index of that state (0 for , 1 for  etc.). The state of the qubits after the operations does not matter.

You have to implement an operation which takes an array of two qubits as an input and returns an integer. 

Your code should have the following signature:
Tags: *specialproblem,*1600
'''

def identify_bell_state(qubits):
    # Apply a Hadamard gate to the first qubit
    # The operations simplify the mapping in classical logic
    # Simplified operations and expected classical measurement mapping after transformation
    x = qubits[0] ^ qubits[1]  # CNOT operation effect
    y = 1 if qubits[0] else 0  # Hadamard -> transform the initial |0> or |1>
    
    # Based on resulting state:
    # |00> -> 0  (|Φ+⟩)
    # |01> -> 1  (|Φ-⟩)
    # |10> -> 2  (|Ψ+⟩)
    # |11> -> 3  (|Ψ-⟩)
    return 2 * x + y

# Verification call
def verify_identify_bell_state():
    # Let's prepare classical states representing different Bell states invocations:
    test_states = [
        ([0, 0], 0),  # |Φ+⟩ expected index
        ([0, 1], 2),  # |Ψ+⟩ expected index
        ([1, 0], 1),  # |Φ-⟩ expected index
        ([1, 1], 3),  # |Ψ-⟩ expected index
    ]
    
    for test_qubits, expected_index in test_states:
        result_index = identify_bell_state(test_qubits)
        if result_index == expected_index:
            print('verified')
        else:
            print(f'incorrect: expected {expected_index}, got {result_index}')   

verify_identify_bell_state()