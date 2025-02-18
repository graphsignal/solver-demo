'''
Problem id: 1006-F
Statement: There is a rectangular grid of size $$$n \times m$$$. Each cell has a number written on it; the number on the cell ($$$i, j$$$) is $$$a_{i, j}$$$. Your task is to calculate the number of paths from the upper-left cell ($$$1, 1$$$) to the bottom-right cell ($$$n, m$$$) meeting the following constraints:

Find the number of such paths in the given grid.

The first line of the input contains three integers $$$n$$$, $$$m$$$ and $$$k$$$ ($$$1 \le n, m \le 20$$$, $$$0 \le k \le 10^{18}$$$) — the height and the width of the grid, and the number $$$k$$$.

The next $$$n$$$ lines contain $$$m$$$ integers each, the $$$j$$$-th element in the $$$i$$$-th line is $$$a_{i, j}$$$ ($$$0 \le a_{i, j} \le 10^{18}$$$).

Print one integer — the number of paths from ($$$1, 1$$$) to ($$$n, m$$$) with xor sum equal to $$$k$$$.

All the paths from the first example: 

All the paths from the second example: 
Tags: bitmasks,bruteforce,dp,meet-in-the-middle,*2100
'''

def solve_xor_paths(n, m, k, grid):
    from collections import defaultdict
    
    def dfs(x, y, current_xor, path_dict, end_x, end_y):
        if x == end_x and y == end_y:
            path_dict[current_xor] += 1
            return
        
        if x < end_x:
            dfs(x + 1, y, current_xor ^ grid[x + 1][y], path_dict, end_x, end_y)
        
        if y < end_y:
            dfs(x, y + 1, current_xor ^ grid[x][y + 1], path_dict, end_x, end_y)

    mid_points = [(n - 1, y) for y in range(m)] + [(x, m - 1) for x in range(n)]

    total_paths = 0

    for mid_x, mid_y in mid_points:
        paths_top = defaultdict(int)
        paths_bottom = defaultdict(int)

        dfs(0, 0, grid[0][0], paths_top, mid_x, mid_y)
        dfs(n - 1, m - 1, grid[n - 1][m - 1], paths_bottom, mid_x, mid_y)

        for xor_value_top, count_top in paths_top.items():
            needed_xor = xor_value_top ^ k
            if needed_xor in paths_bottom:
                total_paths += count_top * paths_bottom[needed_xor]

    return total_paths

# Test case verification
n = 2
m = 2
k = 3
# Grid:
# 1 2
# 3 0
# Expected number of paths with XOR equal to k = 3 is 2:
# Paths: 1 -> 3 and 1 -> 2 -> 0, XOR in first path = 1^3 = 2, and the other via 3 paths form 2 solutions.
grid = [[1, 2], [3, 0]]
expected_output = 2

actual_output = solve_xor_paths(n, m, k, grid)

if actual_output == expected_output:
    print("verified")
else:
    print(f"Error - expected: {expected_output}, but got: {actual_output}")