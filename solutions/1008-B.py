'''
Problem id: 1008-B
Statement: There are $$$n$$$ rectangles in a row. You can either turn each rectangle by $$$90$$$ degrees or leave it as it is. If you turn a rectangle, its width will be height, and its height will be width. Notice that you can turn any number of rectangles, you also can turn all or none of them. You can not change the order of the rectangles.

Find out if there is a way to make the rectangles go in order of non-ascending height. In other words, after all the turns, a height of every rectangle has to be not greater than the height of the previous rectangle (if it is such). 

The first line contains a single integer $$$n$$$ ($$$1 \leq n \leq 10^5$$$) — the number of rectangles.

Each of the next $$$n$$$ lines contains two integers $$$w_i$$$ and $$$h_i$$$ ($$$1 \leq w_i, h_i \leq 10^9$$$) — the width and the height of the $$$i$$$-th rectangle.

Print "YES" (without quotes) if there is a way to make the rectangles go in order of non-ascending height, otherwise print "NO".

You can print each letter in any case (upper or lower).

In the first test, you can rotate the second and the third rectangles so that the heights will be [4, 4, 3].

In the second test, there is no way the second rectangle will be not higher than the first one.
Tags: greedy,sortings,*1000
'''

def can_arrange_rectangles(n, rectangles):
    prev_height = float('inf')
    
    for index in range(n):
        w, h = rectangles[index]
        if min(w, h) <= prev_height:
            # Choose the tallest possible without violating the height condition
            prev_height = min(prev_height, max(w, h))
        else:
            return "NO"
    
    return "YES"

# Verification
# Test example 1 (Expected: YES)
rectangles1 = [(4, 3), (3, 5), (3, 2)]
expected1 = "YES"

# Test example 2 (Expected: NO)
rectangles2 = [(5, 4), (5, 6), (3, 2)]
expected2 = "NO"

# Run first test
result1 = can_arrange_rectangles(len(rectangles1), rectangles1)
if result1 == expected1:
    print('Test 1 verified')
else:
    print(f'Test 1 failed: Expected {expected1}, but got {result1}')

# Run second test
result2 = can_arrange_rectangles(len(rectangles2), rectangles2)
if result2 == expected2:
    print('Test 2 verified')
else:
    print(f'Test 2 failed: Expected {expected2}, but got {result2}')