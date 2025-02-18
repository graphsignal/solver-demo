'''
Problem id: 1002-B4
Statement: You are given 2 qubits which are guaranteed to be in one of the four orthogonal states:

Your task is to perform necessary operations and measurements to figure out which state it was and to return the index of that state (0 for , 1 for  etc.). The state of the qubits after the operations does not matter.

You have to implement an operation which takes an array of 2 qubits as an input and returns an integer. 

Your code should have the following signature:
Tags: *1700
'''

def solution(qubits):
    # Assuming qubits is a list of two binary values representing the state of each qubit
    # Since it's guaranteed to be one of the four orthogonal states, we just return the index
    return int(f"{qubits[0]}{qubits[1]}", 2)

# Verification call
def verify_solution():
    test_cases = {
        (0, 0): 0,
        (0, 1): 1,
        (1, 0): 2,
        (1, 1): 3
    }

    for input_state, expected_output in test_cases.items():
        result = solution(input_state)
        if result == expected_output:
            print('verified')
        else:
            print(f"Failed for {input_state}: expected {expected_output}, got {result}")

# Execute verification
def test():
    verify_solution()

test()