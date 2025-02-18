'''
Problem id: 1003-E
Statement: You are given three integers $$$n$$$, $$$d$$$ and $$$k$$$.

Your task is to construct an undirected tree on $$$n$$$ vertices with diameter $$$d$$$ and degree of each vertex at most $$$k$$$, or say that it is impossible.

An undirected tree is a connected undirected graph with $$$n - 1$$$ edges.

Diameter of a tree is the maximum length of a simple path (a path in which each vertex appears at most once) between all pairs of vertices of this tree.

Degree of a vertex is the number of edges incident to this vertex (i.e. for a vertex $$$u$$$ it is the number of edges $$$(u, v)$$$ that belong to the tree, where $$$v$$$ is any other vertex of a tree).

The first line of the input contains three integers $$$n$$$, $$$d$$$ and $$$k$$$ ($$$1 \le n, d, k \le 4 \cdot 10^5$$$).

If there is no tree satisfying the conditions above, print only one word "NO" (without quotes).

Otherwise in the first line print "YES" (without quotes), and then print $$$n - 1$$$ lines describing edges of a tree satisfying the conditions above. Vertices of the tree must be numbered from $$$1$$$ to $$$n$$$. You can print edges and vertices connected by an edge in any order. If there are multiple answers, print any of them.1
Tags: constructivealgorithms,graphs,*2100
'''

def construct_tree(n, d, k):
    # Check feasibility
    if n <= d or k < 2:
        return "NO"
    
    # If k == 2, the structure is limited to a path or disjoint paths.
    if d == 1 and n > 2 and k == 1:
        return "NO"

    # Create a linear path for the diameter
    edges = []
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    remaining_vertices = n - (d + 1)
    
    # Whether each vertex in the path is able to hold additional children
    availability = [k - 2 if 1 <= i <= d else 0 for i in range(n + 1)]
    available_indices = list(range(1, d + 1))

    current_vertex = d + 2

    for u in available_indices:
        while availability[u] > 0 and remaining_vertices > 0:
            if current_vertex > n:
                return "NO"
            edges.append((u, current_vertex))
            availability[u] -= 1
            availability.append(k - 1)
            available_indices.append(current_vertex)
            remaining_vertices -= 1
            current_vertex += 1

    if remaining_vertices > 0:
        return "NO"

    return "YES", edges

def verify():
    # Verify function
    n, d, k = 7, 4, 3
    expected_diameter = 4
    expected_degrees = [0] * (n + 1)

    result = construct_tree(n, d, k)
    if result == "NO":
        print("Failed, expected a valid tree with diameter", expected_diameter)
        return

    status, edges = result
    
    # Check if the number of edges is correct
    if len(edges) != n - 1:
        print("Failed, expected", n - 1, "edges but got", len(edges))
        return

    from collections import defaultdict, deque

    def bfs_longest_path(start):
        visited = [False] * (n + 1)
        queue = deque([(start, 0)])
        visited[start] = True
        farthest_node = (start, 0)

        while queue:
            node, length = queue.popleft()
            if length > farthest_node[1]:
                farthest_node = (node, length)
            for neighbour in tree[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append((neighbour, length + 1))

        return farthest_node

    # Build the graph
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
        expected_degrees[u] += 1
        expected_degrees[v] += 1

    # Check if the degree constraint is satisfied
    if any(degree > k for degree in expected_degrees):
        print("Failed, degree constraint exceeded")
        return

    # Check the diameter
    _, endpoint = bfs_longest_path(1)
    _, actual_diameter = bfs_longest_path(endpoint)

    if actual_diameter != expected_diameter:
        print("Failed, expected diameter", expected_diameter, "but got", actual_diameter)
        return

    print("Verified")

verify()