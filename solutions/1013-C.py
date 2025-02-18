'''
Problem id: 1013-C
Statement: Pavel made a photo of his favourite stars in the sky. His camera takes a photo of all points of the sky that belong to some rectangle with sides parallel to the coordinate axes.

Strictly speaking, it makes a photo of all points with coordinates $$$(x, y)$$$, such that $$$x_1 \leq x \leq x_2$$$ and $$$y_1 \leq y \leq y_2$$$, where $$$(x_1, y_1)$$$ and $$$(x_2, y_2)$$$ are coordinates of the left bottom and the right top corners of the rectangle being photographed. The area of this rectangle can be zero.

After taking the photo, Pavel wrote down coordinates of $$$n$$$ of his favourite stars which appeared in the photo. These points are not necessarily distinct, there can be multiple stars in the same point of the sky.

Pavel has lost his camera recently and wants to buy a similar one. Specifically, he wants to know the dimensions of the photo he took earlier. Unfortunately, the photo is also lost. His notes are also of not much help; numbers are written in random order all over his notepad, so it's impossible to tell which numbers specify coordinates of which points.

Pavel asked you to help him to determine what are the possible dimensions of the photo according to his notes. As there are multiple possible answers, find the dimensions with the minimal possible area of the rectangle.

The first line of the input contains an only integer $$$n$$$ ($$$1 \leq n \leq 100\,000$$$), the number of points in Pavel's records.

The second line contains $$$2 \cdot n$$$ integers $$$a_1$$$, $$$a_2$$$, ..., $$$a_{2 \cdot n}$$$ ($$$1 \leq a_i \leq 10^9$$$), coordinates, written by Pavel in some order.

Print the only integer, the minimal area of the rectangle which could have contained all points from Pavel's records.

In the first sample stars in Pavel's records can be $$$(1, 3)$$$, $$$(1, 3)$$$, $$$(2, 3)$$$, $$$(2, 4)$$$. In this case, the minimal area of the rectangle, which contains all these points is $$$1$$$ (rectangle with corners at $$$(1, 3)$$$ and $$$(2, 4)$$$).
Tags: implementation,math,*1500
'''

def minimal_rectangle_area(n, coordinates):
    # Step 2: Sort the coordinates
    coordinates.sort()
    
    # Step 3-4: Assign x and y
    x_coords = coordinates[:n]
    y_coords = coordinates[n:]
    
    # Calculate dimensions
    x_min = min(x_coords)
    x_max = max(x_coords)
    y_min = min(y_coords)
    y_max = max(y_coords)
    
    # Step 5: Calculate the area
    width = x_max - x_min
    height = y_max - y_min
    area = width * height
    
    return area

# Verification Test
# Test input
n_test = 4
coordinates_test = [1, 3, 1, 3, 2, 3, 2, 4]
expected_output = 1  # As explained in the example

# Actual output
actual_output = minimal_rectangle_area(n_test, coordinates_test)

# Verify
if actual_output == expected_output:
    print("verified")
else:
    print(f"incorrect, expected {expected_output} but got {actual_output}")