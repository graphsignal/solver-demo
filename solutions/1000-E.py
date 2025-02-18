'''
Problem id: 1000-E
Statement: Your friend is developing a computer game. He has already decided how the game world should look like — it should consist of $$$n$$$ locations connected by $$$m$$$ two-way passages. The passages are designed in such a way that it should be possible to get from any location to any other location.

Of course, some passages should be guarded by the monsters (if you just can go everywhere without any difficulties, then it's not fun, right?). Some crucial passages will be guarded by really fearsome monsters, requiring the hero to prepare for battle and designing his own tactics of defeating them (commonly these kinds of monsters are called bosses). And your friend wants you to help him place these bosses.

The game will start in location $$$s$$$ and end in location $$$t$$$, but these locations are not chosen yet. After choosing these locations, your friend will place a boss in each passage such that it is impossible to get from $$$s$$$ to $$$t$$$ without using this passage. Your friend wants to place as much bosses as possible (because more challenges means more fun, right?), so he asks you to help him determine the maximum possible number of bosses, considering that any location can be chosen as $$$s$$$ or as $$$t$$$.

The first line contains two integers $$$n$$$ and $$$m$$$ ($$$2 \le n \le 3 \cdot 10^5$$$, $$$n - 1 \le m \le 3 \cdot 10^5$$$) — the number of locations and passages, respectively.

Then $$$m$$$ lines follow, each containing two integers $$$x$$$ and $$$y$$$ ($$$1 \le x, y \le n$$$, $$$x \ne y$$$) describing the endpoints of one of the passages.

It is guaranteed that there is no pair of locations directly connected by two or more passages, and that any location is reachable from any other location.

Print one integer — the maximum number of bosses your friend can place, considering all possible choices for $$$s$$$ and $$$t$$$.
Tags: dfsandsimilar,graphs,trees,*2100
'''

from collections import defaultdict

# Tarjan's algorithm for finding bridges in an undirected graph
def find_bridges(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    time = [0]  # Global timer for discovery times
    disc = [-1] * (n + 1)
    low = [-1] * (n + 1)
    visited = [False] * (n + 1)
    bridges = []

    def dfs(u, parent):
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1

        for v in graph[u]:
            if v == parent:
                continue

            if not visited[v]:
                dfs(v, u)

                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    bridges.append((u, v))
            else:
                low[u] = min(low[u], disc[v])

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, -1)

    return bridges

# Solution function
def max_number_of_bosses(n, m, passages):
    # Find all bridges in the graph
    bridges = find_bridges(n, passages)
    # The number of bridges is the maximum number of bosses that can be placed
    return len(bridges)

# Verify the solution with a known test case
def verify_solution():
    # Example graph with 5 locations and 5 passages
    # The graph is a chain: 1-2-3-4-5
    n = 5
    m = 5
    passages = [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (2, 4)  # Extra passage to maintain connectivity
    ]
    expected_number_of_bosses = 2  # Bridges: (1,2), (4,5)

    result = max_number_of_bosses(n, m, passages)

    if result == expected_number_of_bosses:
        print('verified')
    else:
        print(f'Incorrect: expected {expected_number_of_bosses}, got {result}')

verify_solution()