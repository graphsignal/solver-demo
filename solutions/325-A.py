'''
Problem id: 325-A
Statement: You are given n rectangles. The corners of rectangles have integer coordinates and their edges are parallel to the Ox and Oy axes. The rectangles may touch each other, but they do not overlap (that is, there are no points that belong to the interior of more than one rectangle). 

Your task is to determine if the rectangles form a square. In other words, determine if the set of points inside or on the border of at least one rectangle is precisely equal to the set of points inside or on the border of some square.

The first line contains a single integer n (1 ≤ n ≤ 5). Next n lines contain four integers each, describing a single rectangle: x1, y1, x2, y2 (0 ≤ x1 < x2 ≤ 31400, 0 ≤ y1 < y2 ≤ 31400) — x1 and x2 are x-coordinates of the left and right edges of the rectangle, and y1 and y2 are y-coordinates of the bottom and top edges of the rectangle. 

No two rectangles overlap (that is, there are no points that belong to the interior of more than one rectangle).

In a single line print "YES", if the given rectangles form a square, or "NO" otherwise.
Tags: implementation,*1500
'''

def does_form_square(n, rectangles):
    # Step 1: Calculate the total area of all rectangles
    total_area = 0
    for (x1, y1, x2, y2) in rectangles:
        total_area += (x2 - x1) * (y2 - y1)

    # Step 2: Determine the bounding box
    x_min = min(rect[0] for rect in rectangles)
    y_min = min(rect[1] for rect in rectangles)
    x_max = max(rect[2] for rect in rectangles)
    y_max = max(rect[3] for rect in rectangles)

    # Step 3: Check for square property
    width = x_max - x_min
    height = y_max - y_min

    # Step 4: Verify area match
    square_area = width * height

    if width == height and total_area == square_area:
        return "YES"
    else:
        return "NO"

# Verification function

def verify():
    # Test case where rectangles form a square
    rectangles = [
        (0, 0, 2, 2), 
        (2, 0, 4, 2), 
        (0, 2, 2, 4), 
        (2, 2, 4, 4),
    ]
    expected_result = "YES"
    actual_result = does_form_square(4, rectangles)
    if actual_result == expected_result:
        print("verified")
    else:
        print(f"Test failed: expected {expected_result}, but got {actual_result}")

    # Test case where rectangles do not form a square
    rectangles = [
        (0, 0, 2, 2),
        (2, 0, 3, 2),
    ]
    expected_result = "NO"
    actual_result = does_form_square(2, rectangles)
    if actual_result == expected_result:
        print("verified")
    else:
        print(f"Test failed: expected {expected_result}, but got {actual_result}")

verify()