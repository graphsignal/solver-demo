'''
Problem id: 100-C
Statement: Bijan is new to programming. He learned recently that programmers do not code every bit of their apps from scratch.

For example they never write a code to sum two integers, because their languages have the ability to do the sum. But can they use it? Can an experienced coder who has attended more than 100 contests, sum two integers?

Bijan is not sure about this. What's your opinion?

You are given two integers a and b, one per line (1 ≤ a, b < 10500). These numbers will not have any leading zeros.

Write sum of the two integers. Do not put any leading zeros.
Tags: *specialproblem,implementation,*1400
'''

def solution(a: str, b: str) -> str:
    # Convert strings to integers, sum them, and convert the result back to string.
    return str(int(a) + int(b))

# Test the solution function with a test case
# Test case: let a be a large number within the given constraint, and b another large number.
a = '1234567890123456789012345678901234567890'
b = '9876543210987654321098765432109876543210'

# Expected output should be the sum of the two large numbers:
expected_result = '11111111101111111110111111111011111111100'

# Call the solution function
test_result = solution(a, b)

# Verification
if test_result == expected_result:
    print('verified')
else:
    print(f"Incorrect calculation. Actual: {test_result}, Expected: {expected_result}")