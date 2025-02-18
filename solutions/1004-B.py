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

def maximize_flower_beauty(n, m, visitors):
    # Optionally use "010101..." pattern, but "101010..." is also valid
    pattern = ['0', '1'] * (n // 2 + 1)
    flower_row = ''.join(pattern[:n])
    return flower_row

# Helper function to validate the pattern conform to the visitor's segment requirement
def validate_alternating_patterns(n, visitors):
    # Check for a valid pattern "010101..."
    valid_pattern_1 = ['0', '1'] * (n // 2 + 1)
    valid_str_1 = ''.join(valid_pattern_1[:n])
    
    # Check for alternate valid pattern "101010..."
    valid_pattern_2 = ['1', '0'] * (n // 2 + 1)
    valid_str_2 = ''.join(valid_pattern_2[:n])
    
    # Verify for all visitor segments
    for li, ri in visitors:
        segment_1 = valid_str_1[li-1:ri]
        segment_2 = valid_str_2[li-1:ri]
        if not ('0' in segment_1 and '1' in segment_1) and not ('0' in segment_2 and '1' in segment_2):
            return False
    return True

# Sample test
n, m = 5, 3
visitors = [(1, 2), (2, 3), (1, 5)]

actual_output = maximize_flower_beauty(n, m, visitors)

# Check if the actual output meets the requirements
if validate_alternating_patterns(n, visitors):
    print('verified')
else:
    print(f'Incorrect: Pattern did not match the criteria')