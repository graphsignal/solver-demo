'''
Problem id: 1005-A
Statement: Little girl Tanya climbs the stairs inside a multi-storey building. Every time Tanya climbs a stairway, she starts counting steps from $$$1$$$ to the number of steps in this stairway. She speaks every number aloud. For example, if she climbs two stairways, the first of which contains $$$3$$$ steps, and the second contains $$$4$$$ steps, she will pronounce the numbers $$$1, 2, 3, 1, 2, 3, 4$$$.

You are given all the numbers pronounced by Tanya. How many stairways did she climb? Also, output the number of steps in each stairway.

The given sequence will be a valid sequence that Tanya could have pronounced when climbing one or more stairways.

The first line contains $$$n$$$ ($$$1 \le n \le 1000$$$) — the total number of numbers pronounced by Tanya.

The second line contains integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 1000$$$) — all the numbers Tanya pronounced while climbing the stairs, in order from the first to the last pronounced number. Passing a stairway with $$$x$$$ steps, she will pronounce the numbers $$$1, 2, \dots, x$$$ in that order.

The given sequence will be a valid sequence that Tanya could have pronounced when climbing one or more stairways.

In the first line, output $$$t$$$ — the number of stairways that Tanya climbed. In the second line, output $$$t$$$ numbers — the number of steps in each stairway she climbed. Write the numbers in the correct order of passage of the stairways.
Tags: implementation,*800
'''

def calculate_stairways_steps(n, sequence):
    steps_list = []
    current_steps = 0

    for i in range(n):
        current_steps += 1  # counting a step
        
        # Check if it's the end of a stairway
        if i == n - 1 or sequence[i + 1] == 1:
            steps_list.append(current_steps)
            current_steps = 0  # reset for next stairway

    return len(steps_list), steps_list

# Test case
n = 7
sequence = [1, 2, 3, 1, 2, 3, 4]
expected_stairways_count = 2
expected_steps_list = [3, 4]

# Call the solution function
stairways_count, steps_list = calculate_stairways_steps(n, sequence)

# Verification
if stairways_count == expected_stairways_count and steps_list == expected_steps_list:
    print('verified')
else:
    print(f'incorrect result: expected ({expected_stairways_count}, {expected_steps_list}), got ({stairways_count}, {steps_list})')