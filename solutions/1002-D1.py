'''
Problem id: 1002-D1
Statement: Implement a quantum oracle on N qubits which implements the following function: , where  (a vector of N integers, each of which can be 0 or 1).

For an explanation on how this type of quantum oracles works, see Introduction to quantum oracles.

You have to implement an operation which takes the following inputs:

The operation doesn't have an output; its "output" is the state in which it leaves the qubits.

Your code should have the following signature:
Tags: *1200
'''

def quantum_oracle_simulation_and_verification(a):
    n = len(a)

    def f(x):
        # Compute the dot product mod 2 between x and a
        return sum(int(x[i]) * a[i] for i in range(n)) % 2

    # Check for all possible 2^n input states represented by binary strings
    for x in range(2 ** n):
        # Convert x to binary string with leading zeros
        x_bin = f"{x:0{n}b}"
        actual_result = f(x_bin)
        expected_result = sum(int(x_bin[i]) * a[i] for i in range(n)) % 2
        if actual_result != expected_result:
            print(f"Verification failed for x = {x_bin}: expected {expected_result}, got {actual_result}")
            return False

    print("verified")
    return True

# Example vector a for testing
example_a = [1, 0, 1]

# Run verification
quantum_oracle_simulation_and_verification(example_a)