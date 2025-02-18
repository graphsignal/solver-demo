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
    # Convert k degrees to radians
    theta_radians = k * (math.pi / 180)
    
    # Apply the rotation matrix
    x_prime = x * math.cos(theta_radians) - y * math.sin(theta_radians)
    y_prime = x * math.sin(theta_radians) + y * math.cos(theta_radians)

    return x_prime, y_prime

# Verification
# Rotate (1, 0) by 90 degrees counter-clockwise. Expected result: (0, 1)
expected_x_prime = 0
expected_y_prime = 1
rotated_x, rotated_y = rotate_point(90, 1, 0)

# Checking if the result is within a small tolerance
if math.isclose(rotated_x, expected_x_prime, abs_tol=0.1) and math.isclose(rotated_y, expected_y_prime, abs_tol=0.1):
    print('verified')
else:
    print(f'Error: Expected ({expected_x_prime}, {expected_y_prime}), got ({rotated_x}, {rotated_y})')