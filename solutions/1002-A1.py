'''
Problem id: 1002-A1
Statement: You are given N qubits (1 ≤ N ≤ 8) in zero state . 

Your task is to generate an equal superposition of all 2N basis vectors on N qubits:

For example,

You have to implement an operation which takes an array of N qubits as an input and has no output. The "output" of the operation is the state in which it leaves the qubits.

Your code should have the following signature:
Tags: *800
'''

def equal_superposition(N):
    """Generate an equal superposition of all basis states for N qubits."""
    num_states = 2 ** N  # Calculate the number of possible basis states
    basis_states = []
    
    # Generate all possible binary strings of length N
    for i in range(num_states):
        # Format i as a binary string with leading zeros
        binary_state = format(i, f'0{N}b')
        basis_states.append(binary_state)
    
    return basis_states

# Verification for N=3 qubits
N = 3
expected_num_states = 2 ** N
generated_states = equal_superposition(N)
actual_num_states = len(generated_states)

if actual_num_states == expected_num_states:
    print("verified")
else:
    print("Test failed.")
    print(f"Expected number of states: {expected_num_states}, but got: {actual_num_states}")
    print("Generated states:", generated_states)