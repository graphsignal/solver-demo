'''
Problem id: 172-C
Statement: There is a bus stop near the university. The lessons are over, and n students come to the stop. The i-th student will appear at the bus stop at time ti (all ti's are distinct).

We shall assume that the stop is located on the coordinate axis Ox, at point x = 0, and the bus goes along the ray Ox, that is, towards the positive direction of the coordinate axis, and back. The i-th student needs to get to the point with coordinate xi (xi > 0).

The bus moves by the following algorithm. Initially it is at point 0. The students consistently come to the stop and get on it. The bus has a seating capacity which is equal to m passengers. At the moment when m students get on the bus, it starts moving in the positive direction of the coordinate axis. Also it starts moving when the last (n-th) student gets on the bus. The bus is moving at a speed of 1 unit of distance per 1 unit of time, i.e. it covers distance y in time y.

Every time the bus passes the point at which at least one student needs to get off, it stops and these students get off the bus. The students need 1 + [k / 2] units of time to get off the bus, where k is the number of students who leave at this point. Expression [k / 2] denotes rounded down k / 2. As soon as the last student leaves the bus, the bus turns around and goes back to the point x = 0. It doesn't make any stops until it reaches the point. At the given point the bus fills with students once more, and everything is repeated.

If students come to the stop when there's no bus, they form a line (queue) and get on the bus in the order in which they came. Any number of students get on the bus in negligible time, you should assume that it doesn't take any time. Any other actions also take no time. The bus has no other passengers apart from the students.

Write a program that will determine for each student the time when he got off the bus. The moment a student got off the bus is the moment the bus stopped at the student's destination stop (despite the fact that the group of students need some time to get off).

The first line contains two space-separated integers n, m (1 ≤ n, m ≤ 105) — the number of students and the number of passengers the bus can transport, correspondingly. Next n lines contain descriptions of the students, one per line. Each line contains a pair of integers ti, xi (1 ≤ ti ≤ 105, 1 ≤ xi ≤ 104). The lines are given in the order of strict increasing of ti. Values of xi can coincide.

Print n numbers w1, w2, ..., wn, wi — the moment of time when the i-th student got off the bus. Print the numbers on one line and separate them with single spaces.

In the first sample the bus waits for the first student for 3 units of time and drives him to his destination in additional 5 units of time. So the student leaves the bus at the moment of time 3 + 5 = 8.

In the second sample the capacity of the bus equals 1, that's why it will drive the first student alone. This student is the same as the student from the first sample. So the bus arrives to his destination at the moment of time 8, spends 1 + [1 / 2] = 1 units of time on getting him off, and returns back to 0 in additional 5 units of time. That is, the bus returns to the bus stop at the moment of time 14. By this moment the second student has already came to the bus stop. So he immediately gets in the bus, and is driven to his destination in additional 5 units of time. He gets there at the moment 14 + 5 = 19. 

In the third sample the bus waits for the fourth student for 6 units of time, then drives for 5 units of time, then gets the passengers off for 1 + [4 / 2] = 3 units of time, then returns for 5 units of time, and then drives the fifth student for 1 unit of time.
Tags: *specialproblem,implementation,sortings,*1500
'''

def bus_stop_simulation(n, m, students):
    # Sort students by their destination because bus serves students in order of xi during the trip
    students.sort(key=lambda s: s[1])

    current_time = 0
    drop_off_times = [0] * n
    i = 0

    while i < n:
        # Determine the batch of students to take on the bus
        bus_capacity = min(m, n - i)  # Actual current bus load
        furthest_x = max(students[j][1] for j in range(i, i + bus_capacity))

        # Determine the time bus leaves, which is the max of current time and t_i of last student in bus
        bus_depart_time = max(current_time, students[i + bus_capacity - 1][0])

        # Calculate time to reach furthest student
        current_time = bus_depart_time + furthest_x

        # Drop off each student and calculate their individual drop-off time based on arrival time
        j = i
        while j < i + bus_capacity:
            drop_off_pos = students[j][1]
            drop_off_times[j] = current_time  # Time bus reaches x_j
            j += 1

        # Calculate time for dropping off all students in this trip
        drop_off_group_size = j - i
        current_time += 1 + (drop_off_group_size // 2)  # Time taken for students to get off
        
        # Return trip to x = 0
        current_time += furthest_x

        # Update student index for the next bus trip
        i += bus_capacity

    return drop_off_times

# Test the function with a verification call

def verify_simulation():
    # Test Case: Provided example 1
    n, m = 1, 2
    students = [(3, 5)]
    expected = [8]
    result = bus_stop_simulation(n, m, students)
    if result == expected:
        print('verified')
    else:
        print(f'incorrect result for test case 1: {result}, expected: {expected}')

    # Test Case: Provided example 2
    n, m = 1, 1
    students = [(3, 5), (13, 5)]
    expected = [8, 19]
    result = bus_stop_simulation(n, m, students)
    if result == expected:
        print('verified')
    else:
        print(f'incorrect result for test case 2: {result}, expected: {expected}')

    # Test Case: Provided example 3 (has additional student)
    n, m = 4, 100
    students = [(0, 1), (1, 2), (2, 3), (3, 5), (6, 1)]
    expected = [9, 10, 11, 8, 15]
    result = bus_stop_simulation(n, m, students)
    if result == expected:
        print('verified')
    else:
        print(f'incorrect result for test case 3: {result}, expected: {expected}')

verify_simulation()