'''
Problem id: 10-A
Statement: Tom is interested in power consumption of his favourite laptop. His laptop has three modes. In normal mode laptop consumes P1 watt per minute. T1 minutes after Tom moved the mouse or touched the keyboard for the last time, a screensaver starts and power consumption changes to P2 watt per minute. Finally, after T2 minutes from the start of the screensaver, laptop switches to the "sleep" mode and consumes P3 watt per minute. If Tom moves the mouse or touches the keyboard when the laptop is in the second or in the third mode, it switches to the first (normal) mode. Tom's work with the laptop can be divided into n time periods [l1, r1], [l2, r2], ..., [ln, rn]. During each interval Tom continuously moves the mouse and presses buttons on the keyboard. Between the periods Tom stays away from the laptop. Find out the total amount of power consumed by the laptop during the period [l1, rn].

The first line contains 6 integer numbers n, P1, P2, P3, T1, T2 (1 ≤ n ≤ 100, 0 ≤ P1, P2, P3 ≤ 100, 1 ≤ T1, T2 ≤ 60). The following n lines contain description of Tom's work. Each i-th of these lines contains two space-separated integers li and ri (0 ≤ li < ri ≤ 1440, ri < li + 1 for i < n), which stand for the start and the end of the i-th period of work.

Output the answer to the problem.
Tags: implementation,*900
'''

def calculate_total_power(n, P1, P2, P3, T1, T2, intervals):
    total_power = 0
    current_time = intervals[0][0]

    # Process each interval
    for idx in range(n):
        li, ri = intervals[idx]

        if idx > 0:
            # Calculate the inactive period between previous end and current start
            inactive_duration = li - intervals[idx-1][1]

            # Compute power consumption during inactive period
            if inactive_duration > 0:
                # Idle time less than or equal to T1
                if inactive_duration <= T1:
                    total_power += inactive_duration * P1
                else:
                    # First T1 minutes: P1 watts
                    total_power += T1 * P1
                    remaining_time = inactive_duration - T1

                    # Next up to T2 minutes: P2 watts
                    if remaining_time <= T2:
                        total_power += remaining_time * P2
                    else:
                        total_power += T2 * P2
                        remaining_time -= T2

                        # Remaining time: P3 watts
                        total_power += remaining_time * P3

        # Add power consumption for the current active interval
        total_power += (ri - li) * P1

    return total_power

# Test the function with sample input
n, P1, P2, P3, T1, T2 = 1, 10, 5, 1, 10, 20
intervals = [(0, 30)]
expected_output = (30 * P1)  # Active period 0 to 30
result = calculate_total_power(n, P1, P2, P3, T1, T2, intervals)

if result == expected_output:
    print("verified")
else:
    print(f"Test failed: expected {expected_output}, got {result}")