'''
Problem id: 1010-C
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

def find_divine_numbers(n, k, denominations):
    # Initialize reachable as a set containing 0
    reachable = {0}
    for denomination in denominations:
        b_i = denomination % k
        new_reachable = set(reachable)  # Make copy of current reachable set
        for residue in reachable:
            new_residue = (residue + b_i) % k
            new_reachable.add(new_residue)
        reachable = new_reachable
    
    result = sorted(list(reachable))
    return len(result), result

# Example Test Cases
# Test Case 1
n1, k1 = 2, 8
A1 = [12, 20]
expected_output1 = (2, [0, 4])

# Test Case 2
n2, k2 = 2, 10
A2 = [10, 20]
expected_output2 = (1, [0])

# Verification and Output
output1 = find_divine_numbers(n1, k1, A1)
output2 = find_divine_numbers(n2, k2, A2)

# Verifying output
if output1 == expected_output1:
    print("Test Case 1: verified")
else:
    print(f"Test Case 1 failed! Expected {expected_output1}, but got {output1}")

if output2 == expected_output2:
    print("Test Case 2: verified")
else:
    print(f"Test Case 2 failed! Expected {expected_output2}, but got {output2}")

# Add more test cases as needed...