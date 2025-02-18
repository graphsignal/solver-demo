'''
Problem id: 1004-D
Statement: Since Sonya has just learned the basics of matrices, she decided to play with them a little bit.

Sonya imagined a new type of matrices that she called rhombic matrices. These matrices have exactly one zero, while all other cells have the Manhattan distance to the cell containing the zero. The cells with equal numbers have the form of a rhombus, that is why Sonya called this type so.

The Manhattan distance between two cells ($$$x_1$$$, $$$y_1$$$) and ($$$x_2$$$, $$$y_2$$$) is defined as $$$|x_1 - x_2| + |y_1 - y_2|$$$. For example, the Manhattan distance between the cells $$$(5, 2)$$$ and $$$(7, 1)$$$ equals to $$$|5-7|+|2-1|=3$$$.

Note that rhombic matrices are uniquely defined by $$$n$$$, $$$m$$$, and the coordinates of the cell containing the zero.

She drew a $$$n\times m$$$ rhombic matrix. She believes that you can not recreate the matrix if she gives you only the elements of this matrix in some arbitrary order (i.e., the sequence of $$$n\cdot m$$$ numbers). Note that Sonya will not give you $$$n$$$ and $$$m$$$, so only the sequence of numbers in this matrix will be at your disposal.

Write a program that finds such an $$$n\times m$$$ rhombic matrix whose elements are the same as the elements in the sequence in some order.

The first line contains a single integer $$$t$$$ ($$$1\leq t\leq 10^6$$$) — the number of cells in the matrix.

The second line contains $$$t$$$ integers $$$a_1, a_2, \ldots, a_t$$$ ($$$0\leq a_i< t$$$) — the values in the cells in arbitrary order.

In the first line, print two positive integers $$$n$$$ and $$$m$$$ ($$$n \times m = t$$$) — the size of the matrix.

In the second line, print two integers $$$x$$$ and $$$y$$$ ($$$1\leq x\leq n$$$, $$$1\leq y\leq m$$$) — the row number and the column number where the cell with $$$0$$$ is located.

If there are multiple possible answers, print any of them. If there is no solution, print the single integer $$$-1$$$.

You can see the solution to the first example in the legend. You also can choose the cell $$$(2, 2)$$$ for the cell where $$$0$$$ is located. You also can choose a $$$5\times 4$$$ matrix with zero at $$$(4, 2)$$$.

In the second example, there is a $$$3\times 6$$$ matrix, where the zero is located at $$$(2, 3)$$$ there.

In the third example, a solution does not exist.
Tags: bruteforce,constructivealgorithms,implementation,*2300
'''

def generate_rhombic_matrix_solution(t, elements):
    def valid_dimensions(t):
        dims = []
        for n in range(1, int(t**0.5) + 1):
            if t % n == 0:
                dims.append((n, t // n))
                if n != t // n:
                    dims.append((t // n, n))
        return dims

    elements_sorted = sorted(elements)

    for n, m in valid_dimensions(t):
        for x in range(1, n + 1):
            for y in range(1, m + 1):
                generated_distances = []
                for i in range(1, n + 1):
                    for j in range(1, m + 1):
                        dist = abs(i - x) + abs(j - y)
                        generated_distances.append(dist)
                if sorted(generated_distances) == elements_sorted:
                    return n, m, x, y

    return -1

def test_generate_rhombic_matrix_solution():
    # Test 1: A valid 3x4 matrix with zero at (2,2)
    t1 = 12
    elements1 = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3]
    result1 = generate_rhombic_matrix_solution(t1, elements1)
    expected1 = (3, 4, 2, 2)  # since the center zero can be at (2, 2)

    if result1 == expected1:
        print("Test 1 verified")
    else:
        print(f"Test 1 failed: expected {expected1}, but got {result1}")

    # Test 2: No valid matrix possible
    t2 = 5
    elements2 = [0, 1, 2, 3, 4]
    result2 = generate_rhombic_matrix_solution(t2, elements2)
    expected2 = -1

    if result2 == expected2:
        print("Test 2 verified")
    else:
        print(f"Test 2 failed: expected {expected2}, but got {result2}")

# Run tests
test_generate_rhombic_matrix_solution()