'''
Problem id: 1004-B
Statement: Sonya decided to organize an exhibition of flowers. Since the girl likes only roses and lilies, she decided that only these two kinds of flowers should be in this exhibition.

There are $$$n$$$ flowers in a row in the exhibition. Sonya can put either a rose or a lily in the $$$i$$$-th position. Thus each of $$$n$$$ positions should contain exactly one flower: a rose or a lily.

She knows that exactly $$$m$$$ people will visit this exhibition. The $$$i$$$-th visitor will visit all flowers from $$$l_i$$$ to $$$r_i$$$ inclusive. The girl knows that each segment has its own beauty that is equal to the product of the number of roses and the number of lilies.

Sonya wants her exhibition to be liked by a lot of people. That is why she wants to put the flowers in such way that the sum of beauties of all segments would be maximum possible.

The first line contains two integers $$$n$$$ and $$$m$$$ ($$$1\leq n, m\leq 10^3$$$) — the number of flowers and visitors respectively.

Each of the next $$$m$$$ lines contains two integers $$$l_i$$$ and $$$r_i$$$ ($$$1\leq l_i\leq r_i\leq n$$$), meaning that $$$i$$$-th visitor will visit all flowers from $$$l_i$$$ to $$$r_i$$$ inclusive.

Print the string of $$$n$$$ characters. The $$$i$$$-th symbol should be «0» if you want to put a rose in the $$$i$$$-th position, otherwise «1» if you want to put a lily.

If there are multiple answers, print any.

In the first example, Sonya can put roses in the first, fourth, and fifth positions, and lilies in the second and third positions;

The total beauty is equal to $$$2+2+4=8$$$.

In the second example, Sonya can put roses in the third, fourth, and sixth positions, and lilies in the first, second, and fifth positions;

The total beauty is equal to $$$1+4+2=7$$$.
Tags: constructivealgorithms,greedy,implementation,math,*1300
'''

def maximize_beauty(n, m, segments):
    # We will create an alternating pattern of flowers (0 - rose, 1 - lily)
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

# Verification based on expected outcomes.
def verify_solution():
    # Example case 1: 
    n1, m1 = 5, 3
    segments1 = [(1, 2), (2, 3), (1, 5)]  # segments aren't used in the solution calculation
    result1 = maximize_beauty(n1, m1, segments1)
    expected1_possibilities = {"01010", "10101"}  # Either alternating sequence is valid
    
    # Example case 2: 
    n2, m2 = 6, 3
    segments2 = [(1, 1), (2, 5), (3, 6)]
    result2 = maximize_beauty(n2, m2, segments2)
    expected2_possibilities = {"010101", "101010"}  # Either alternating sequence is valid
    
    if result1 in expected1_possibilities:
        print("Case 1 verified")
    else:
        print(f"Case 1 incorrect. Got {result1}, expected one of {expected1_possibilities}")
        
    if result2 in expected2_possibilities:
        print("Case 2 verified")
    else:
        print(f"Case 2 incorrect. Got {result2}, expected one of {expected2_possibilities}")

verify_solution()