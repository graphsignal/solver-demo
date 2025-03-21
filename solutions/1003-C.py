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

def find_maximum_average_temperature(n, k, temperatures):
    # Step 1: Compute prefix sums
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + temperatures[i]

    # Step 2: Track maximum average
    max_average = float('-inf')

    # Step 3: Evaluate all segments of at least k days
    for i in range(n):
        for j in range(i + k - 1, n):
            segment_sum = prefix_sum[j + 1] - prefix_sum[i]
            segment_length = j - i + 1
            average = segment_sum / segment_length
            if average > max_average:
                max_average = average

    return max_average

# Test the function with a sample input
# Test case: n = 4, k = 3, temperatures = [3, 4, 1, 2]
# Expected result can be calculated by hand:
# Max averages will be (3+4+1)/3 = 8/3 = 2.6667, (4+1+2)/3 = 7/3 = 2.3333, and (3+4+1+2)/4 = 10/4 = 2.5.
# Thus, the maximum average of segments of at least 3 days is 2.6667.

def verify_result():
    n = 4
    k = 3
    temperatures = [3, 4, 1, 2]
    expected = 2.6666666666666665  # Approximately 2.6667
    result = find_maximum_average_temperature(n, k, temperatures)
    if abs(result - expected) < 1e-6:
        print('verified')
    else:
        print(f'incorrect: actual result = {result}, expected = {expected}')

verify_result()