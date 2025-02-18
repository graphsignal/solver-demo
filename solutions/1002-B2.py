'''
Problem id: 1002-B2
Statement: You are given N qubits (2 ≤ N ≤ 8) which are guaranteed to be in one of the two states:

Your task is to perform necessary operations and measurements to figure out which state it was and to return 0 if it was GHZ state or 1 if it was W state. The state of the qubits after the operations does not matter.

You have to implement an operation which takes an array of N qubits as an input and returns an integer. 

Your code should have the following signature:
Tags: *1600
'''

def determine_state(qubits):
    num_ones = sum(qubits)  # Sum the ones from a "measurement" of qubits
    if num_ones == 0 or num_ones == len(qubits):
        return 0  # GHZ state is detected
    elif num_ones == 1:
        return 1  # W state is detected
    else:
        raise ValueError("This situation should not happen based on the problem description.")

# Verification call
# Test with a GHZ state example (all qubits are 0)
test_qubits_ghz = [0, 0, 0, 0]  # Expected to return 0 (GHZ state)
result_ghz = determine_state(test_qubits_ghz)

# Test with a W state example (exactly one qubit is 1)
test_qubits_w = [1, 0, 0, 0]  # Expected to return 1 (W state)
result_w = determine_state(test_qubits_w)

# Check results and print verification
verified_ghz = (result_ghz == 0)
verified_w = (result_w == 1)

if verified_ghz and verified_w:
    print('verified')
else:
    if not verified_ghz:
        print(f'Incorrect for GHZ test. Result: {result_ghz}, Expected: 0')
    if not verified_w:
        print(f'Incorrect for W test. Result: {result_w}, Expected: 1')