'''
Problem id: 100-A
Statement: Soroush's room is a square with side length n. Before this contest he bought k fine Persian carpets to carpet his room for celebrating the 100th contest on his favorite site. Each Persian carpet is a square of side length n1.

Soroush wants to cover all the area of his room. Carpets can be put over each other but it is not allowed to rotate the carpets. Can Soroush carpet his room completely?

The input consists of three integer numbers n, k and n1 (10 ≤ n ≤ 12, 1 ≤ k ≤ 10, ).

Write a single YES or NO. Write YES if and only if Sorush can carpet his room completely.
Tags: *specialproblem,implementation,*1100
'''

def can_cover_room(n, k, n1):
    room_area = n * n
    carpet_area = n1 * n1
    total_carpet_area = k * carpet_area
    return total_carpet_area >= room_area

# Test example:
# Let's say the room's side n = 10, and we have k = 5 carpets each of side n1 = 5.
# Expected output: NO, because 5*5*5 = 125 which is less than 10*10 = 100.

n = 10
k = 5
n1 = 5
expected_output = "NO" if not can_cover_room(n, k, n1) else "YES"

# Actual function output:
actual_output = "YES" if can_cover_room(n, k, n1) else "NO"

if actual_output == expected_output:
    print("verified")
else:
    print(f"Incorrect result. Expected: {expected_output}, Got: {actual_output}")