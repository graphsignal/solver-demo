'''
Problem id: 1002-B1
Statement: You are given N qubits (2 ≤ N ≤ 8) which are guaranteed to be in one of the two states:

Your task is to perform necessary operations and measurements to figure out which state it was and to return 0 if it was  state or 1 if it was W state. The state of the qubits after the operations does not matter.

You have to implement an operation which takes an array of N qubits as an input and returns an integer. 

Your code should have the following signature:
Tags: *1300
'''

def identify_qubit_state(qubits):
    # Measure the qubits
    # Note: Assuming 'qubits' is a list of integers where each can be 0 or 1 after measurement
    count_of_ones = sum(qubits)
    
    # Determine the state based on the count of ones
    if count_of_ones == 0:
        return 0  # Indicating the |0> state
    elif count_of_ones == 1:
        return 1  # Indicating the |W> state
    else:
        # This should not happen with guaranteed input, included for robustness
        raise ValueError("Invalid qubit state detected")

# Test cases
# 1. All qubits are 0s, indicating state |0>
test_0 = [0, 0, 0]   # For N=3, should return 0
result_0 = identify_qubit_state(test_0)
expected_0 = 0

# Verification
if result_0 == expected_0:
    print('Test case 0 verified')
else:
    print(f'Test case 0 failed: got {result_0}, expected {expected_0}')

# 2. Exactly one qubit is 1, indicating state |W>
test_1 = [0, 1, 0]   # For N=3, should return 1
result_1 = identify_qubit_state(test_1)
expected_1 = 1

# Verification
if result_1 == expected_1:
    print('Test case 1 verified')
else:
    print(f'Test case 1 failed: got {result_1}, expected {expected_1}')

# 3. Another configuration for |W>
# Only 1 should be in a different position
test_2 = [1, 0, 0]   # For N=3, should return 1
result_2 = identify_qubit_state(test_2)
expected_2 = 1

# Verification
if result_2 == expected_2:
    print('Test case 2 verified')
else:
    print(f'Test case 2 failed: got {result_2}, expected {expected_2}')