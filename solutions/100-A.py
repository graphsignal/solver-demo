'''
Problem id: 100-A
Statement: Soroush's room is a square with side length n. Before this contest he bought k fine Persian carpets to carpet his room for celebrating the 100th contest on his favorite site. Each Persian carpet is a square of side length n1.

Soroush wants to cover all the area of his room. Carpets can be put over each other but it is not allowed to rotate the carpets. Can Soroush carpet his room completely?

The input consists of three integer numbers n, k and n1 (10 ≤ n ≤ 12, 1 ≤ k ≤ 10, ).

Write a single YES or NO. Write YES if and only if Sorush can carpet his room completely.
Tags: *specialproblem,implementation,*1100
'''

def can_carpet_room(n, k, n1):
    # Calculate areas
    area_room = n * n
    area_carpet = n1 * n1
    area_covered_by_carpets = k * area_carpet
    
    # Check conditions
    if area_covered_by_carpets >= area_room and n % n1 == 0:
        return "YES"
    else:
        return "NO"

# Define the verification function
def verify():
    # Test case
    n = 10
    k = 9
    n1 = 3
    expected = "NO"
    result = can_carpet_room(n, k, n1)
    
    # Verify the result
    if result == expected:
        print("verified")
    else:
        print(f"Test failed: expected {expected}, got {result}")

verify()