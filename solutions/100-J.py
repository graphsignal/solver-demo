'''
Problem id: 100-J
Statement: Aryo has got a lot of intervals for his 2418th birthday. He is really excited and decided to color all these intervals with some colors. He has a simple rule for himself. He calls a coloring nice if there exists no three intervals a, b and c such that the following conditions are satisfied simultaneously: 

Moreover he found out that for every intervals i and j, there is at least one point in i which isn't in j.

Given some set of intervals. You have to find the minimum number k, such that Aryo can find a nice coloring with k colors.

The first line contains a single integer n (1 ≤ n ≤ 103), number of intervals.

The following n lines contain a interval description each. Each interval is described by two numbers si, ei which are the start and end points of it ( - 105 < si, ei < 105, si ≤ ei). See samples for clarity. A square bracket stands for including of the corresponding endpoint, while a round bracket stands for excluding.

Write a single integer k — the minimum number of colors needed for a nice coloring.
Tags: *specialproblem,greedy,math,*2400
'''

def min_colors_for_intervals(intervals):
    # Step 1: Transform each interval into (start_time, end_time, type) events.
    events = []
    for start, end in intervals:
        events.append((start, 1))  # +1 when an interval starts
        events.append((end, -1))   # -1 when an interval ends

    # Step 2: Sort events by time; if times tie, sort by type (-1 should come before +1)
    events.sort(key=lambda x: (x[0], x[1]))

    # Step 3: Sweep through events to find maximum overlaps
    current_overlap = 0
    max_overlap = 0

    for event in events:
        current_overlap += event[1]  # Add 1 if start, subtract 1 if end
        max_overlap = max(max_overlap, current_overlap)

    return max_overlap

# Verification function

def verify():
    # Test case: Expect max overlap/clique is 3 for below intervals.
    intervals = [(1, 4), (2, 5), (3, 6), (7, 8)]  # At time 3, three intervals overlap.
    expected_result = 3 
    result = min_colors_for_intervals(intervals)
    if result == expected_result:
        print("verified")
    else:
        print(f"Failed: Expected {expected_result}, but got {result}")

verify()