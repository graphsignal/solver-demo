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

def tanya_stairways(n, a):
    steps_per_stairway = []
    step_count = 0
    
    for i in range(n):
        if a[i] == 1:
            if step_count != 0:  # if step_count is not zero, means a stairway ended
                steps_per_stairway.append(step_count)
            step_count = 1
        else:
            step_count += 1
    
    # Add the last stairway count
    steps_per_stairway.append(step_count)
    
    return len(steps_per_stairway), steps_per_stairway

# Test case
def test_solution():
    # Given inputs
    n = 7
    a = [1, 2, 3, 1, 2, 3, 4]
    # Expected output
    expected_t = 2
    expected_stairways = [3, 4]
    
    # Get results
    result_t, result_stairways = tanya_stairways(n, a)
    
    # Verify results
    if result_t == expected_t and result_stairways == expected_stairways:
        print('verified')
    else:
        print(f'Incorrect result: Got ({result_t}, {result_stairways}), but expected ({expected_t}, {expected_stairways})')

# Run test
test_solution()