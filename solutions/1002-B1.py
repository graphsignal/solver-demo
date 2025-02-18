'''
Problem id: 1002-B1
Statement: You are given N qubits (2 ≤ N ≤ 8) which are guaranteed to be in one of the two states:

Your task is to perform necessary operations and measurements to figure out which state it was and to return 0 if it was  state or 1 if it was W state. The state of the qubits after the operations does not matter.

You have to implement an operation which takes an array of N qubits as an input and returns an integer. 

Your code should have the following signature:
Tags: *1300
'''

def identify_state(qubits):
    # Count the number of 1s in the qubits array
    count_one = qubits.count(1)
    
    # Determine the state based on the count of 1s
    if count_one == 0:
        return 0  # all qubits are 0, meaning it's the "0" state
    elif count_one == 1:
        return 1  # exactly one qubit is 1, meaning it's the "W" state

# Verification call
# Test case: all qubits are 0
result1 = identify_state([0, 0, 0, 0])
expected1 = 0

# Test case: exactly one qubit is 1
result2 = identify_state([0, 1, 0, 0])
expected2 = 1

# Check results and print verification status
if result1 == expected1 and result2 == expected2:
    print('verified')
else:
    if result1 != expected1:
        print(f'Failure in test case 1: expected {expected1}, got {result1}')
    if result2 != expected2:
        print(f'Failure in test case 2: expected {expected2}, got {result2}')