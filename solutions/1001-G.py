'''
Problem id: 1001-G
Statement: Implement a quantum oracle on N qubits which implements a function f(x) = xk, i.e. the value of the function is the value of the k-th qubit.

For an explanation on how the quantum oracles work, see the tutorial blog post.

You have to implement an operation which takes the following inputs:

The operation doesn't have an output; the "output" of your solution is the state in which it left the qubits.

Your code should have the following signature:
Tags: *specialproblem,*1400
'''

def simulate_oracle(N, k, input_state):
    """
    Simulates a quantum oracle output by checking the value of k-th qubit in the input state.
    
    :param N: Number of qubits, should equal the length of input_state.
    :param k: Index of the qubit to be checked.
    :param input_state: A binary string representing state of qubits like '0001'.
    :return: The value of the k-th qubit (0 or 1).
    """
    if len(input_state) != N:
        raise ValueError("Length of input_state must be equal to N.")
    
    return input_state[k]

def verify_simulation():
    N = 4
    k = 2
    test_cases = {
        '0000': '0',
        '1111': '1',
        '1010': '1',
        '0101': '0'
    }
    all_verified = True
    for input_state, expected in test_cases.items():
        result = simulate_oracle(N, k, input_state)
        if result == expected:
            print(f'Test with input_state={input_state} verified.')
        else:
            print(f'Mismatch for input_state={input_state}: expected {expected}, got {result}.')
            all_verified = False

    if all_verified:
        print('All cases verified.')
    else:
        print('Some cases failed verification.')

verify_simulation()