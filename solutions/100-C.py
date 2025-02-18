'''
Problem id: 100-C
Statement: Bijan is new to programming. He learned recently that programmers do not code every bit of their apps from scratch.

For example they never write a code to sum two integers, because their languages have the ability to do the sum. But can they use it? Can an experienced coder who has attended more than 100 contests, sum two integers?

Bijan is not sure about this. What's your opinion?

You are given two integers a and b, one per line (1 ≤ a, b < 10500). These numbers will not have any leading zeros.

Write sum of the two integers. Do not put any leading zeros.
Tags: *specialproblem,implementation,*1400
'''

def solution():
    # Provided test case input
    a = "12345678901234567890"
    b = "98765432109876543210"

    # Convert inputs to integers
    int_a = int(a)
    int_b = int(b)

    # Compute the sum of the two integers
    result = int_a + int_b
    
    return result

# Invoke the solution function and verify the output
expected_result = 111111111011111111100
actual_result = solution()

if actual_result == expected_result:
    print('verified')
else:
    print(f'Incorrect result. Expected: {expected_result}, but got: {actual_result}')