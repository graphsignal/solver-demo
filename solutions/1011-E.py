'''
Problem id: 1011-E
Statement: Astronaut Natasha arrived on Mars. She knows that the Martians are very poor aliens. To ensure a better life for the Mars citizens, their emperor decided to take tax from every tourist who visited the planet. Natasha is the inhabitant of Earth, therefore she had to pay the tax to enter the territory of Mars.

There are $$$n$$$ banknote denominations on Mars: the value of $$$i$$$-th banknote is $$$a_i$$$. Natasha has an infinite number of banknotes of each denomination.

Martians have $$$k$$$ fingers on their hands, so they use a number system with base $$$k$$$. In addition, the Martians consider the digit $$$d$$$ (in the number system with base $$$k$$$) divine. Thus, if the last digit in Natasha's tax amount written in the number system with the base $$$k$$$ is $$$d$$$, the Martians will be happy. Unfortunately, Natasha does not know the Martians' divine digit yet.

Determine for which values $$$d$$$ Natasha can make the Martians happy.

Natasha can use only her banknotes. Martians don't give her change.

The first line contains two integers $$$n$$$ and $$$k$$$ ($$$1 \le n \le 100\,000$$$, $$$2 \le k \le 100\,000$$$) — the number of denominations of banknotes and the base of the number system on Mars.

The second line contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \le a_i \le 10^9$$$) — denominations of banknotes on Mars.

All numbers are given in decimal notation.

On the first line output the number of values $$$d$$$ for which Natasha can make the Martians happy.

In the second line, output all these values in increasing order.

Print all numbers in decimal notation.

Consider the first test case. It uses the octal number system.

If you take one banknote with the value of $$$12$$$, you will get $$$14_8$$$ in octal system. The last digit is $$$4_8$$$.

If you take one banknote with the value of $$$12$$$ and one banknote with the value of $$$20$$$, the total value will be $$$32$$$. In the octal system, it is $$$40_8$$$. The last digit is $$$0_8$$$.

If you take two banknotes with the value of $$$20$$$, the total value will be $$$40$$$, this is $$$50_8$$$ in the octal system. The last digit is $$$0_8$$$.

No other digits other than $$$0_8$$$ and $$$4_8$$$ can be obtained. Digits $$$0_8$$$ and $$$4_8$$$ could also be obtained in other ways.

The second test case uses the decimal number system. The nominals of all banknotes end with zero, so Natasha can give the Martians only the amount whose decimal notation also ends with zero.
Tags: numbertheory,*1800
'''

def solution(n, k, denominations):
    from math import gcd
    from functools import reduce
    
    # Calculate remaining of each denomination modulo k
    modulos = [a % k for a in denominations]
    
    # Find gcd of these modulos
    g = reduce(gcd, modulos)
    
    # Find all multiples of g that are less than k
    possible_d = list(range(0, k, g))
    
    return len(possible_d), possible_d

# Test example:
# Example 1:
n1 = 2
k1 = 8
denominations1 = [12, 20]
expected_d1 = [0, 4]
expected_len1 = len(expected_d1)

# Get result from solution
result_len1, result_d1 = solution(n1, k1, denominations1)

# Verify the result for Example 1
if result_len1 == expected_len1 and result_d1 == expected_d1:
    print('verified')
else:
    print(f'Mismatch: Expected length {expected_len1}, got {result_len1} and expected d {expected_d1}, got {result_d1}')

# Example 2:
n2 = 3
k2 = 10
denominations2 = [60, 20, 30]
expected_d2 = [0]  # Since all multiples are of 10 and k is also 10
expected_len2 = len(expected_d2)

# Get result from solution
result_len2, result_d2 = solution(n2, k2, denominations2)

# Verify the result for Example 2
if result_len2 == expected_len2 and result_d2 == expected_d2:
    print('verified')
else:
    print(f'Mismatch: Expected length {expected_len2}, got {result_len2} and expected d {expected_d2}, got {result_d2}')