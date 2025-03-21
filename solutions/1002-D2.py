'''
Problem id: 1002-D2
Statement: Implement a quantum oracle on N qubits which implements the following function: 

Here  (a vector of N integers, each of which can be 0 or 1), and  is a vector of N 1s.

For an explanation on how this type of quantum oracles works, see Introduction to quantum oracles.

You have to implement an operation which takes the following inputs:

The operation doesn't have an output; its "output" is the state in which it leaves the qubits.

Your code should have the following signature:
Tags: *1300
'''

def classical_oracle_simulation(n, a):
    """
    Simulates the oracle by flipping the sign of the amplitude for state |a>.
    """
    state_space = [(bin(i)[2:].zfill(n), 1) for i in range(2**n)]  # Each state initialization in binary
    
    # Simulate phase flip for state matching a
    for i, (state, amplitude) in enumerate(state_space):
        if all(int(state[j]) == a[j] for j in range(n)):
            state_space[i] = (state, -amplitude)
    
    return state_space

def verify_oracle():
    n = 3  # Number of bits
    a = [1, 0, 1]  # State to flip the phase
    
    result = classical_oracle_simulation(n, a)
    
    expected_outcome = [(state, -amp) if state == ''.join(map(str, a)) else (state, amp)
                        for (state, amp) in [(bin(i)[2:].zfill(n), 1) for i in range(2**n)]]

    if result == expected_outcome:
        print('verified')
    else:
        print('Oracle verification failed.')
        print('Expected:', expected_outcome)
        print('Actual:', result)

# Run the verification
verify_oracle()