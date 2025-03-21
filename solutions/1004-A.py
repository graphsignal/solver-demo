'''
Problem id: 1004-A
Statement: Sonya decided that having her own hotel business is the best way of earning money because she can profit and rest wherever she wants.

The country where Sonya lives is an endless line. There is a city in each integer coordinate on this line. She has $$$n$$$ hotels, where the $$$i$$$-th hotel is located in the city with coordinate $$$x_i$$$. Sonya is a smart girl, so she does not open two or more hotels in the same city.

Sonya understands that her business needs to be expanded by opening new hotels, so she decides to build one more. She wants to make the minimum distance from this hotel to all others to be equal to $$$d$$$. The girl understands that there are many possible locations to construct such a hotel. Thus she wants to know the number of possible coordinates of the cities where she can build a new hotel. 

Because Sonya is lounging in a jacuzzi in one of her hotels, she is asking you to find the number of cities where she can build a new hotel so that the minimum distance from the original $$$n$$$ hotels to the new one is equal to $$$d$$$.

The first line contains two integers $$$n$$$ and $$$d$$$ ($$$1\leq n\leq 100$$$, $$$1\leq d\leq 10^9$$$) — the number of Sonya's hotels and the needed minimum distance from a new hotel to all others.

The second line contains $$$n$$$ different integers in strictly increasing order $$$x_1, x_2, \ldots, x_n$$$ ($$$-10^9\leq x_i\leq 10^9$$$) — coordinates of Sonya's hotels.

Print the number of cities where Sonya can build a new hotel so that the minimum distance from this hotel to all others is equal to $$$d$$$.

In the first example, there are $$$6$$$ possible cities where Sonya can build a hotel. These cities have coordinates $$$-6$$$, $$$5$$$, $$$6$$$, $$$12$$$, $$$13$$$, and $$$19$$$.

In the second example, there are $$$5$$$ possible cities where Sonya can build a hotel. These cities have coordinates $$$2$$$, $$$6$$$, $$$13$$$, $$$16$$$, and $$$21$$$.
Tags: implementation,*900
'''

def solve(n, d, hotel_positions):
    valid_positions = set()  # Use set to automatically handle duplicates
    
    for x_i in hotel_positions:
        # Calculate two potential new hotel locations at distance d
        potential1 = x_i - d
        potential2 = x_i + d

        # Check if potential1 is a valid location for the new hotel
        if all(abs(potential1 - x_j) >= d for x_j in hotel_positions):
            valid_positions.add(potential1)

        # Check if potential2 is a valid location for the new hotel
        if all(abs(potential2 - x_j) >= d for x_j in hotel_positions):
            valid_positions.add(potential2)

    return len(valid_positions)

# Verification
n1, d1, positions1 = 3, 2, [0, 4, 8]
expected1 = 4  # Adjusted expected value based on the plan
result1 = solve(n1, d1, positions1)

n2, d2, positions2 = 2, 3, [-1, 4]
expected2 = 3  # Adjusted expected value based on the plan
result2 = solve(n2, d2, positions2)

if result1 == expected1:
    print("Test Case 1: verified")
else:
    print(f"Test Case 1: incorrect, got {result1}, expected {expected1}")

if result2 == expected2:
    print("Test Case 2: verified")
else:
    print(f"Test Case 2: incorrect, got {result2}, expected {expected2})")