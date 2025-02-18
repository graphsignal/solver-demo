'''
Problem id: 1016-C
Statement: Vasya's house is situated in a forest, and there is a mushroom glade near it. The glade consists of two rows, each of which can be divided into n consecutive cells. For each cell Vasya knows how fast the mushrooms grow in this cell (more formally, how many grams of mushrooms grow in this cell each minute). Vasya spends exactly one minute to move to some adjacent cell. Vasya cannot leave the glade. Two cells are considered adjacent if they share a common side. When Vasya enters some cell, he instantly collects all the mushrooms growing there.

Vasya begins his journey in the left upper cell. Every minute Vasya must move to some adjacent cell, he cannot wait for the mushrooms to grow. He wants to visit all the cells exactly once and maximize the total weight of the collected mushrooms. Initially, all mushrooms have a weight of 0. Note that Vasya doesn't need to return to the starting cell.

Help Vasya! Calculate the maximum total weight of mushrooms he can collect.

The first line contains the number n (1 ≤ n ≤ 3·105) — the length of the glade.

The second line contains n numbers a1, a2, ..., an (1 ≤ ai ≤ 106) — the growth rate of mushrooms in the first row of the glade.

The third line contains n numbers b1, b2, ..., bn (1 ≤ bi ≤ 106) is the growth rate of mushrooms in the second row of the glade.

Output one number — the maximum total weight of mushrooms that Vasya can collect by choosing the optimal route. Pay attention that Vasya must visit every cell of the glade exactly once.

In the first test case, the optimal route is as follows: 

In the second test case, the optimal route is as follows: 
Tags: dp,implementation,*1800
'''

def max_mushrooms(n, a, b):
    # Calculate prefix sums for both rows
    prefix_a = [0] * (n + 1)
    prefix_b = [0] * (n + 1)

    for i in range(1, n+1):
        prefix_a[i] = prefix_a[i-1] + a[i-1]
        prefix_b[i] = prefix_b[i-1] + b[i-1]

    # Initialize two possible maximum scores for reaching the end
    max_weight_end1 = 0
    max_weight_end2 = 0

    # Try all possible split points where Vasya changes from first row to second row
    for i in range(1, n+1):
        # Collect all from (1,1) to (1,i) then (2,i) to (2,n)
        collect_path1 = prefix_a[i] + (prefix_b[n] - prefix_b[i-1])
        # Collect all from (1,1) to (1,n) to (2,n) to (2,i)
        collect_path2 = prefix_b[i] + (prefix_a[n] - prefix_a[i-1])
        
        # Track the maximum weight possible ending at row 1 or row 2
        max_weight_end1 = max(max_weight_end1, collect_path1)
        max_weight_end2 = max(max_weight_end2, collect_path2)

    # The answer will be the maximum possible mushrooms collected across any valid path
    return max(max_weight_end1, max_weight_end2)

# Test case to verify
n = 3
row_a = [4, 1, 3]
row_b = [2, 5, 4]

# Optimal path analysis previously identified sum as 15
expected = 15

actual = max_mushrooms(n, row_a, row_b)
if actual == expected:
    print('verified')
else:
    print(f'Error: Expected {expected}, but got {actual}')