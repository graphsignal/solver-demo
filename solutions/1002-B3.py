'''
Problem id: 1002-B3
Statement: You are given 2 qubits which are guaranteed to be in one of the four orthogonal states:

Your task is to perform necessary operations and measurements to figure out which state it was and to return the index of that state (0 for , 1 for  etc.). The state of the qubits after the operations does not matter.

You have to implement an operation which takes an array of 2 qubits as an input and returns an integer. 

Your code should have the following signature:
Tags: *1600
'''

def identify_state(qubits):
    # Measure the first qubit, result is either 0 or 1
    result_0 = measure(qubits[0])  # 0 for |0⟩, 1 for |1⟩
    
    # Measure the second qubit, result is either 0 or 1
    result_1 = measure(qubits[1])  # 0 for |0⟩, 1 for |1⟩
    
    # Combine the results into a binary number
    index = (result_0 << 1) | result_1  # Binary to integer conversion
    
    return index

# This is a placeholder function which simulates measurement in the |0⟩,|1⟩ basis
def measure(qubit):
    # Assume qubit values are either '0' or '1' as strings for this mockup
    return int(qubit)  # Convert '0' or '1' to 0 or 1

# Verification Calls
# Test case: qubits are in the |00⟩ state
actual_index = identify_state(['0', '0'])
expected_index = 0

if actual_index == expected_index:
    print('verified')
else:
    print(f'Incorrect. Actual: {actual_index}, Expected: {expected_index}')

# Test case: qubits are in the |01⟩ state
actual_index = identify_state(['0', '1'])
expected_index = 1

if actual_index == expected_index:
    print('verified')
else:
    print(f'Incorrect. Actual: {actual_index}, Expected: {expected_index}')

# Test case: qubits are in the |10⟩ state
actual_index = identify_state(['1', '0'])
expected_index = 2

if actual_index == expected_index:
    print('verified')
else:
    print(f'Incorrect. Actual: {actual_index}, Expected: {expected_index}')

# Test case: qubits are in the |11⟩ state
actual_index = identify_state(['1', '1'])
expected_index = 3

if actual_index == expected_index:
    print('verified')
else:
    print(f'Incorrect. Actual: {actual_index}, Expected: {expected_index}')