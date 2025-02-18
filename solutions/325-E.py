'''
Problem id: 325-E
Statement: Piegirl found the red button. You have one last chance to change the inevitable end.

The circuit under the button consists of n nodes, numbered from 0 to n - 1. In order to deactivate the button, the n nodes must be disarmed in a particular order. Node 0 must be disarmed first. After disarming node i, the next node to be disarmed must be either node (2·i) modulo n or node (2·i) + 1 modulo n. The last node to be disarmed must be node 0. Node 0 must be disarmed twice, but all other nodes must be disarmed exactly once. 

Your task is to find any such order and print it. If there is no such order, print -1.

Input consists of a single integer n (2 ≤ n ≤ 105).

Print an order in which you can to disarm all nodes. If it is impossible, print -1 instead. If there are multiple orders, print any one of them.
Tags: combinatorics,dfsandsimilar,dsu,graphs,greedy,*2800
'''

def disarm_nodes(n):
    if n % 2 == 1:
        return -1
    
    sequence = []
    stack = [0]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        sequence.append(node)
        next1 = (2 * node) % n
        next2 = (2 * node + 1) % n
        if next2 not in visited and len(visited) < n:
            stack.append(next2)
        if next1 not in visited and len(visited) < n:
            stack.append(next1)
    
    sequence.append(0)  # Return to start
    
    return sequence

# Verification Test Function
def test_disarm_nodes():
    n = 4
    result = disarm_nodes(n)
    
    expected_size = n + 1
    valid = (
        result != -1 and len(result) == expected_size
        and result[0] == 0 and result[-1] == 0
        and len(set(result)) == n
    )
    
    if valid:
        print("verified")
    else:
        print(f"Test case failed. Check output for n={n}. Got: {result}")

# While this test checks n=4, modify with other even number cases if intended.
test_disarm_nodes()