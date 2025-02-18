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

def oracle_function(a, x):
    # Calculate the dot product (bitwise AND followed by modulo 2 sum)
    return sum(xi & ai for xi, ai in zip(x, a)) % 2


def test_oracle_function():
    # Define test parameters
    a = [1, 0, 1]
    x = [1, 0, 1]  # This is equivalent to the binary representation |101⟩
    
    # Calculate the expected output
    expected_parity = oracle_function(a, x)
    
    # The expected result is obtained from xor of x and a
    # In binary, 101 AND 101 = 101, and sum bits modulo 2
    # 1+0+1 = 2, 2 mod 2 = 0
    # So, expected parity should be 0
    expected_result = 0
    
    # Perform check
    if expected_parity == expected_result:
        print("verified")
    else:
        print("incorrect result")
        print(f"Expected parity: {expected_result}, but got: {expected_parity}")

# Run the test
test_oracle_function()