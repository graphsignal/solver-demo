'''
Problem id: 1015-A
Statement: You are given a set of $$$n$$$ segments on the axis $$$Ox$$$, each segment has integer endpoints between $$$1$$$ and $$$m$$$ inclusive. Segments may intersect, overlap or even coincide with each other. Each segment is characterized by two integers $$$l_i$$$ and $$$r_i$$$ ($$$1 \le l_i \le r_i \le m$$$) — coordinates of the left and of the right endpoints. 

Consider all integer points between $$$1$$$ and $$$m$$$ inclusive. Your task is to print all such points that don't belong to any segment. The point $$$x$$$ belongs to the segment $$$[l; r]$$$ if and only if $$$l \le x \le r$$$.

The first line of the input contains two integers $$$n$$$ and $$$m$$$ ($$$1 \le n, m \le 100$$$) — the number of segments and the upper bound for coordinates.

The next $$$n$$$ lines contain two integers each $$$l_i$$$ and $$$r_i$$$ ($$$1 \le l_i \le r_i \le m$$$) — the endpoints of the $$$i$$$-th segment. Segments may intersect, overlap or even coincide with each other. Note, it is possible that $$$l_i=r_i$$$, i.e. a segment can degenerate to a point.

In the first line print one integer $$$k$$$ — the number of points that don't belong to any segment.

In the second line print exactly $$$k$$$ integers in any order — the points that don't belong to any segment. All points you print should be distinct.

If there are no such points at all, print a single integer $$$0$$$ in the first line and either leave the second line empty or do not print it at all.

In the first example the point $$$1$$$ belongs to the second segment, the point $$$2$$$ belongs to the first and the second segments and the point $$$5$$$ belongs to the third segment. The points $$$3$$$ and $$$4$$$ do not belong to any segment.

In the second example all the points from $$$1$$$ to $$$7$$$ belong to the first segment.
Tags: implementation,*800
'''

def find_uncovered_points(n, m, segments):
    # Step 1: Initialize the covered array
    covered = [False] * (m + 1)

    # Step 2: Mark covered points for each segment
    for l, r in segments:
        for j in range(l, r + 1):
            covered[j] = True

    # Step 3: Gather all uncovered points
    uncovered_points = [x for x in range(1, m + 1) if not covered[x]]

    # Step 4: Return results
    return len(uncovered_points), uncovered_points

# Correct example verification call
n = 3
m = 5
segments = [(1, 2), (3, 3), (5, 5)]

expected_length = 1
expected_points = [4]

actual_length, actual_points = find_uncovered_points(n, m, segments)

if actual_length == expected_length and set(actual_points) == set(expected_points):
    print("verified")
else:
    print(f"Test failed: Length - expected {expected_length}, got {actual_length}; "
          f"Points - expected {expected_points}, got {actual_points}")