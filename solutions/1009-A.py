'''
Problem id: 1009-A
Statement: Maxim wants to buy some games at the local game shop. There are $$$n$$$ games in the shop, the $$$i$$$-th game costs $$$c_i$$$.

Maxim has a wallet which can be represented as an array of integers. His wallet contains $$$m$$$ bills, the $$$j$$$-th bill has value $$$a_j$$$.

Games in the shop are ordered from left to right, Maxim tries to buy every game in that order.

When Maxim stands at the position $$$i$$$ in the shop, he takes the first bill from his wallet (if his wallet is empty then he proceeds to the next position immediately) and tries to buy the $$$i$$$-th game using this bill. After Maxim tried to buy the $$$n$$$-th game, he leaves the shop.

Maxim buys the $$$i$$$-th game if and only if the value of the first bill (which he takes) from his wallet is greater or equal to the cost of the $$$i$$$-th game. If he successfully buys the $$$i$$$-th game, the first bill from his wallet disappears and the next bill becomes first. Otherwise Maxim leaves the first bill in his wallet (this bill still remains the first one) and proceeds to the next game.

For example, for array $$$c = [2, 4, 5, 2, 4]$$$ and array $$$a = [5, 3, 4, 6]$$$ the following process takes place: Maxim buys the first game using the first bill (its value is $$$5$$$), the bill disappears, after that the second bill (with value $$$3$$$) becomes the first one in Maxim's wallet, then Maxim doesn't buy the second game because $$$c_2 > a_2$$$, the same with the third game, then he buys the fourth game using the bill of value $$$a_2$$$ (the third bill becomes the first one in Maxim's wallet) and buys the fifth game using the bill of value $$$a_3$$$.

Your task is to get the number of games Maxim will buy.

The first line of the input contains two integers $$$n$$$ and $$$m$$$ ($$$1 \le n, m \le 1000$$$) — the number of games and the number of bills in Maxim's wallet.

The second line of the input contains $$$n$$$ integers $$$c_1, c_2, \dots, c_n$$$ ($$$1 \le c_i \le 1000$$$), where $$$c_i$$$ is the cost of the $$$i$$$-th game.

The third line of the input contains $$$m$$$ integers $$$a_1, a_2, \dots, a_m$$$ ($$$1 \le a_j \le 1000$$$), where $$$a_j$$$ is the value of the $$$j$$$-th bill from the Maxim's wallet.

Print a single integer — the number of games Maxim will buy.

The first example is described in the problem statement.

In the second example Maxim cannot buy any game because the value of the first bill in his wallet is smaller than the cost of any game in the shop.

In the third example the values of the bills in Maxim's wallet are large enough to buy any game he encounter until he runs out of bills in his wallet.
Tags: implementation,*800
'''

def number_of_games_bought(n, m, c, a):
    i = 0  # index for games
    j = 0  # index for bills
    count_games = 0  # to count games bought
    
    while i < n and j < m:
        if a[j] >= c[i]:
            # buy the game
            count_games += 1
            j += 1  # move to the next bill
        i += 1  # move to the next game
    
    return count_games

# Test case 1: described in the problem statement
n1, m1 = 5, 4
c1 = [2, 4, 5, 2, 4]
a1 = [5, 3, 4, 6]
expected1 = 3

# Test case 2: cannot buy any game
n2, m2 = 2, 3
c2 = [5, 6]
a2 = [2, 2, 2]
expected2 = 0

# Test case 3: enough large bills
n3, m3 = 3, 3
c3 = [2, 4, 3]
a3 = [10, 10, 10]
expected3 = 3

assert number_of_games_bought(n1, m1, c1, a1) == expected1, f"Test 1 failed: expected {expected1}, got {number_of_games_bought(n1, m1, c1, a1)}"
assert number_of_games_bought(n2, m2, c2, a2) == expected2, f"Test 2 failed: expected {expected2}, got {number_of_games_bought(n2, m2, c2, a2)}"
assert number_of_games_bought(n3, m3, c3, a3) == expected3, f"Test 3 failed: expected {expected3}, got {number_of_games_bought(n3, m3, c3, a3)}"

print('All test cases verified!')