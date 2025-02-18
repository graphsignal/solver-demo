'''
Problem id: 1002-D3
Statement: Implement a quantum oracle on 3 qubits which implements a majority function. Majority function on 3-bit vectors is defined as follows:  if vector  has two or three 1s, and 0 if it has zero or one 1s.

For an explanation on how this type of quantum oracles works, see Introduction to quantum oracles.

You have to implement an operation which takes the following inputs:

The operation doesn't have an output; its "output" is the state in which it leaves the qubits.

Your code should have the following signature:
Tags: *1600
'''

def majority_function(a, b, c):
    """Simulates the majority function of three bits."""
    return 1 if a + b + c >= 2 else 0


def test_majority_function():
    # Define all possible input states and their expected results
    test_cases = {
        (0, 0, 0): 0,
        (0, 0, 1): 0,
        (0, 1, 0): 0,
        (0, 1, 1): 1,
        (1, 0, 0): 0,
        (1, 0, 1): 1,
        (1, 1, 0): 1,
        (1, 1, 1): 1
    }
    
    # Verify each test case
    for (a, b, c), expected in test_cases.items():
        result = majority_function(a, b, c)
        if result == expected:
            print(f"Test with inputs ({a}, {b}, {c}) passed: Output: {result}, Expected: {expected} - verified")
        else:
            print(f"Test with inputs ({a}, {b}, {c}) failed: Output: {result}, Expected: {expected} - Reason: Incorrect result")

# Run the test function
test_majority_function()