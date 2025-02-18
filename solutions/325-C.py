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

def solve_monster_diamonds(m, n, split_rules):
    from collections import defaultdict, deque
    import sys
    sys.setrecursionlimit(200000)

    # Constants
    CAP = 314000000
    UNREACHABLE = -1
    UNBOUNDED = -2

    # Graph setup
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    indegree = [0] * (n + 1)

    for rule in split_rules:
        monster_id, *res = rule
        num_diamonds = res.count(-1)
        result_monsters = [x for x in res if x != -1]
        graph[monster_id].append((num_diamonds, result_monsters))
        for rm in result_monsters:
            reverse_graph[rm].append(monster_id)
            indegree[rm] += 1

    # Step 1: Topological sorting with a queue
    order = []
    queue = deque()
    for monster in range(1, n + 1):
        if indegree[monster] == 0:
            queue.append(monster)

    while queue:
        node = queue.popleft()
        order.append(node)
        for num_diamonds, result_monsters in graph[node]:
            for rm in result_monsters:
                indegree[rm] -= 1
                if indegree[rm] == 0:
                    queue.append(rm)

    # Step 2: Handle cycles (check for unprocessed nodes in order)
    if len(order) < n:
        special_cases = [(UNREACHABLE, UNBOUNDED) if monster + 1 not in order else None for monster in range(n)]
    else:
        special_cases = [None] * n

    # Step 3: Process in reverse topological order
    minDiamonds = [float('inf')] * (n + 1)
    maxDiamonds = [0] * (n + 1)

    for monster in reversed(order):
        for num_diamonds, successors in graph[monster]:
            total_min = num_diamonds
            total_max = num_diamonds
            for succ in successors:
                if minDiamonds[succ] == float('inf'):
                    total_min = float('inf')
                    break
                total_min += minDiamonds[succ]
                total_max += maxDiamonds[succ]
            else:
                minDiamonds[monster] = min(minDiamonds[monster], total_min)
                maxDiamonds[monster] = max(maxDiamonds[monster], min(total_max, CAP))

    results = []
    for i in range(1, n + 1):
        if special_cases[i - 1]:
            results.append(special_cases[i - 1])
        else:
            if minDiamonds[i] == float('inf'):
                results.append((UNREACHABLE, UNREACHABLE))
            else:
                results.append((minDiamonds[i], CAP if maxDiamonds[i] >= CAP else maxDiamonds[i]))

    return results

# Sample Test Case to verify
m = 2
n = 2
split_rules = [
    [1, 2, -1],  # Monster 1 can split into 1 Monster 2 and 1 diamond
    [2, -1]      # Monster 2 can split into 1 diamond
]

# Expected Output:
# Monster 1: (2, 2) because it can split 1 -> 2 (+1 diamond), then 2 -> (+1 diamond)
# Monster 2: (1, 1) because it directly goes to 1 diamond
expected = [(2, 2), (1, 1)]

actual = solve_monster_diamonds(m, n, split_rules)

# Verification
if actual == expected:
    print('verified')
else:
    print(f'Failed: expected {expected}, but got {actual}')