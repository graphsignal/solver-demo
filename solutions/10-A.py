'''
Problem id: 10-A
Statement: Tom is interested in power consumption of his favourite laptop. His laptop has three modes. In normal mode laptop consumes P1 watt per minute. T1 minutes after Tom moved the mouse or touched the keyboard for the last time, a screensaver starts and power consumption changes to P2 watt per minute. Finally, after T2 minutes from the start of the screensaver, laptop switches to the "sleep" mode and consumes P3 watt per minute. If Tom moves the mouse or touches the keyboard when the laptop is in the second or in the third mode, it switches to the first (normal) mode. Tom's work with the laptop can be divided into n time periods [l1, r1], [l2, r2], ..., [ln, rn]. During each interval Tom continuously moves the mouse and presses buttons on the keyboard. Between the periods Tom stays away from the laptop. Find out the total amount of power consumed by the laptop during the period [l1, rn].

The first line contains 6 integer numbers n, P1, P2, P3, T1, T2 (1 ≤ n ≤ 100, 0 ≤ P1, P2, P3 ≤ 100, 1 ≤ T1, T2 ≤ 60). The following n lines contain description of Tom's work. Each i-th of these lines contains two space-separated integers li and ri (0 ≤ li < ri ≤ 1440, ri < li + 1 for i < n), which stand for the start and the end of the i-th period of work.

Output the answer to the problem.
Tags: implementation,*900
'''

def calculate_total_power(n, P1, P2, P3, T1, T2, usage_periods):
    total_power = 0
    last_interaction_time = 0
    
    # Process each work period
    for i in range(n):
        li, ri = usage_periods[i]
        
        # Compute the idle time before the current period starts
        idle_time = li - last_interaction_time
        
        # Calculate power consumption during the idle period
        if idle_time > 0:
            # If idle time is less than T1, only normal mode consumed
            if idle_time <= T1:
                total_power += idle_time * P1
            else:
                # If idle time is greater than T1, it crosses to screensaver mode
                total_power += T1 * P1
                remaining_time = idle_time - T1
                
                # If remaining idle time is less than T2, all time in screen saver mode
                if remaining_time <= T2:
                    total_power += remaining_time * P2
                else:
                    # If remaining time is greater than T2, some time is in sleep mode
                    total_power += T2 * P2
                    sleep_time = remaining_time - T2
                    total_power += sleep_time * P3
        
        # Add power for active usage period (normal mode)
        active_time = ri - li
        total_power += active_time * P1
        
        # Update the last interaction time to the end of this period
        last_interaction_time = ri
    
    return total_power

# Test the solution function with a sample test case
# Example test case:
# n, P1, P2, P3, T1, T2 = 1, 10, 5, 2, 5, 5
# Usage periods: [[0, 10]]
# Expected output = 10 * 10 = 100 watts as there's no idle time
expected_output = 100
actual_output = calculate_total_power(1, 10, 5, 2, 5, 5, [[0, 10]])

# Check the output
if actual_output == expected_output:
    print('verified')
else:
    print(f'Incorrect: Got {actual_output}, Expected {expected_output}')