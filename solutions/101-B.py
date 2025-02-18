'''
Problem id: 101-B
Statement: Little boy Gerald studies at school which is quite far from his house. That's why he has to go there by bus every day. The way from home to school is represented by a segment of a straight line; the segment contains exactly n + 1 bus stops. All of them are numbered with integers from 0 to n in the order in which they follow from Gerald's home. The bus stop by Gerald's home has number 0 and the bus stop by the school has number n.

There are m buses running between the house and the school: the i-th bus goes from stop si to ti (si < ti), visiting all the intermediate stops in the order in which they follow on the segment. Besides, Gerald's no idiot and he wouldn't get off the bus until it is still possible to ride on it closer to the school (obviously, getting off would be completely pointless). In other words, Gerald can get on the i-th bus on any stop numbered from si to ti - 1 inclusive, but he can get off the i-th bus only on the bus stop ti.

Gerald can't walk between the bus stops and he also can't move in the direction from the school to the house.

Gerald wants to know how many ways he has to get from home to school. Tell him this number. Two ways are considered different if Gerald crosses some segment between the stops on different buses. As the number of ways can be too much, find the remainder of a division of this number by 1000000007 (109 + 7).

The first line contains two space-separated integers: n and m (1 ≤ n ≤ 109, 0 ≤ m ≤ 105). Then follow m lines each containing two integers si, ti. They are the numbers of starting stops and end stops of the buses (0 ≤ si < ti ≤ n).

Print the only number — the number of ways to get to the school modulo 1000000007 (109 + 7).

The first test has the only variant to get to school: first on bus number one to the bus stop number one; then on bus number two to the bus stop number two.

In the second test no bus goes to the third bus stop, where the school is positioned. Thus, the correct answer is 0.

In the third test Gerald can either get or not on any of the first four buses to get closer to the school. Thus, the correct answer is 24 = 16.
Tags: binarysearch,datastructures,dp,*1700
'''

def count_ways_to_school(n, m, buses):
    MOD = 1000000007
    
    # Dictionary to store buses ending at a particular stop
    ends_at = {}
    
    for si, ti in buses:
        if ti not in ends_at:
            ends_at[ti] = []
        ends_at[ti].append(si)

    # Dictionary to store number of ways to reach each stop
    dp = {0: 1}  # Start with stop 0

    # List of stops where buses end, sorted
    stops = sorted(ends_at.keys())

    # Process each stop
    for stop in stops:
        if stop in ends_at:
            for si in ends_at[stop]:
                if si in dp:
                    dp[stop] = (dp.get(stop, 0) + dp[si]) % MOD

    # Return the number of ways to reach stop n
    return dp.get(n, 0)

# Sample Test Cases

def verify():
    # Test case 1
    n1, m1 = 2, 2
    buses1 = [(0, 1), (1, 2)]
    expected1 = 1
    result1 = count_ways_to_school(n1, m1, buses1)
    if result1 == expected1:
        print("Test Case 1: verified")
    else:
        print(f"Test Case 1: incorrect, expected {expected1}, got {result1}")
        
    # Test case 2
    n2, m2 = 3, 2
    buses2 = [(0, 1), (1, 2)]
    expected2 = 0
    result2 = count_ways_to_school(n2, m2, buses2)
    if result2 == expected2:
        print("Test Case 2: verified")
    else:
        print(f"Test Case 2: incorrect, expected {expected2}, got {result2}")
        
    # Test case 3
    n3, m3 = 2, 4
    buses3 = [(0, 2), (0, 2), (0, 2), (0, 2)]
    expected3 = 16
    result3 = count_ways_to_school(n3, m3, buses3)
    if result3 == expected3:
        print("Test Case 3: verified")
    else:
        print(f"Test Case 3: incorrect, expected {expected3}, got {result3}")

verify()