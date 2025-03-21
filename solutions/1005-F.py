'''
Problem id: 1005-F
Statement: There are $$$n$$$ cities in Berland. Some pairs of cities are connected by roads. All roads are bidirectional. Each road connects two different cities. There is at most one road between a pair of cities. The cities are numbered from $$$1$$$ to $$$n$$$.

It is known that, from the capital (the city with the number $$$1$$$), you can reach any other city by moving along the roads.

The President of Berland plans to improve the country's road network. The budget is enough to repair exactly $$$n-1$$$ roads. The President plans to choose a set of $$$n-1$$$ roads such that:

In other words, the set of $$$n-1$$$ roads should preserve the connectivity of the country, and the sum of distances from city $$$1$$$ to all cities should be minimized (where you can only use the $$$n-1$$$ chosen roads).

The president instructed the ministry to prepare $$$k$$$ possible options to choose $$$n-1$$$ roads so that both conditions above are met.

Write a program that will find $$$k$$$ possible ways to choose roads for repair. If there are fewer than $$$k$$$ ways, then the program should output all possible valid ways to choose roads.

The first line of the input contains integers $$$n$$$, $$$m$$$ and $$$k$$$ ($$$2 \le n \le 2\cdot10^5, n-1 \le m \le 2\cdot10^5, 1 \le k \le 2\cdot10^5$$$), where $$$n$$$ is the number of cities in the country, $$$m$$$ is the number of roads and $$$k$$$ is the number of options to choose a set of roads for repair. It is guaranteed that $$$m \cdot k \le 10^6$$$.

The following $$$m$$$ lines describe the roads, one road per line. Each line contains two integers $$$a_i$$$, $$$b_i$$$ ($$$1 \le a_i, b_i \le n$$$, $$$a_i \ne b_i$$$) — the numbers of the cities that the $$$i$$$-th road connects. There is at most one road between a pair of cities. The given set of roads is such that you can reach any city from the capital.

Print $$$t$$$ ($$$1 \le t \le k$$$) — the number of ways to choose a set of roads for repair. Recall that you need to find $$$k$$$ different options; if there are fewer than $$$k$$$ of them, then you need to find all possible different valid options.

In the following $$$t$$$ lines, print the options, one per line. Print an option as a string of $$$m$$$ characters where the $$$j$$$-th character is equal to '1' if the $$$j$$$-th road is included in the option, and is equal to '0' if the road is not included. The roads should be numbered according to their order in the input. The options can be printed in any order. All the $$$t$$$ lines should be different.

Since it is guaranteed that $$$m \cdot k \le 10^6$$$, the total length of all the $$$t$$$ lines will not exceed $$$10^6$$$.

If there are several answers, output any of them.
Tags: bruteforce,dfsandsimilar,graphs,shortestpaths,*2100
'''

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False


def find_mst_variants(n, m, k, roads):
    # Initialize variables
    roads_with_index = [(c1, c2, i) for i, (c1, c2) in enumerate(roads)]
    potential_msts = []
    # Determine initial MST using Kruskal's algorithm
    def kruskal(roads):
        uf = UnionFind(n)
        mst = []

        for u, v, idx in roads:
            if uf.union(u, v):
                mst.append(idx)
                if len(mst) == n - 1:
                    break
        return mst

    # Edge list needs to be sorted for typical Kruskal's behavior, 
    # but here all roads have equal priority so we assume them as sorted
    initial_mst = kruskal(roads_with_index)
    potential_msts.append(initial_mst)

    # Function to explore alternative MSTs using DFS on removed edges and other possibilities
    def explore_alternatives(mst_base):
        nonlocal potential_msts
        used_edges = set(mst_base)

        for excluded in mst_base:
            alternative_mst = [e for e in mst_base if e != excluded]
            uf = UnionFind(n)
            for idx in alternative_mst:
                u, v = roads_with_index[idx][0], roads_with_index[idx][1]
                uf.union(u, v)

            # Attempt to add different edges
            for u, v, idx in roads_with_index:
                if idx not in used_edges and uf.union(u, v):
                    alternative_mst.append(idx)
                if len(alternative_mst) == n - 1:
                    potential_msts.append(alternative_mst)
                    break
            if len(potential_msts) >= k:
                return

    # Explore alternative MSTs
    explore_alternatives(initial_mst)

    return [create_output(m, mst) for mst in potential_msts[:k]]


def create_output(m, mst):
    mst_set = set(mst)
    return ''.join('1' if i in mst_set else '0' for i in range(m))


def verify():
    # Example: Simple triangle connected graph
    n, m, k = 3, 3, 2
    roads = [(0, 1), (1, 2), (0, 2)]
    expected = {'110', '011'}  # Two possible MSTs
    result = find_mst_variants(n, m, k, roads)
    assert set(result).issubset(expected), f"Test failed: got {set(result)}, expected a subset of {expected}"
    print('verified')

verify()