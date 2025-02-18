'''
Problem id: 325-A
Statement: You are given n rectangles. The corners of rectangles have integer coordinates and their edges are parallel to the Ox and Oy axes. The rectangles may touch each other, but they do not overlap (that is, there are no points that belong to the interior of more than one rectangle). 

Your task is to determine if the rectangles form a square. In other words, determine if the set of points inside or on the border of at least one rectangle is precisely equal to the set of points inside or on the border of some square.

The first line contains a single integer n (1 ≤ n ≤ 5). Next n lines contain four integers each, describing a single rectangle: x1, y1, x2, y2 (0 ≤ x1 < x2 ≤ 31400, 0 ≤ y1 < y2 ≤ 31400) — x1 and x2 are x-coordinates of the left and right edges of the rectangle, and y1 and y2 are y-coordinates of the bottom and top edges of the rectangle. 

No two rectangles overlap (that is, there are no points that belong to the interior of more than one rectangle).

In a single line print "YES", if the given rectangles form a square, or "NO" otherwise.
Tags: implementation,*1500
'''

def check_if_rectangles_form_square(rectangles):
    if not rectangles:
        return "NO"
    
    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')
    total_area = 0

    for x1, y1, x2, y2 in rectangles:
        min_x = min(min_x, x1)
        min_y = min(min_y, y1)
        max_x = max(max_x, x2)
        max_y = max(max_y, y2)
        total_area += (x2 - x1) * (y2 - y1)

    # Calculate the side length of the bounding square
    side_length = max_x - min_x

    # Check if bounding box is a square
    if side_length == (max_y - min_y):
        # Calculate the area of the bounding box assumed square
        if total_area == side_length * side_length:
            return "YES"

    return "NO"

# Verification function

def verify_solution(test_case, expected):
    result = check_if_rectangles_form_square(test_case)
    if result == expected:
        print("verified")
    else:
        print(f"Incorrect: Expected {expected}, but got {result}")

# Test case
rectangles_test = [
    (0, 0, 2, 2), 
    (0, 2, 2, 4), 
    (2, 0, 4, 2), 
    (2, 2, 4, 4)
]

# This should form a perfect 4x4 square
verify_solution(rectangles_test, "YES")