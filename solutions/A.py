def forms_square(rectangles):
    # Step 3 and 4: Calculate total area and determine bounding box
    total_area = 0
    x_min = float('inf')
    x_max = float('-inf')
    y_min = float('inf')
    y_max = float('-inf')
    
    for x1, y1, x2, y2 in rectangles:
        # Calculate the area of each rectangle
        total_area += (x2 - x1) * (y2 - y1)
        # Update the bounding box coordinates
        x_min = min(x_min, x1)
        x_max = max(x_max, x2)
        y_min = min(y_min, y1)
        y_max = max(y_max, y2)

    # Calculate width and height of the bounding box
    width = x_max - x_min
    height = y_max - y_min

    # Check if the bounding box is a square and its area equals total_area
    if width == height and width * height == total_area:
        return "YES"
    else:
        return "NO"

# Verification code
rectangles = [
    (0, 0, 2, 2),  # Rectangle 1
    (2, 0, 4, 2),  # Rectangle 2
    (0, 2, 2, 4),  # Rectangle 3
    (2, 2, 4, 4)   # Rectangle 4
]

# These rectangles form a square (4x4 square), should return "YES"
expected_output = "YES"

# Checking the solution
result = forms_square(rectangles)

if result == expected_output:
    print('correct')
else:
    print('incorrect')