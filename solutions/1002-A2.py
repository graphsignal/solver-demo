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

def generate_superposition(n, bits):
    """
    Prepare a superposition state of |00..0⟩ and the given basis state with a bitstring on N qubits.

    :param n: Number of qubits (int)
    :param bits: Bitstring (list of booleans) (true -> |1⟩, false -> |0⟩)
    :return: Tuple of strings representing the two states in superposition
    """
    zero_state = "|" + "0" * n + "⟩"
    basis_state = "|" + ''.join(['1' if bit else '0' for bit in bits]) + "⟩"
    return (zero_state, basis_state)

# Verification
def verify_superposition():
    n = 3
    bits = [True, False, True]  # Corresponds to |101⟩
    expected_state = ("|000⟩", "|101⟩")
    actual_state = generate_superposition(n, bits)
    if actual_state == expected_state:
        print("verified")
    else:
        print(f"Incorrect: expected {expected_state}, but got {actual_state}")

verify_superposition()