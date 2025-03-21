'''
Problem id: 325-C
Statement: Piegirl has found a monster and a book about monsters and pies. When she is reading the book, she found out that there are n types of monsters, each with an ID between 1 and n. If you feed a pie to a monster, the monster will split into some number of monsters (possibly zero), and at least one colorful diamond. Monsters may be able to split in multiple ways.

At the begining Piegirl has exactly one monster. She begins by feeding the monster a pie. She continues feeding pies to monsters until no more monsters are left. Then she collects all the diamonds that were created.

You will be given a list of split rules describing the way in which the various monsters can split. Every monster can split in at least one way, and if a monster can split in multiple ways then each time when it splits Piegirl can choose the way it splits.

For each monster, determine the smallest and the largest number of diamonds Piegirl can possibly collect, if initially she has a single instance of that monster. Piegirl has an unlimited supply of pies.

The first line contains two integers: m and n (1 ≤ m, n ≤ 105), the number of possible splits and the number of different monster types. Each of the following m lines contains a split rule. Each split rule starts with an integer (a monster ID) mi (1 ≤ mi ≤ n), and a positive integer li indicating the number of monsters and diamonds the current monster can split into. This is followed by li integers, with positive integers representing a monster ID and -1 representing a diamond.

Each monster will have at least one split rule. Each split rule will have at least one diamond. The sum of li across all split rules will be at most 105.

For each monster, in order of their IDs, print a line with two integers: the smallest and the largest number of diamonds that can possibly be collected by starting with that monster. If Piegirl cannot possibly end up in a state without monsters, print -1 for both smallest and the largest value. If she can collect an arbitrarily large number of diamonds, print -2 as the largest number of diamonds. 

If any number in output exceeds 314000000 (but is finite), print 314000000 instead of that number.
Tags: dfsandsimilar,graphs,shortestpaths,*2600
'''

def solve_monster_problem(m, n, split_rules):
    from collections import defaultdict, deque
    import sys

    sys.setrecursionlimit(200000)

    # Constants
    INF = float('inf')
    LIMIT = 314000000

    # Initialize Graph
    adj_list = defaultdict(list)

    # Parse split rules
    for rule in split_rules:
        mi = rule[0]
        li = rule[1]
        adj_list[mi].append(rule[2:])  # Add the generated monsters and diamonds rule

    # Arrays to store minimum and maximum diamonds
    min_diamonds = [INF] * (n + 1)
    max_diamonds = [-1] * (n + 1)

    # Helper function for DFS with memoization
    def dfs(monster_id, min_diam, max_diam, visited):
        if min_diam[monster_id] != INF and max_diam[monster_id] != -1:
            # Already calculated
            return min_diam[monster_id], max_diam[monster_id]
        if visited[monster_id]:
            # We're in a cycle, check for possible infinite case
            return INF, -2

        visited[monster_id] = True
        local_min = INF
        local_max = 0
        for rule in adj_list[monster_id]:
            diamonds = rule.count(-1)
            next_monsters = [m for m in rule if m != -1]
            # Sum diamonds and recursive call on next monsters
            cur_min = diamonds
            cur_max = diamonds
            for nm in next_monsters:
                min_result, max_result = dfs(nm, min_diam, max_diam, visited)
                if max_result == -2:
                    cur_max = -2
                elif max_result != -1:
                    cur_max += max_result
                if min_result == INF:
                    cur_min = INF
                else:
                    cur_min += min_result
            local_min = min(local_min, cur_min)
            if cur_max != -2:
                local_max = max(local_max, cur_max)
            else:
                local_max = -2
        if local_min == INF:
            min_diam[monster_id] = -1
        else:
            min_diam[monster_id] = local_min
        max_diam[monster_id] = local_max
        visited[monster_id] = False
        return min_diam[monster_id], max_diam[monster_id]

    # Calculate for each monster type
    for monster_id in range(1, n + 1):
        if min_diamonds[monster_id] == INF:
            visited = [False] * (n + 1)
            min_d, max_d = dfs(monster_id, min_diamonds, max_diamonds, visited)
            if min_d > LIMIT:
                min_d = LIMIT
            if max_d > LIMIT:
                max_d = LIMIT
            min_diamonds[monster_id] = min_d
            max_diamonds[monster_id] = max_d

    # Prepare output
    result = []
    for i in range(1, n + 1):
        if min_diamonds[i] > LIMIT:
            min_diamonds[i] = LIMIT
        if max_diamonds[i] > LIMIT:
            max_diamonds[i] = LIMIT
        result.append((min_diamonds[i], max_diamonds[i]))

    return result

# Test case (m = 1, n = 1)
# One monster with a single split rule: one diamond
m = 1
n = 1
split_rules = [
    [1, 1, -1]  # Monster 1 splits into 1 diamond
]
actual_output = solve_monster_problem(m, n, split_rules)
expected_output = [(1, 1)]

# Verify output
if actual_output == expected_output:
    print('verified')
else:
    print(f'mismatch: got {actual_output}, expected {expected_output})')