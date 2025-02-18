'''
Problem id: 101-C
Statement: At a geometry lesson Gerald was given a task: to get vector B out of vector A. Besides, the teacher permitted him to perform the following operations with vector А:

Operations could be performed in any order any number of times.

Can Gerald cope with the task?

The first line contains integers x1 и y1 — the coordinates of the vector A ( - 108 ≤ x1, y1 ≤ 108). The second and the third line contain in the similar manner vectors B and C (their coordinates are integers; their absolute value does not exceed 108).

Print "YES" (without the quotes) if it is possible to get vector B using the given operations. Otherwise print "NO" (without the quotes).
Tags: implementation,math,*2000
'''

def can_transform(x1, y1, x2, y2, x3, y3):
    dx = x2 - x1
    dy = y2 - y1

    if x3 == 0 and y3 == 0:
        return x1 == x2 and y1 == y2
    if x3 == 0:
        return dx == 0 and dy % y3 == 0
    if y3 == 0:
        return dy == 0 and dx % x3 == 0
    return (dx % x3 == 0) and (dy % y3 == 0) and (dx // x3 == dy // y3)

# Test the function with an example where it's possible to transform A to B
x1, y1 = 1, 1
x2, y2 = 5, 5
x3, y3 = 2, 2

result = "YES" if can_transform(x1, y1, x2, y2, x3, y3) else "NO"
expected = "YES"

if result == expected:
    print("verified")
else:
    print(f"Test failed: expected {expected}, got {result}")