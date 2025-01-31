'''
Problem id: 325-A
Statement: You are given n rectangles. The corners of rectangles have integer coordinates and their edges are parallel to the Ox and Oy axes. The rectangles may touch each other, but they do not overlap (that is, there are no points that belong to the interior of more than one rectangle). 

Your task is to determine if the rectangles form a square. In other words, determine if the set of points inside or on the border of at least one rectangle is precisely equal to the set of points inside or on the border of some square.

The first line contains a single integer n (1 ≤ n ≤ 5). Next n lines contain four integers each, describing a single rectangle: x1, y1, x2, y2 (0 ≤ x1 < x2 ≤ 31400, 0 ≤ y1 < y2 ≤ 31400) — x1 and x2 are x-coordinates of the left and right edges of the rectangle, and y1 and y2 are y-coordinates of the bottom and top edges of the rectangle. 

No two rectangles overlap (that is, there are no points that belong to the interior of more than one rectangle).

In a single line print "YES", if the given rectangles form a square, or "NO" otherwise.
Tags: implementation,*1500
'''

def form_square(rectangles):
    if not rectangles:
        return "NO"
    
    # Step 1: Find the bounding box of all rectangles
    min_x = min(rect[0] for rect in rectangles)
    max_x = max(rect[2] for rect in rectangles)
    min_y = min(rect[1] for rect in rectangles)
    max_y = max(rect[3] for rect in rectangles)
    
    # Step 2: Check if the bounding box is square
    side_x = max_x - min_x
    side_y = max_y - min_y
    if side_x != side_y:
        return "NO"
    
    # Step 3: Calculate bounding box and rectangles area
    bounding_box_area = side_x * side_y
    total_rectangles_area = sum((rect[2] - rect[0]) * (rect[3] - rect[1]) for rect in rectangles)

    # Step 4: Validate if total area matches
    if total_rectangles_area == bounding_box_area:
        return "YES"
    else:
        return "NO"

# Test the function with a verification call
rectangles_test = [
    (0, 0, 2, 2),
    (2, 0, 4, 2),
    (0, 2, 4, 4)
]
expected_result = "YES"
actual_result = form_square(rectangles_test)

if actual_result == expected_result:
    print('verified')
else:
    print(f'incorrect result: expected {expected_result}, got {actual_result}')