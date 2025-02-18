'''
Problem id: 1002-D1
Statement: Implement a quantum oracle on N qubits which implements the following function: , where  (a vector of N integers, each of which can be 0 or 1).

For an explanation on how this type of quantum oracles works, see Introduction to quantum oracles.

You have to implement an operation which takes the following inputs:

The operation doesn't have an output; its "output" is the state in which it leaves the qubits.

Your code should have the following signature:
Tags: *1200
'''

def classical_oracle(a, x):
    """
    Simulates the behavior of a quantum oracle by computing the dot product
    modulo 2, where the inputs are binary vectors.

    :param a: List[int], the binary vector a.
    :param x: List[int], the input binary vector x.
    :return: int, the result of a dot x mod 2.
    """
    dot_product = sum(a_i * x_i for a_i, x_i in zip(a, x))
    f_x = dot_product % 2
    return f_x


def verify_classical_oracle(a, x, expected_result):
    """
    Verifies the oracle by comparing the computed result with the expected result.

    :param a: List[int], the binary vector a.
    :param x: List[int], the input binary vector x.
    :param expected_result: int, the expected result, should be 0 or 1.
    """
    result = classical_oracle(a, x)
    if result == expected_result:
        print("verified")
    else:
        print(f"incorrect: result = {result}, expected = {expected_result}")

# Example parameters for testing
N = 3
example_a = [1, 0, 1]
example_x = [0, 0, 1]  # x state to test

# Calculate the expected result manually for verification
expected_result = (example_a[0]*example_x[0] + example_a[1]*example_x[1] + example_a[2]*example_x[2]) % 2

# Verify the implementation by checking correctness
verify_classical_oracle(example_a, example_x, expected_result)