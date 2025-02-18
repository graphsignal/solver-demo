'''
Problem id: 1005-D
Statement: Polycarp likes numbers that are divisible by 3.

He has a huge number $$$s$$$. Polycarp wants to cut from it the maximum number of numbers that are divisible by $$$3$$$. To do this, he makes an arbitrary number of vertical cuts between pairs of adjacent digits. As a result, after $$$m$$$ such cuts, there will be $$$m+1$$$ parts in total. Polycarp analyzes each of the obtained numbers and finds the number of those that are divisible by $$$3$$$.

For example, if the original number is $$$s=3121$$$, then Polycarp can cut it into three parts with two cuts: $$$3|1|21$$$. As a result, he will get two numbers that are divisible by $$$3$$$.

Polycarp can make an arbitrary number of vertical cuts, where each cut is made between a pair of adjacent digits. The resulting numbers cannot contain extra leading zeroes (that is, the number can begin with 0 if and only if this number is exactly one character '0'). For example, 007, 01 and 00099 are not valid numbers, but 90, 0 and 10001 are valid.

What is the maximum number of numbers divisible by $$$3$$$ that Polycarp can obtain?

The first line of the input contains a positive integer $$$s$$$. The number of digits of the number $$$s$$$ is between $$$1$$$ and $$$2\cdot10^5$$$, inclusive. The first (leftmost) digit is not equal to 0.

Print the maximum number of numbers divisible by $$$3$$$ that Polycarp can get by making vertical cuts in the given number $$$s$$$.

In the first example, an example set of optimal cuts on the number is 3|1|21.

In the second example, you do not need to make any cuts. The specified number 6 forms one number that is divisible by $$$3$$$.

In the third example, cuts must be made between each pair of digits. As a result, Polycarp gets one digit 1 and $$$33$$$ digits 0. Each of the $$$33$$$ digits 0 forms a number that is divisible by $$$3$$$.

In the fourth example, an example set of optimal cuts is 2|0|1|9|201|81. The numbers $$$0$$$, $$$9$$$, $$$201$$$ and $$$81$$$ are divisible by $$$3$$$.
Tags: dp,greedy,numbertheory,*1500
'''

def max_divisible_by_3_segments(s: str) -> int:
    sum_so_far = 0
    cut_count = 0
    for digit in s:
        sum_so_far += int(digit)
        if sum_so_far % 3 == 0:
            cut_count += 1
            sum_so_far = 0
    return cut_count

# Test the function
# Given examples:
# 1. s = "3121"; segments: 3, 1, 21 -> 2 segments (3, 21) divisible by 3.
# 2. s = "6"; full number divisible by 3, so result is 1.
# 3. s = "100000"; segments: 1, followed by 5 zeros -> 5 zeros count as segments, so result is 5.
# 4. s = "201920181"; optimally segmented into 2, 0, 1, 9, 201, 81 -> 4 segments divisible by 3 (0, 9, 201, 81)

test_cases = {
    "3121": 2,
    "6": 1,
    "100000": 5,
    "201920181": 4
}

all_verified = True
for s, expected in test_cases.items():
    result = max_divisible_by_3_segments(s)
    if result == expected:
        print(f"Test case {s}: verified")
    else:
        print(f"Test case {s}: failed (actual: {result}, expected: {expected})")
        all_verified = False

if all_verified:
    print("All test cases verified.")
else:
    print("Some test cases failed.")