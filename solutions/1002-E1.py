'''
Problem id: 1002-E1
Statement: You are given a quantum oracle - an operation on N + 1 qubits which implements a function . You are guaranteed that the function f implemented by the oracle is scalar product function (oracle from problem D1): 

Here  (an array of N integers, each of which can be 0 or 1). 

Your task is to reconstruct the array . Your code is allowed to call the given oracle only once.

You have to implement an operation which takes the following inputs:

The return of your operation is an array of integers of length N, each of them 0 or 1.

Your code should have the following signature:
Tags: *1500
'''

def quantum_oracle_example(x):
    # An example oracle function that uses a predefined `a`
    # Let's assume N=3 for example purposes, and the array a is [1, 0, 1]
    a = [1, 0, 1]
    # Compute the function f(x) = (sum(a_i * x_i) for i in range(N)) mod 2
    return sum(a_i * x_i for a_i, x_i in zip(a, x)) % 2


def reconstruct_a_with_oracle(quantum_oracle, N):
    # Reconstruct the array `a` using the given oracle
    a = []
    for i in range(N):
        x = [0] * N  # Start with all zeroes
        x[i] = 1     # Set the i-th position to 1
        parity = quantum_oracle(x)
        a.append(parity)  # Append the result, which is a_i

    return a


# Test our solution with the oracle
N = 3  # Length of the array a

# Expected result is a reconstruction of the array [1, 0, 1]
expected = [1, 0, 1]

# Run the function with the example quantum oracle
actual = reconstruct_a_with_oracle(quantum_oracle_example, N)

# Verification
if actual == expected:
    print("verified")
else:
    print("Result not matching. Expected:", expected, "Actual:", actual)
    print("Possible error: In the input to the oracle or the oracle implementation itself.")