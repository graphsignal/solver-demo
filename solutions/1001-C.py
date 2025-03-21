'''
Problem id: 1001-C
Statement: You are given N qubits (1 ≤ N ≤ 8) in zero state . Your task is to create Greenberger–Horne–Zeilinger (GHZ) state on them:

Note that for N = 1 and N = 2 GHZ state becomes states  and  from the previous tasks, respectively.

You have to implement an operation which takes an array of N qubits as an input and has no output. The "output" of your solution is the state in which it left the input qubits.

Your code should have the following signature:
Tags: *specialproblem,*1400
'''

def generate_ghz_state_vector(n):
    # Create an empty state list initialized to zero
    state_vector = [0] * (2**n)
    # Set the initial and final states to 1/sqrt(2) to simulate the GHZ state
    state_vector[0] = 1
    state_vector[-1] = 1
    return state_vector


def verify_ghz_state_vector(actual_state_vector, n):
    # Build the expected state vector
    expected_state_vector = [0] * (2**n)
    expected_state_vector[0] = 1
    expected_state_vector[-1] = 1
    # Compare the actual and expected states
    if actual_state_vector == expected_state_vector:
        return True, 'verified'
    else:
        return False, f'actual: {actual_state_vector}, expected: {expected_state_vector}'


# Example usage
n_qubits = 3
actual_state_vector = generate_ghz_state_vector(n_qubits)
verified, message = verify_ghz_state_vector(actual_state_vector, n_qubits)
print(message)