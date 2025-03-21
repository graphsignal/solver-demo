'''
Problem id: 100-I
Statement: Ehsan loves geometry! Especially he likes to rotate points!

Given a point in the plane, Ehsan likes to rotate it by k degrees (counter-clockwise), around the origin. What is the result of this rotation?

A single integer k (0 ≤ k < 360) is given in the first line. Two integer numbers x and y are given in the second line ( - 1390 ≤ x, y ≤ 1390).

Write two numbers. The result of the rotation. Your answer must have a relative error less than 10 - 1.
Tags: *specialproblem,geometry,math,*1500
'''

import math

def rotate_point(k, x, y):
    # Convert degrees to radians
    radians = k * math.pi / 180
    
    # Calculate the new coordinates using rotation formulas
    x_new = x * math.cos(radians) - y * math.sin(radians)
    y_new = x * math.sin(radians) + y * math.cos(radians)
    
    return (x_new, y_new)

# Test the function with a verification step
# Test case: Rotate 90 degrees counter-clockwise
k_test = 90
x_test, y_test = 1, 0 # point on x-axis
expected_result = (0, 1) # expected point on y-axis

# Call the solution function
actual_result = rotate_point(k_test, x_test, y_test)

# Verify the result
relative_error_allowance = 0.1

x_error = abs(actual_result[0] - expected_result[0])
y_error = abs(actual_result[1] - expected_result[1])

if x_error < relative_error_allowance and y_error < relative_error_allowance:
    print('verified')
else:
    print(f'Incorrect result. Actual: {actual_result}, Expected: {expected_result}')