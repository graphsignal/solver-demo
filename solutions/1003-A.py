'''
Problem id: 1003-A
Statement: Polycarp has $$$n$$$ coins, the value of the $$$i$$$-th coin is $$$a_i$$$. Polycarp wants to distribute all the coins between his pockets, but he cannot put two coins with the same value into the same pocket.

For example, if Polycarp has got six coins represented as an array $$$a = [1, 2, 4, 3, 3, 2]$$$, he can distribute the coins into two pockets as follows: $$$[1, 2, 3], [2, 3, 4]$$$.

Polycarp wants to distribute all the coins with the minimum number of used pockets. Help him to do that.

The first line of the input contains one integer $$$n$$$ ($$$1 \le n \le 100$$$) — the number of coins.

The second line of the input contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 100$$$) — values of coins.

Print only one integer — the minimum number of pockets Polycarp needs to distribute all the coins so no two coins with the same value are put into the same pocket.
Tags: implementation,*800
'''

def minimum_pockets(n, coins):
    # Step 1: Initialize frequency array of size 101
    frequency = [0] * 101
    
    # Step 2: Count the frequency of each coin value
    for coin in coins:
        frequency[coin] += 1
    
    # Step 3: Find the maximum frequency
    max_frequency = max(frequency)
    
    # Step 4: The minimum number of pockets required
    return max_frequency

# Verification function

def verify_minimum_pockets():
    # Test case
    coins = [1, 2, 4, 3, 3, 2]
    n = len(coins)
    expected_result = 2  # As explained in the example
    result = minimum_pockets(n, coins)
    if result == expected_result:
        print("verified")
    else:
        print(f"Incorrect result. Expected {expected_result}, but got {result}.")

# Call verify function
verify_minimum_pockets()