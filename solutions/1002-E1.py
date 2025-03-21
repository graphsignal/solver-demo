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

def oracle(x, y):
    # Example oracle for testing (not the real quantum oracle)
    # Let's assume a = [1, 0, 1]
    a = [1, 0, 1]
    dot_product = sum(a[i] * x[i] for i in range(len(a)))
    return dot_product % 2


def find_a(N, oracle):
    # Initialize an array to hold the solution a
    a = [0] * N

    # Query the oracle for each bit position
    for i in range(N):
        # Create a query vector with 1 in the i-th position and 0 elsewhere
        x = [0] * N
        x[i] = 1

        # Call oracle with this vector and y=0
        response = oracle(x, 0)

        # The response determines the value of a[i]
        a[i] = response

    return a

# Test the implemented function
expected = [1, 0, 1]
N = 3
result = find_a(N, oracle)

# Verification
if result == expected:
    print('verified')
else:
    print(f'Incorrect result. Actual: {result}, Expected: {expected}. This could happen if the implementation does not correctly deduce each bit of `a`.')