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

def max_divisible_by_three(s):
    current_sum = 0
    count = 0
    
    for digit in s:
        current_sum += int(digit)
        
        if current_sum % 3 == 0:
            count += 1
            current_sum = 0
    
    return count

# Test the function with an example
# Let's use '3121', expecting the maximum parts divisible by 3 to be 2 (3|1|21)
sample_input = '3121'
expected_output = 2

# Calculate the result using the implemented function
actual_output = max_divisible_by_three(sample_input)

# Verify the output
if actual_output == expected_output:
    print('verified')
else:
    print(f'failed: expected {expected_output}, got {actual_output}')