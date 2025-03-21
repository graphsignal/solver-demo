'''
Problem id: 1010-B
Statement: This is an interactive problem.

Natasha is going to fly to Mars. Finally, Natasha sat in the rocket. She flies, flies... but gets bored. She wishes to arrive to Mars already! So she decides to find something to occupy herself. She couldn't think of anything better to do than to calculate the distance to the red planet.

Let's define $$$x$$$ as the distance to Mars. Unfortunately, Natasha does not know $$$x$$$. But it is known that $$$1 \le x \le m$$$, where Natasha knows the number $$$m$$$. Besides, $$$x$$$ and $$$m$$$ are positive integers.

Natasha can ask the rocket questions. Every question is an integer $$$y$$$ ($$$1 \le y \le m$$$). The correct answer to the question is $$$-1$$$, if $$$x<y$$$, $$$0$$$, if $$$x=y$$$, and $$$1$$$, if $$$x>y$$$. But the rocket is broken — it does not always answer correctly. Precisely: let the correct answer to the current question be equal to $$$t$$$, then, if the rocket answers this question correctly, then it will answer $$$t$$$, otherwise it will answer $$$-t$$$.

In addition, the rocket has a sequence $$$p$$$ of length $$$n$$$. Each element of the sequence is either $$$0$$$ or $$$1$$$. The rocket processes this sequence in the cyclic order, that is $$$1$$$-st element, $$$2$$$-nd, $$$3$$$-rd, $$$\ldots$$$, $$$(n-1)$$$-th, $$$n$$$-th, $$$1$$$-st, $$$2$$$-nd, $$$3$$$-rd, $$$\ldots$$$, $$$(n-1)$$$-th, $$$n$$$-th, $$$\ldots$$$. If the current element is $$$1$$$, the rocket answers correctly, if $$$0$$$ — lies. Natasha doesn't know the sequence $$$p$$$, but she knows its length — $$$n$$$.

You can ask the rocket no more than $$$60$$$ questions.

Help Natasha find the distance to Mars. Assume, that the distance to Mars does not change while Natasha is asking questions.

Your solution will not be accepted, if it does not receive an answer $$$0$$$ from the rocket (even if the distance to Mars is uniquely determined by the already received rocket's answers).

The first line contains two integers $$$m$$$ and $$$n$$$ ($$$1 \le m \le 10^9$$$, $$$1 \le n \le 30$$$) — the maximum distance to Mars and the number of elements in the sequence $$$p$$$.

You can ask the rocket no more than $$$60$$$ questions.

To ask a question, print a number $$$y$$$ ($$$1\le y\le m$$$) and an end-of-line character, then do the operation flush and read the answer to the question.

If the program reads $$$0$$$, then the distance is correct and you must immediately terminate the program (for example, by calling exit(0)). If you ignore this, you can get any verdict, since your program will continue to read from the closed input stream.

If at some point your program reads $$$-2$$$ as an answer, it must immediately end (for example, by calling exit(0)). You will receive the "Wrong answer" verdict, and this will mean that the request is incorrect or the number of requests exceeds $$$60$$$. If you ignore this, you can get any verdict, since your program will continue to read from the closed input stream.

If your program's request is not a valid integer between $$$-2^{31}$$$ and $$$2^{31}-1$$$ (inclusive) without leading zeros, then you can get any verdict.

You can get "Idleness limit exceeded" if you don't print anything or if you forget to flush the output.

To flush the output buffer you can use (after printing a query and end-of-line):

Hacking

Use the following format for hacking:

In the first line, print $$$3$$$ integers $$$m,n,x$$$ ($$$1\le x\le m\le 10^9$$$, $$$1\le n\le 30$$$) — the maximum distance to Mars, the number of elements in the sequence $$$p$$$ and the current distance to Mars.

In the second line, enter $$$n$$$ numbers, each of which is equal to $$$0$$$ or $$$1$$$ — sequence $$$p$$$.

The hacked solution will not have access to the number $$$x$$$ and sequence $$$p$$$.

In the example, hacking would look like this:

5 2 3

1 0

This means that the current distance to Mars is equal to $$$3$$$, Natasha knows that it does not exceed $$$5$$$, and the rocket answers in order: correctly, incorrectly, correctly, incorrectly ...

Really:

on the first query ($$$1$$$) the correct answer is $$$1$$$, the rocket answered correctly: $$$1$$$;

on the second query ($$$2$$$) the correct answer is $$$1$$$, the rocket answered incorrectly: $$$-1$$$;

on the third query ($$$4$$$) the correct answer is $$$-1$$$, the rocket answered correctly: $$$-1$$$;

on the fourth query ($$$5$$$) the correct answer is $$$-1$$$, the rocket answered incorrectly: $$$1$$$;

on the fifth query ($$$3$$$) the correct and incorrect answer is $$$0$$$.
Tags: binarysearch,interactive,*1800
'''

def test_incorrect_behavior():
    # Define mocked behavioral conditions
    # m: max distance, n: length of p
    m, n, x = 5, 2, 3  # Given known values for testing
    p = [1, 0]  # Sequence pattern of truth-telling

    # Define the rocket response simulation
    def rocket_response(y, query_count):
        correct_answer = 0 if x == y else (-1 if x < y else 1)
        truth_teller = p[query_count % n]
        return correct_answer if truth_teller else -correct_answer

    # The solution we are testing
    def find_distance_to_mars(m, n):
        # Starting the binary search
        low, high = 1, m
        query_count = 0
        guessed_x = None

        while low <= high and query_count < 60:
            mid = (low + high) // 2
            response = rocket_response(mid, query_count)
            query_count += 1

            if response == 0:
                guessed_x = mid
                break
            elif response == 1:
                low = mid + 1
            else:
                high = mid - 1

        return guessed_x

    # Expected value and results
    expected = x
    result = find_distance_to_mars(m, n)

    if result == expected:
        print('verified')
    else:
        print(f'Incorrect behavior. Expected {expected}, but got {result}. Possible reason: Breaking rocket logic either in truth pattern handling or search space narrowing.')

# Run the verification test
test_incorrect_behavior()