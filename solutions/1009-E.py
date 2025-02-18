'''
Problem id: 1009-E
Statement: Leha is planning his journey from Moscow to Saratov. He hates trains, so he has decided to get from one city to another by car.

The path from Moscow to Saratov can be represented as a straight line (well, it's not that straight in reality, but in this problem we will consider it to be straight), and the distance between Moscow and Saratov is $$$n$$$ km. Let's say that Moscow is situated at the point with coordinate $$$0$$$ km, and Saratov — at coordinate $$$n$$$ km.

Driving for a long time may be really difficult. Formally, if Leha has already covered $$$i$$$ kilometers since he stopped to have a rest, he considers the difficulty of covering $$$(i + 1)$$$-th kilometer as $$$a_{i + 1}$$$. It is guaranteed that for every $$$i \in [1, n - 1]$$$ $$$a_i \le a_{i + 1}$$$. The difficulty of the journey is denoted as the sum of difficulties of each kilometer in the journey.

Fortunately, there may be some rest sites between Moscow and Saratov. Every integer point from $$$1$$$ to $$$n - 1$$$ may contain a rest site. When Leha enters a rest site, he may have a rest, and the next kilometer will have difficulty $$$a_1$$$, the kilometer after it — difficulty $$$a_2$$$, and so on.

For example, if $$$n = 5$$$ and there is a rest site in coordinate $$$2$$$, the difficulty of journey will be $$$2a_1 + 2a_2 + a_3$$$: the first kilometer will have difficulty $$$a_1$$$, the second one — $$$a_2$$$, then Leha will have a rest, and the third kilometer will have difficulty $$$a_1$$$, the fourth — $$$a_2$$$, and the last one — $$$a_3$$$. Another example: if $$$n = 7$$$ and there are rest sites in coordinates $$$1$$$ and $$$5$$$, the difficulty of Leha's journey is $$$3a_1 + 2a_2 + a_3 + a_4$$$.

Leha doesn't know which integer points contain rest sites. So he has to consider every possible situation. Obviously, there are $$$2^{n - 1}$$$ different distributions of rest sites (two distributions are different if there exists some point $$$x$$$ such that it contains a rest site in exactly one of these distributions). Leha considers all these distributions to be equiprobable. He wants to calculate $$$p$$$ — the expected value of difficulty of his journey.

Obviously, $$$p \cdot 2^{n - 1}$$$ is an integer number. You have to calculate it modulo $$$998244353$$$.

The first line contains one number $$$n$$$ ($$$1 \le n \le 10^6$$$) — the distance from Moscow to Saratov.

The second line contains $$$n$$$ integer numbers $$$a_1$$$, $$$a_2$$$, ..., $$$a_n$$$ ($$$1 \le a_1 \le a_2 \le \dots \le a_n \le 10^6$$$), where $$$a_i$$$ is the difficulty of $$$i$$$-th kilometer after Leha has rested.

Print one number — $$$p \cdot 2^{n - 1}$$$, taken modulo $$$998244353$$$.
Tags: combinatorics,math,probabilities,*2000
'''

def calculate_difficulty(n, a):
    MOD = 998244353
    # Precompute powers of 2 modulo MOD
    power_of_2 = [1] * (n + 1)
    for i in range(1, n + 1):
        power_of_2[i] = (power_of_2[i - 1] * 2) % MOD

    # Calculate s = sum(a[i] * 2^(n-i) for all i)
    total_sum = 0
    for i in range(n):
        total_sum = (total_sum + a[i] * power_of_2[n - 1 - i]) % MOD

    return total_sum

# Function to verify the correctness of the function.
def verify():
    n = 5
    a = [1, 2, 3, 4, 5]
    # For this input, expected result should be:
    # 1*2^(4) + 2*2^(3) + 3*2^(2) + 4*2^(1) + 5*2^(0)
    expected_result = (1 * 16 + 2 * 8 + 3 * 4 + 4 * 2 + 5 * 1) % 998244353
    result = calculate_difficulty(n, a)
    if result == expected_result:
        print("verified")
    else:
        print(f"Verification failed: got {result}, expected {expected_result}")

verify()