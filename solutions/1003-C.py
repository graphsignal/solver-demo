'''
Problem id: 1003-C
Statement: The heat during the last few days has been really intense. Scientists from all over the Berland study how the temperatures and weather change, and they claim that this summer is abnormally hot. But any scientific claim sounds a lot more reasonable if there are some numbers involved, so they have decided to actually calculate some value which would represent how high the temperatures are.

Mathematicians of Berland State University came up with a special heat intensity value. This value is calculated as follows:

Suppose we want to analyze the segment of $$$n$$$ consecutive days. We have measured the temperatures during these $$$n$$$ days; the temperature during $$$i$$$-th day equals $$$a_i$$$.

We denote the average temperature of a segment of some consecutive days as the arithmetic mean of the temperature measures during this segment of days. So, if we want to analyze the average temperature from day $$$x$$$ to day $$$y$$$, we calculate it as $$$\frac{\sum \limits_{i = x}^{y} a_i}{y - x + 1}$$$ (note that division is performed without any rounding). The heat intensity value is the maximum of average temperatures over all segments of not less than $$$k$$$ consecutive days. For example, if analyzing the measures $$$[3, 4, 1, 2]$$$ and $$$k = 3$$$, we are interested in segments $$$[3, 4, 1]$$$, $$$[4, 1, 2]$$$ and $$$[3, 4, 1, 2]$$$ (we want to find the maximum value of average temperature over these segments).

You have been hired by Berland State University to write a program that would compute the heat intensity value of a given period of days. Are you up to this task?

The first line contains two integers $$$n$$$ and $$$k$$$ ($$$1 \le k \le n \le 5000$$$) — the number of days in the given period, and the minimum number of days in a segment we consider when calculating heat intensity value, respectively.

The second line contains $$$n$$$ integers $$$a_1$$$, $$$a_2$$$, ..., $$$a_n$$$ ($$$1 \le a_i \le 5000$$$) — the temperature measures during given $$$n$$$ days.

Print one real number — the heat intensity value, i. e., the maximum of average temperatures over all segments of not less than $$$k$$$ consecutive days.

Your answer will be considered correct if the following condition holds: $$$|res - res_0| < 10^{-6}$$$, where $$$res$$$ is your answer, and $$$res_0$$$ is the answer given by the jury's solution.
Tags: bruteforce,implementation,math,*1300
'''

def calculate_heat_intensity(n, k, temperatures):
    # Compute prefix sum array
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + temperatures[i]

    # Initialize maximum average
    max_avg = 0.0

    # Iterate over all starting positions
    for start in range(n):
        for length in range(k, n - start + 1):
            sum_segment = prefix[start + length] - prefix[start]
            avg = sum_segment / length
            if avg > max_avg:
                max_avg = avg

    return max_avg

# Fix expected result based on correct understanding
n_test = 4
k_test = 3
temperatures_test = [3, 4, 1, 2]
expected_output = 2.6666666666666665 # The correct segment average as per previous explanation.

# Run the function
actual_output = calculate_heat_intensity(n_test, k_test, temperatures_test)

# Verify the output
if abs(actual_output - expected_output) < 1e-6:
    print('verified')
else:
    print('incorrect result')
    print(f'Actual: {actual_output}, Expected: {expected_output})')