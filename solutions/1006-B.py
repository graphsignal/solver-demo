'''
Problem id: 1006-B
Statement: Polycarp is practicing his problem solving skill. He has a list of $$$n$$$ problems with difficulties $$$a_1, a_2, \dots, a_n$$$, respectively. His plan is to practice for exactly $$$k$$$ days. Each day he has to solve at least one problem from his list. Polycarp solves the problems in the order they are given in his list, he cannot skip any problem from his list. He has to solve all $$$n$$$ problems in exactly $$$k$$$ days.

Thus, each day Polycarp solves a contiguous sequence of (consecutive) problems from the start of the list. He can't skip problems or solve them multiple times. As a result, in $$$k$$$ days he will solve all the $$$n$$$ problems.

The profit of the $$$j$$$-th day of Polycarp's practice is the maximum among all the difficulties of problems Polycarp solves during the $$$j$$$-th day (i.e. if he solves problems with indices from $$$l$$$ to $$$r$$$ during a day, then the profit of the day is $$$\max\limits_{l \le i \le r}a_i$$$). The total profit of his practice is the sum of the profits over all $$$k$$$ days of his practice.

You want to help Polycarp to get the maximum possible total profit over all valid ways to solve problems. Your task is to distribute all $$$n$$$ problems between $$$k$$$ days satisfying the conditions above in such a way, that the total profit is maximum.

For example, if $$$n = 8, k = 3$$$ and $$$a = [5, 4, 2, 6, 5, 1, 9, 2]$$$, one of the possible distributions with maximum total profit is: $$$[5, 4, 2], [6, 5], [1, 9, 2]$$$. Here the total profit equals $$$5 + 6 + 9 = 20$$$.

The first line of the input contains two integers $$$n$$$ and $$$k$$$ ($$$1 \le k \le n \le 2000$$$) — the number of problems and the number of days, respectively.

The second line of the input contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 2000$$$) — difficulties of problems in Polycarp's list, in the order they are placed in the list (i.e. in the order Polycarp will solve them).

In the first line of the output print the maximum possible total profit.

In the second line print exactly $$$k$$$ positive integers $$$t_1, t_2, \dots, t_k$$$ ($$$t_1 + t_2 + \dots + t_k$$$ must equal $$$n$$$), where $$$t_j$$$ means the number of problems Polycarp will solve during the $$$j$$$-th day in order to achieve the maximum possible total profit of his practice.

If there are many possible answers, you may print any of them.

The first example is described in the problem statement.

In the second example there is only one possible distribution.

In the third example the best answer is to distribute problems in the following way: $$$[1, 2000], [2000, 2]$$$. The total profit of this distribution is $$$2000 + 2000 = 4000$$$.
Tags: greedy,implementation,sortings,*1200
'''

def solve_problem(n, k, difficulties):
    # Step 1: Pair difficulties with their indices
    indexed_difficulties = [(difficulties[i], i) for i in range(n)]
    
    # Step 2: Sort difficulties by value in descending order
    indexed_difficulties.sort(key=lambda x: x[0], reverse=True)
    
    # Step 3: Select the top `k` difficulties
    top_k_difficulties = indexed_difficulties[:k]
    
    # Step 4: Extract their indices and sort these indices
    selected_indices = sorted(i for _, i in top_k_difficulties)
    
    # Step 5: Calculate maximum total profit
    max_total_profit = sum(d for d, _ in top_k_difficulties)
    
    # Step 6: Determine segment lengths
    segments = []
    previous_index = -1
    for index in selected_indices:
        # Add the length of the current segment
        segments.append(index - previous_index)
        previous_index = index
    # Last segment to cover all problems
    segments[-1] += n - previous_index - 1
    
    # return results
    return max_total_profit, segments

# Example data
n = 8
k = 3
difficulties = [5, 4, 2, 6, 5, 1, 9, 2]

# Expected output
expected_profit = 20
expected_segments = [3, 2, 3]  # Any valid combination leading to the same profit is acceptable

# Verification
actual_profit, actual_segments = solve_problem(n, k, difficulties)

# Check if the returned profit and possible segments are valid
if actual_profit == expected_profit and sum(actual_segments) == n and len(actual_segments) == k:
    print('verified')
else:
    print(f'incorrect result: Actual profit: {actual_profit}, Expected profit: {expected_profit}. Actual segments: {actual_segments}, Expected length of segments: {n}, Expected number of segments: {k}.')