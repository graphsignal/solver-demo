'''
Problem id: 10-E
Statement: Billy investigates the question of applying greedy algorithm to different spheres of life. At the moment he is studying the application of greedy algorithm to the problem about change. There is an amount of n coins of different face values, and the coins of each value are not limited in number. The task is to collect the sum x with the minimum amount of coins. Greedy algorithm with each its step takes the coin of the highest face value, not exceeding x. Obviously, if among the coins' face values exists the face value 1, any sum x can be collected with the help of greedy algorithm. However, greedy algorithm does not always give the optimal representation of the sum, i.e. the representation with the minimum amount of coins. For example, if there are face values {1, 3, 4} and it is asked to collect the sum 6, greedy algorithm will represent the sum as 4 + 1 + 1, while the optimal representation is 3 + 3, containing one coin less. By the given set of face values find out if there exist such a sum x that greedy algorithm will collect in a non-optimal way. If such a sum exists, find out the smallest of these sums.

The first line contains an integer n (1 ≤ n ≤ 400) — the amount of the coins' face values. The second line contains n integers ai (1 ≤ ai ≤ 109), describing the face values. It is guaranteed that a1 > a2 > ... > an and an = 1.

If greedy algorithm collects any sum in an optimal way, output -1. Otherwise output the smallest sum that greedy algorithm collects in a non-optimal way.
Tags: constructivealgorithms,*2600
'''

def smallest_non_optimal_sum(n, values):
    max_limit = 10000  # Maximum limit for checking sums
    
    # Sort values and confirm last is 1 as guaranteed
    coins = sorted(values, reverse=True)
    
    # Create a DP array to find the optimal number of coins for each sum
    dp = [float('inf')] * (max_limit + 1)
    dp[0] = 0  # Base case: 0 coins needed to make the sum of 0
    
    # Fill out the DP table
    for coin in coins:
        for amount in range(coin, max_limit + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # Check each possible sum using greedy vs. optimal (DP) method
    for x in range(1, max_limit + 1):
        remaining = x
        greedy_count = 0
        
        # Perform a greedy coin count simulation
        for coin in coins:
            if remaining >= coin:
                greedy_count += remaining // coin
                remaining %= coin
        
        # If greedy requires more coins than dp, it's a non-optimal sum
        if greedy_count > dp[x]:
            return x
    
    # Return -1 if all sums up to max_limit are optimal
    return -1

# Test example
coins_example = [4, 3, 1]
expected_output = 6

# Invoke the solution
actual_output = smallest_non_optimal_sum(len(coins_example), coins_example)

# Verification
if actual_output == expected_output:
    print("verified")
else:
    print(f"Failed, expected {expected_output} but got {actual_output}")