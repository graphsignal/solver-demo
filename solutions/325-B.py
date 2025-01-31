def compute_games(m):
    total_games = 0
    while m > 5:  # Continue until we reach a round robin situation
        games = m // 2
        total_games += games
        m -= games
    # Round robin if there are 5 or fewer teams
    total_games += m * (m - 1) // 2
    return total_games


def find_possible_teams(n):
    results = []
    # We consider up to a practical limit for initial teams
    # The choice here for limit is arbitrary, considering large numbers for `m` might result
    # in very large number of games exceeding n far too quickly without practical need
    for m in range(1, min(10**6, 2 * n) + 1):  # increased limit to 2 * n
        if compute_games(m) == n:
            results.append(m)
    if results:
        return results
    else:
        return [-1]


def test_find_possible_teams():
    # Example case from statement
    n = 25  # It should be 20 teams for exactly 25 games
    expected = [20]
    result = find_possible_teams(n)
    if result == expected:
        print("verified")
    else:
        print(f"Test failed: expected {expected}, got {result}")

# Call the test function
test_find_possible_teams()