'''
Problem id: 1013-D
Statement: Innopolis University scientists continue to investigate the periodic table. There are n·m known elements and they form a periodic table: a rectangle with n rows and m columns. Each element can be described by its coordinates (r, c) (1 ≤ r ≤ n, 1 ≤ c ≤ m) in the table.

Recently scientists discovered that for every four different elements in this table that form a rectangle with sides parallel to the sides of the table, if they have samples of three of the four elements, they can produce a sample of the fourth element using nuclear fusion. So if we have elements in positions (r1, c1), (r1, c2), (r2, c1), where r1 ≠ r2 and c1 ≠ c2, then we can produce element (r2, c2).

Samples used in fusion are not wasted and can be used again in future fusions. Newly crafted elements also can be used in future fusions.

Innopolis University scientists already have samples of q elements. They want to obtain samples of all n·m elements. To achieve that, they will purchase some samples from other laboratories and then produce all remaining elements using an arbitrary number of nuclear fusions in some order. Help them to find the minimal number of elements they need to purchase.

The first line contains three integers n, m, q (1 ≤ n, m ≤ 200 000; 0 ≤ q ≤ min(n·m, 200 000)), the chemical table dimensions and the number of elements scientists already have.

The following q lines contain two integers ri, ci (1 ≤ ri ≤ n, 1 ≤ ci ≤ m), each describes an element that scientists already have. All elements in the input are different.

Print the minimal number of elements to be purchased.

For each example you have a picture which illustrates it.

The first picture for each example describes the initial set of element samples available. Black crosses represent elements available in the lab initially.

The second picture describes how remaining samples can be obtained. Red dashed circles denote elements that should be purchased from other labs (the optimal solution should minimize the number of red circles). Blue dashed circles are elements that can be produced with nuclear fusion. They are numbered in order in which they can be produced.

Test 1

We can use nuclear fusion and get the element from three other samples, so we don't need to purchase anything.

Test 2

We cannot use any nuclear fusion at all as there is only one row, so we have to purchase all missing elements.

Test 3

There are several possible solutions. One of them is illustrated below.

Note that after purchasing one element marked as red it's still not possible to immidiately produce the middle element in the bottom row (marked as 4). So we produce the element in the left-top corner first (marked as 1), and then use it in future fusions.
Tags: dfsandsimilar,graphs,matrices,*1900
'''

def minimum_samples_to_purchase(n, m, q, known_samples):
    # Track rows and columns that have at least one sample
    rows_with_samples = set()
    columns_with_samples = set()
    
    for r, c in known_samples:
        rows_with_samples.add(r)
        columns_with_samples.add(c)
    
    # Calculate missing coverage
    missing_rows = n - len(rows_with_samples)
    missing_columns = m - len(columns_with_samples)
    
    # The minimum additional samples needed
    return max(missing_rows, missing_columns)

# Verification
# Test Case 1
n1, m1, q1 = 2, 2, 3 # 2x2 matrix with 3 known samples
known_samples1 = [(1, 1), (1, 2), (2, 1)]
expected1 = 0 # We can produce element (2, 2) using nuclear fusion

# Test Case 2
n2, m2, q2 = 1, 4, 1 # 1x4 matrix with only 1 known sample
known_samples2 = [(1, 1)]
expected2 = 3 # We need to purchase 3 more samples to cover all columns

# Test Case 3
n3, m3, q3 = 3, 3, 2 # 3x3 matrix with 2 known samples
known_samples3 = [(1, 1), (2, 2)]
expected3 = 1 # We purchase one more sample to cover all rows and columns

actual1 = minimum_samples_to_purchase(n1, m1, q1, known_samples1)
actual2 = minimum_samples_to_purchase(n2, m2, q2, known_samples2)
actual3 = minimum_samples_to_purchase(n3, m3, q3, known_samples3)

print("Checking Test Case 1:")
if actual1 == expected1:
    print("verified")
else:
    print(f"incorrect, actual: {actual1}, expected: {expected1}")

print("Checking Test Case 2:")
if actual2 == expected2:
    print("verified")
else:
    print(f"incorrect, actual: {actual2}, expected: {expected2}")

print("Checking Test Case 3:")
if actual3 == expected3:
    print("verified")
else:
    print(f"incorrect, actual: {actual3}, expected: {expected3}")