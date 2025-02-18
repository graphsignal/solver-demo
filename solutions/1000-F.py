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

class MoAlgorithm:
    def __init__(self, array):
        self.array = array
        self.block_size = int(len(array) ** 0.5) + 1
        self.freq = {}
        self.current_ans = 0
        self.unique_items = set()
        self.result_cache = {}

    def add(self, index):
        val = self.array[index]
        
        if val in self.freq:
            if self.freq[val] == 1:
                self.unique_items.discard(val)
                self.current_ans -= 1
            self.freq[val] += 1
        else:
            self.freq[val] = 1
            self.unique_items.add(val)
            self.current_ans += 1
        
    def remove(self, index):
        val = self.array[index]
        
        if val in self.freq:
            if self.freq[val] == 1:
                self.unique_items.discard(val)
                self.current_ans -= 1
            self.freq[val] -= 1
            if self.freq[val] == 1:
                self.unique_items.add(val)
                self.current_ans += 1
            elif self.freq[val] == 0:
                del self.freq[val]

    def get_answer(self):
        # Return any item from the set or 0 if empty
        return next(iter(self.unique_items), 0)

    def process_query(self, queries):
        queries = sorted(queries, key=lambda q: (q[0] // self.block_size, q[1]))
        l, r, answers = 0, 0, [0] * len(queries)
        for idx, (ql, qr, qi) in enumerate(queries):
            while r <= qr:
                self.add(r)
                r += 1
            while l < ql:
                self.remove(l)
                l += 1
            while l > ql:
                l -= 1
                self.add(l)
            while r > qr + 1:
                r -= 1
                self.remove(r)
            # Store the result
            answers[qi] = self.get_answer()
        return answers

def solution(n, a, q, queries):
    mo_algo = MoAlgorithm(a)
    indexed_queries = [(l-1, r-1, i) for i, (l, r) in enumerate(queries)]
    return mo_algo.process_query(indexed_queries)

# Test Case
def verify_result():
    n = 6
    a = [1, 1, 2, 3, 2, 4]
    q = 2
    queries = [(2, 6), (1, 2)]
    expected = [3, 0]  # Possible output for first query is 1, 3, or 4
    result = solution(n, a, q, queries)
    # Verification
    if all(res in ([1, 3, 4] if exp == 3 else [0]) for res, exp in zip(result, expected)):
        print("verified")
    else:
        print(f"Incorrect: expected {expected}, but got {result}")

verify_result()