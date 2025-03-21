'''
Problem id: 10-E
Statement: Billy investigates the question of applying greedy algorithm to different spheres of life. At the moment he is studying the application of greedy algorithm to the problem about change. There is an amount of n coins of different face values, and the coins of each value are not limited in number. The task is to collect the sum x with the minimum amount of coins. Greedy algorithm with each its step takes the coin of the highest face value, not exceeding x. Obviously, if among the coins' face values exists the face value 1, any sum x can be collected with the help of greedy algorithm. However, greedy algorithm does not always give the optimal representation of the sum, i.e. the representation with the minimum amount of coins. For example, if there are face values {1, 3, 4} and it is asked to collect the sum 6, greedy algorithm will represent the sum as 4 + 1 + 1, while the optimal representation is 3 + 3, containing one coin less. By the given set of face values find out if there exist such a sum x that greedy algorithm will collect in a non-optimal way. If such a sum exists, find out the smallest of these sums.

The first line contains an integer n (1 ≤ n ≤ 400) — the amount of the coins' face values. The second line contains n integers ai (1 ≤ ai ≤ 109), describing the face values. It is guaranteed that a1 > a2 > ... > an and an = 1.

If greedy algorithm collects any sum in an optimal way, output -1. Otherwise output the smallest sum that greedy algorithm collects in a non-optimal way.
Tags: constructivealgorithms,*2600
'''

def find_non_optimal_sum(coin_values):
    # Step 1: Handle edge cases
    if len(coin_values) == 1 or coin_values[-1] != 1:
        return -1
    
    # Step 2: Prepare variables
    n = len(coin_values)
    X = 2 * coin_values[0]  # We will explore sums up to double the largest denomination
    
    # Step 3: Initialize the DP array where dp[x] is the minimum number of coins to make x
    dp = [float('inf')] * (X + 1)
    dp[0] = 0

    # Step 4: Fill the DP table
    for x in range(1, X + 1):
        for coin in coin_values:
            if coin <= x:
                dp[x] = min(dp[x], dp[x - coin] + 1)

    # Step 5: Check each sum from 1 to X with greedy algorithm
    for x in range(1, X + 1):
        greedy_count = 0
        remainder = x

        for coin in coin_values:
            if coin <= remainder:
                greedy_count += remainder // coin
                remainder = remainder % coin

        # Compare greedy approach vs optimal DP approach
        if greedy_count > dp[x]:
            return x

    return -1

# Test case based on the problem statement
coins = [4, 3, 1]
expected_result = 6

# Run the function with the test case
actual_result = find_non_optimal_sum(coins)

# Verification
if actual_result == expected_result:
    print('verified')
else:
    print(f'Error: expected {expected_result}, but got {actual_result}')