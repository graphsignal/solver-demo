'''
Problem id: 325-B
Statement: Daniel is organizing a football tournament. He has come up with the following tournament format: 

For example, if there were 20 teams initially, they would begin by playing 10 games. So, 10 teams would be eliminated, and the remaining 10 would play 5 games. Then the remaining 5 teams would play 10 games in a round robin tournament. In total there would be 10+5+10=25 games.

Daniel has already booked the stadium for n games. Help him to determine how many teams he should invite so that the tournament needs exactly n games. You should print all possible numbers of teams that will yield exactly n games in ascending order, or -1 if there are no such numbers.

The first line contains a single integer n (1 ≤ n ≤ 1018), the number of games that should be played.

Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is preferred to use the cin, cout streams or the %I64d specifier.

Print all possible numbers of invited teams in ascending order, one per line. If exactly n games cannot be played, output one number: -1.
Tags: binarysearch,math,*1800
'''

def tournament_games(n):
    def calculate_games(T):
        games = 0
        while T > 1:
            if T % 2 == 0:
                games += T // 2
                T //= 2
            else:
                break
        if T > 1:
            games += (T * (T-1)) // 2
        return games

    possible_teams = []
    # Try every possible number of teams up to some reasonable bound
    # Let's use a heuristic upper bound
    upper_bound = 10**6  # This is a rough heuristic. For more precise bound use another method
    for T in range(2, upper_bound + 1, 2):  # Start from 2, check only even, increment by 2
        if calculate_games(T) == n:
            possible_teams.append(T)

    return possible_teams if possible_teams else [-1]

# A test verification call
def verify():
    test_n = 25  # From the example case considered in problem description
    expected_output = [20]
    result = tournament_games(test_n)
    if result == expected_output:
        print("verified")
    else:
        print(f"Test failed for n={test_n}.\nExpected {expected_output} but got {result}.")

verify()