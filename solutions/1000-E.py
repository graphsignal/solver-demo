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

# Helper function to add an edge to the graph
def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

# A helper function to find bridges in a graph using DFS
def bridge_dfs(u, visited, parent, low, disc, graph, bridges, time):
    visited[u] = True
    disc[u] = low[u] = time[0]
    time[0] += 1

    for v in graph[u]:
        if not visited[v]:
            parent[v] = u
            bridge_dfs(v, visited, parent, low, disc, graph, bridges, time)

            low[u] = min(low[u], low[v])

            if low[v] > disc[u]:
                bridges.append((u, v))
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])

# The function that implements the solution algorithm
def maximum_bosses(n, m, edges):
    graph = defaultdict(list)

    for x, y in edges:
        add_edge(graph, x, y)

    visited = [False] * (n + 1)
    disc = [-1] * (n + 1)
    low = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    bridges = []
    time = [0]

    for i in range(1, n + 1):
        if not visited[i]:
            bridge_dfs(i, visited, parent, low, disc, graph, bridges, time)

    return len(bridges)

# Verification test case
def verify_maximum_bosses():
    # Sample Input: Graph with 5 nodes and 5 edges, having 2 bridges
    n, m = 5, 5
    edges = [
        (1, 2),
        (1, 3),
        (3, 4),
        (3, 5),
        (4, 5),
    ]
    expected_result = 2  # The bridges are (1, 2) and (3, 4)

    actual_result = maximum_bosses(n, m, edges)
    
    if actual_result == expected_result:
        print("verified")
    else:
        print(f"Failed: Expected {expected_result}, but got {actual_result}.")

# Run verification
def test_solution():
    verify_maximum_bosses()

test_solution()