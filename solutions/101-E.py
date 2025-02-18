'''
Problem id: 101-E
Statement: Little Gerald and his coach Mike play an interesting game. At the beginning of the game there is a pile consisting of n candies and a pile consisting of m stones. Gerald and Mike move in turns, Mike goes first. During his move Mike checks how many candies and stones Gerald has eaten. Let Gerald eat a candies and b stones. Then Mike awards Gerald f(a, b) prize points. Gerald during his move either eats a candy from the pile of candies or a stone from the pile of stones. As Mike sees that Gerald has eaten everything apart one candy and one stone, he awards points for the last time and the game ends. Gerald is not allowed to eat all the candies, and he is not allowed to eat all the stones too. Tell Gerald how to play to get the largest possible number of points: it is required to find one of the possible optimal playing strategies for Gerald.

The first line contains three integers n, m, p (1 ≤ n, m ≤ 20000, 1 ≤ p ≤ 109). The second line contains n integers x0, x1, ..., xn - 1 (0 ≤ xi ≤ 20000). The third line contains m integers y0, y1, ..., ym - 1 (0 ≤ yi ≤ 20000). The value of f(a, b) is calculated as a remainder of the division of the sum xa + yb by number p.

Print on the first line the only number: the maximal number of points Gerald can earn. Print on the second line a sting consisting of n + m - 2 characters, each of which is either a "C" or "S", the i-th character should be "C" if Gerald's i-th move should be eating a candy and "S" if he should eat a stone.

In the first test if Gerald's first move is eating a stone, he will receive a point for it and if he eats a candy, he will get zero pints. In any way Gerald will get 0 points before his first move, and 1 after his second one. This, the maximum number of points Gerald can get equals to 2, and for that he should first eat a stone, then a candy.
Tags: divideandconquer,dp,*2500
'''

def max_points_and_strategy(n, m, p, candies, stones):
    # Precompute x_i % p for candies and y_j % p for stones
    x_mod = [x % p for x in candies]
    y_mod = [y % p for y in stones]
    
    # Find maximum of mod values
    max_candy_mod = max(x_mod)
    max_stone_mod = max(y_mod)

    # Determine the optimal sequence based on maximum mod values
    # If max candy mod >= max stone mod consume more candies otherwise consume more stones
    path = []
    if max_candy_mod >= max_stone_mod:
        # Consume candies first as long as we don’t eat them all
        path.extend(['C'] * (n - 1))  # leave one candy
        path.extend(['S'] * (m - 2))  # leave one stone
    else:
        # Consume stones first as long as we don’t eat them all
        path.extend(['S'] * (m - 1))  # leave one stone
        path.extend(['C'] * (n - 2))  # leave one candy

    # Calculate the maximum possible score
    max_possible_score = (max_candy_mod + max_stone_mod) % p
    
    return max_possible_score, ''.join(path)

# Define verification test function

def test_max_points_and_strategy():
    n = 3
    m = 3
    p = 10
    candies = [1, 2, 3]
    stones = [4, 5, 6]
    
    # In this simple test setup, expected max_points is determined by sum(max of candy mod, max of stone mod) % p
    # Since max candy mod = 3, and max stone mod = 6, max_points = (3 + 6) % 10 = 9
    expected_max_points = (3 + 6) % 10
    # The sequence path can vary but maintains structure e.g. "CCS" or "SSC"
    result = max_points_and_strategy(n, m, p, candies, stones)
    possible_strategies = ['CCS', 'SSC']
    
    if result[0] == expected_max_points and result[1] in possible_strategies:
        print('verified')
    else:
        print(f'incorrect: got {result}, expected max points {expected_max_points} with possible strategies {possible_strategies}')

# Call verification test function
test_max_points_and_strategy()