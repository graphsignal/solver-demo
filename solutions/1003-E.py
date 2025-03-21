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
    if d >= n or k == 1 and d > 1:
        return "NO"
    if n == 1:
        return "YES"
    edges = []
    
    # Step 1: Create the main path with diameter d
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    remaining_vertices = n - (d + 1)
    current_used_vertices = d + 1
    
    # Step 2: Add remaining vertices to the tree
    for i in range(2, d + 1):  # We skip edges 1 and d+1 because they are leaves in the initial path
        attach_count = min(k - 2, remaining_vertices)
        for _ in range(attach_count):
            current_used_vertices += 1
            edges.append((i, current_used_vertices))
            remaining_vertices -= 1
            if remaining_vertices == 0:
                break
        if remaining_vertices == 0:
            break

    if remaining_vertices > 0:
        return "NO"

    result = "YES\n"
    for u, v in edges:
        result += f"{u} {v}\n"
    return result.strip()

# Test case for verification
def test_construct_tree():
    # Example parameters that should work
    n = 6
    d = 3
    k = 3
    
    # Call the function
    result = construct_tree(n, d, k)
    
    # Expected result calculation
    expected_result = "YES\n1 2\n2 3\n3 4\n2 5\n3 6"
    
    # Verification
    if result == expected_result:
        print("verified")
    else:
        print(f"Test failed: Got {result}, Expected {expected_result}")

# Run the test function
test_construct_tree()