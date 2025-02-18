'''
Problem id: 101-D
Statement: Gerald is positioned in an old castle which consists of n halls connected with n - 1 corridors. It is exactly one way to go from any hall to any other one. Thus, the graph is a tree. Initially, at the moment of time 0, Gerald is positioned in hall 1. Besides, some other hall of the castle contains the treasure Gerald is looking for. The treasure's position is not known; it can equiprobably be in any of other n - 1 halls. Gerald can only find out where the treasure is when he enters the hall with the treasure. That very moment Gerald sees the treasure and the moment is regarded is the moment of achieving his goal. 

The corridors have different lengths. At that, the corridors are considered long and the halls are considered small and well lit. Thus, it is possible not to take the time Gerald spends in the halls into consideration. The castle is very old, that's why a corridor collapses at the moment when somebody visits it two times, no matter in which direction. 

Gerald can move around the castle using the corridors; he will go until he finds the treasure. Naturally, Gerald wants to find it as quickly as possible. In other words, he wants to act in a manner that would make the average time of finding the treasure as small as possible. Each corridor can be used no more than two times. That's why Gerald chooses the strategy in such a way, so he can visit every hall for sure.

More formally, if the treasure is located in the second hall, then Gerald will find it the moment he enters the second hall for the first time — let it be moment t2. If the treasure is in the third hall, then Gerald will find it the moment he enters the third hall for the first time. Let it be the moment of time t3. And so on. Thus, the average time of finding the treasure will be equal to .

The first line contains the only integer n (2 ≤ n ≤ 105) — the number of halls in the castle. Next n - 1 lines each contain three integers. The i-th line contains numbers ai, bi and ti (1 ≤ ai, bi ≤ n, ai ≠ bi, 1 ≤ ti ≤ 1000) — the numbers of halls connected with the i-th corridor and the time needed to go along the corridor. Initially Gerald is in the hall number 1. It is guaranteed that one can get from any hall to any other one using corridors.

Print the only real number: the sought expectation of time needed to find the treasure. The answer should differ from the right one in no less than 10 - 6.

In the first test the castle only has two halls which means that the treasure is located in the second hall. Gerald will only need one minute to go to the second hall from the first one.

In the second test Gerald can only go from the first hall to the third one. He can get from the third room to the first one or to the second one, but he has already visited the first hall and can get nowhere from there. Thus, he needs to go to the second hall. He should go to hall 4 from there, because all other halls have already been visited. If the treasure is located in the third hall, Gerald will find it in a minute, if the treasure is located in the second hall, Gerald finds it in two minutes, if the treasure is in the fourth hall, Gerald will find it in three minutes. The average time makes 2 minutes.

In the third test Gerald needs to visit 4 halls: the second, third, fourth and fifth ones. All of them are only reachable from the first hall. Thus, he needs to go to those 4 halls one by one and return. Gerald will enter the first of those halls in a minute, in the second one — in three minutes, in the third one - in 5 minutes, in the fourth one - in 7 minutes. The average time is 4 minutes. 
Tags: dp,greedy,probabilities,sortings,trees,*2300
'''

def solve_treasure_castle(n, corridors):
    from collections import defaultdict
    import heapq
    
    # Step 1: Graph Representation
    adj = defaultdict(list)
    for a, b, t in corridors:
        adj[a].append((b, t))
        adj[b].append((a, t))
    
    # Step 2: Calculate Subtree Sizes using DFS
    def dfs_subtree_sizes(node, parent):
        subtree_size[node] = 1
        for nei, time in adj[node]:
            if nei == parent:
                continue
            subtree_size[node] += dfs_subtree_sizes(nei, node)
        return subtree_size[node]

    # Step 3: Prioritize visiting orders
    def priority_traversal(node, parent, current_time):
        # Using a priority queue to decide next node based on subtree size
        queue = []
        for nei, time in adj[node]:
            if nei == parent:
                continue
            heapq.heappush(queue, (-subtree_size[nei], time, nei))

        total_time = 0
        count = 0
        while queue:
            _, time, nei = heapq.heappop(queue)
            count += 1
            current_time += time
            first_visit_times[nei] = current_time
            recursive_time, recursive_count = priority_traversal(nei, node, current_time)
            total_time += recursive_time
            count += recursive_count
            # Return to node
            current_time += time
        return total_time, count

    subtree_size = [0] * (n + 1)
    first_visit_times = [0] * (n + 1)

    # Initial DFS to calculate sizes
    dfs_subtree_sizes(1, -1)

    # Step 4: Execute priority traversal
    total_time_travelled, halls_visited = priority_traversal(1, -1, 0)

    # Calculate expected time
    halls_to_visit = n - 1
    expected_time = sum(first_visit_times[2:]) / halls_to_visit

    return expected_time

# Verification function

def verify_solution():
    # Test case 1
    n1 = 2
    corridors1 = [(1, 2, 1)]  # (hall1, hall2, time)
    result1 = solve_treasure_castle(n1, corridors1)
    expected1 = 1.0
    if abs(result1 - expected1) < 1e-6:
        print("Test 1 verified")
    else:
        print(f"Test 1 failed: got {result1}, expected {expected1}")
        
    # Test case 2
    n2 = 4
    corridors2 = [(1, 3, 1), (3, 2, 1), (2, 4, 1)]
    result2 = solve_treasure_castle(n2, corridors2)
    expected2 = 2.0
    if abs(result2 - expected2) < 1e-6:
        print("Test 2 verified")
    else:
        print(f"Test 2 failed: got {result2}, expected {expected2}")
        
    # Test case 3
    n3 = 5
    corridors3 = [(1, 2, 1), (1, 3, 2), (1, 4, 3), (1, 5, 4)]
    result3 = solve_treasure_castle(n3, corridors3)
    expected3 = 4.0
    if abs(result3 - expected3) < 1e-6:
        print("Test 3 verified")
    else:
        print(f"Test 3 failed: got {result3}, expected {expected3}")

# Run verification
def main():
    verify_solution()

main()