'''
Problem id: 1000-F
Statement: You are given an array $$$a$$$ consisting of $$$n$$$ integers, and $$$q$$$ queries to it. $$$i$$$-th query is denoted by two integers $$$l_i$$$ and $$$r_i$$$. For each query, you have to find any integer that occurs exactly once in the subarray of $$$a$$$ from index $$$l_i$$$ to index $$$r_i$$$ (a subarray is a contiguous subsegment of an array). For example, if $$$a = [1, 1, 2, 3, 2, 4]$$$, then for query $$$(l_i = 2, r_i = 6)$$$ the subarray we are interested in is $$$[1, 2, 3, 2, 4]$$$, and possible answers are $$$1$$$, $$$3$$$ and $$$4$$$; for query $$$(l_i = 1, r_i = 2)$$$ the subarray we are interested in is $$$[1, 1]$$$, and there is no such element that occurs exactly once.

Can you answer all of the queries?

The first line contains one integer $$$n$$$ ($$$1 \le n \le 5 \cdot 10^5$$$).

The second line contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 5 \cdot 10^5$$$).

The third line contains one integer $$$q$$$ ($$$1 \le q \le 5 \cdot 10^5$$$).

Then $$$q$$$ lines follow, $$$i$$$-th line containing two integers $$$l_i$$$ and $$$r_i$$$ representing $$$i$$$-th query ($$$1 \le l_i \le r_i \le n$$$).

Answer the queries as follows:

If there is no integer such that it occurs in the subarray from index $$$l_i$$$ to index $$$r_i$$$ exactly once, print $$$0$$$. Otherwise print any such integer.
Tags: datastructures,divideandconquer,*2400
'''

def mo_algorithm_solution(n, array, queries):
    import math

    # Calculate block size
    block_size = int(math.sqrt(n))

    # Sort queries based on Mo's order
    def mo_order(x):
        block = x[0] // block_size
        return (block, x[1] if block % 2 == 0 else -x[1])

    queries = [(l-1, r-1, i) for i, (l, r) in enumerate(queries)]  # Convert to 0-based index
    queries.sort(key=mo_order)
    
    # Result list
    result = [0] * len(queries)
    
    # Frequency dictionary
    freq = {}
    unique_elements = set()

    # Current range
    curr_l, curr_r = 0, 0

    def add(x):
        if x in freq:
            if freq[x] == 1:
                unique_elements.discard(x)
            freq[x] += 1
        else:
            freq[x] = 1
            unique_elements.add(x)

    def remove(x):
        if x in freq:
            if freq[x] == 1:
                unique_elements.discard(x)
                del freq[x]
            else:
                freq[x] -= 1
                if freq[x] == 1:
                    unique_elements.add(x)

    # Initialize
    # Initial range [curr_l, curr_r] should be empty
    for l, r, qi in queries:
        while curr_r <= r:
            add(array[curr_r])
            curr_r += 1
        while curr_r > r + 1:
            remove(array[curr_r - 1])
            curr_r -= 1
        while curr_l < l:
            remove(array[curr_l])
            curr_l += 1
        while curr_l > l:
            curr_l -= 1
            add(array[curr_l])

        # Answer the query
        if unique_elements:
            result[qi] = next(iter(unique_elements))
        else:
            result[qi] = 0

    return result

# Test verification
def verify_solution():
    array = [1, 1, 2, 3, 2, 4]
    queries = [(2, 6), (1, 2)]  # 1-based index queries
    expected = [1, 0]  # Possible output for queries
    result = mo_algorithm_solution(len(array), array, queries)
    if result == expected:
        print('verified')
    else:
        print(f'incorrect result, got {result}, expected {expected}')

verify_solution()