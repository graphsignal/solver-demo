'''
Problem id: 1001-C
Statement: You are given N qubits (1 ≤ N ≤ 8) in zero state . Your task is to create Greenberger–Horne–Zeilinger (GHZ) state on them:

Note that for N = 1 and N = 2 GHZ state becomes states  and  from the previous tasks, respectively.

You have to implement an operation which takes an array of N qubits as an input and has no output. The "output" of your solution is the state in which it left the input qubits.

Your code should have the following signature:
Tags: *specialproblem,*1400
'''

def create_ghz_state(N):
    # Generate GHZ state as a list of strings
    ghz_state = []
    zeroes = '0' * N
    ones = '1' * N
    ghz_state.append(zeroes)
    ghz_state.append(ones)
    return ghz_state


def verify_ghz_state(N):
    expected_zeroes = '0' * N
    expected_ones = '1' * N
    expected_state = [expected_zeroes, expected_ones]
    
    generated_state = create_ghz_state(N)
    
    if sorted(generated_state) == sorted(expected_state):
        print("verified")
    else:
        print(f"Expected state: {expected_state} but got {generated_state}")

# Verification call for N = 3
verify_ghz_state(3)