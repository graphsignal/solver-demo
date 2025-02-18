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

def tournament_games(t):
    """
    Calculate the total number of games played in the tournament if we start with `t` teams.
    """
    games = 0
    while t > 1:
        # Even elimination rounds
        games += t // 2
        t = (t + 1) // 2  # Advance half the teams; if odd, round up a team
        
        # If we reach 2 or less teams, consider round-robin games
        if t == 2:
            games += 1  # Only one game needed if two teams remain
            break
    return games


def find_possible_teams(n):
    """
    Find all possible numbers of teams that result in exactly n games being played.
    """
    if n < 1:
        return [-1]

    candidates = []
    t = 2
    while True:
        games = tournament_games(t)
        if games > n:
            break
        if games == n:
            candidates.append(t)
        t += 1

    return candidates if candidates else [-1]


def verify_solution(solution, expected):
    if solution == expected:
        print("verified")
    else:
        print(f"Failed: Expected {expected}, but got {solution}")

# Example verification
test_n = 25
expected_output = [20]  # Notice that expected output needs to be verified if accurate
result = find_possible_teams(test_n)
verify_solution(result, expected_output)

# Additional test cases
# Here we should adjust the expected outputs based on verified computations
# Let's re-evaluate using smaller known values to ensure the algorithm is behaving as expected.
additional_tests = [
    (1, [-1]),  # Not enough rounds for meaningful game
    (2, [3]),  # When n=2, should have 3 teams
    (3, [4]),  # With 4 teams, we have 3 initial rounds (2 eliminations and 1 final)
    (6, [5]),  # For n=6, should have 5 teams
]

for n, expected in additional_tests:
    result = find_possible_teams(n)
    verify_solution(result, expected)