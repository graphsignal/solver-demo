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

def count_possible_positions(n, d, hotels):
    positions = set()
    
    for x_i in hotels:
        # Check position x_i - d
        if all(abs(x_j - (x_i - d)) >= d for x_j in hotels):
            positions.add(x_i - d)
        
        # Check position x_i + d
        if all(abs(x_j - (x_i + d)) >= d for x_j in hotels):
            positions.add(x_i + d)
    
    return len(positions)

# Test case verification
def verify_case():
    # Test case from the problem statement
    n1, d1 = 3, 3
    hotels1 = [0, 3, 7]
    expected1 = 6  # From the example given in the problem
    result1 = count_possible_positions(n1, d1, hotels1)
    
    if result1 == expected1:
        print("Test case 1: verified")
    else:
        print(f"Test case 1: incorrect, expected {expected1} but got {result1}")
    
    # Additional test case
    n2, d2 = 5, 2
    hotels2 = [0, 4, 8, 12, 14]
    expected2 = 5
    result2 = count_possible_positions(n2, d2, hotels2)
    
    if result2 == expected2:
        print("Test case 2: verified")
    else:
        print(f"Test case 2: incorrect, expected {expected2} but got {result2}")
    
verify_case()