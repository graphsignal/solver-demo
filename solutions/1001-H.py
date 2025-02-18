'''
Problem id: 1001-H
Statement: Implement a quantum oracle on N qubits which implements the following function: , i.e., the value of the function is 1 if x has odd number of 1s, and 0 otherwise.

You have to implement an operation which takes the following inputs:

The operation doesn't have an output; the "output" of your solution is the state in which it left the qubits.

Your code should have the following signature:
Tags: *specialproblem,*1200
'''

def odd_parity_oracle(num_qubits, input_state):
    """
    Simulates a quantum operation that calculates if the number of 1s is odd among input_state.

    :param num_qubits: Total number of input qubits (excluding the ancilla).
    :param input_state: List representing the binary state of the qubits (e.g., [1, 1, 0]).
    :return: Parity result: 1 if odd, 0 if even.
    """
    # Initialize ancilla qubit as 0 (|0⟩ state)
    ancilla = 0
    
    # For each qubit in the input state, flip ancilla if qubit is 1
    for qubit in input_state:
        # Simulate CNOT: Flip ancilla for each qubit with value 1
        if qubit == 1:
            ancilla ^= 1  # XOR operation to flip ancilla

    return ancilla


# Verification function

def verify_oracle():
    # Test input: 3 qubits system in state "111", expecting an odd parity (result = 1)
    test_input = [1, 1, 1]
    expected_output = 1  # Odd number of 1s

    # Run the oracle
    result = odd_parity_oracle(3, test_input)
    
    # Verification check
    if result == expected_output:
        print("verified")
    else:
        print(f"Verification failed: Expected {expected_output}, but got {result}. Possible issue with oracle implementation.")


def main():
    verify_oracle()

main()