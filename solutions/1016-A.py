'''
Problem id: 1016-A
Statement: You received a notebook which is called Death Note. This notebook has infinite number of pages. A rule is written on the last page (huh) of this notebook. It says: "You have to write names in this notebook during $$$n$$$ consecutive days. During the $$$i$$$-th day you have to write exactly $$$a_i$$$ names.". You got scared (of course you got scared, who wouldn't get scared if he just receive a notebook which is named Death Note with a some strange rule written in it?).

Of course, you decided to follow this rule. When you calmed down, you came up with a strategy how you will write names in the notebook. You have calculated that each page of the notebook can contain exactly $$$m$$$ names. You will start writing names from the first page. You will write names on the current page as long as the limit on the number of names on this page is not exceeded. When the current page is over, you turn the page. Note that you always turn the page when it ends, it doesn't matter if it is the last day or not. If after some day the current page still can hold at least one name, during the next day you will continue writing the names from the current page.

Now you are interested in the following question: how many times will you turn the page during each day? You are interested in the number of pages you will turn each day from $$$1$$$ to $$$n$$$.

The first line of the input contains two integers $$$n$$$, $$$m$$$ ($$$1 \le n \le 2 \cdot 10^5$$$, $$$1 \le m \le 10^9$$$) — the number of days you will write names in the notebook and the number of names which can be written on each page of the notebook.

The second line contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 10^9$$$), where $$$a_i$$$ means the number of names you will write in the notebook during the $$$i$$$-th day.

Print exactly $$$n$$$ integers $$$t_1, t_2, \dots, t_n$$$, where $$$t_i$$$ is the number of times you will turn the page during the $$$i$$$-th day.

In the first example pages of the Death Note will look like this $$$[1, 1, 1, 2, 2], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [3, 3, 3, 3]$$$. Each number of the array describes during which day name on the corresponding position will be written. It is easy to see that you should turn the first and the second page during the second day and the third page during the third day.
Tags: greedy,implementation,math,*900
'''

def turn_pages(n, m, a):
    current_names_on_page = 0
    page_turns = []

    for i in range(n):
        # Add today's names to the current page
        current_names_on_page += a[i]        
        # Calculate how many full pages we will fill
        pages_filled = current_names_on_page // m
        page_turns.append(pages_filled)
        
        # Calculate remaining names on the current page
        current_names_on_page %= m  # Keep leftover names that don't form a full page

    return page_turns

def verify_solution():
    # Test case 1: Adjust expectation based on example in the problem
    n, m = 5, 3
    a = [1, 10, 3, 3, 3]
    # Based on the corrected understanding of the problem:
    expected_result = [0, 3, 1, 1, 1]
    actual_result = turn_pages(n, m, a)
    if actual_result == expected_result:
        print('Test case 1: verified')
    else:
        print(f'Test case 1 failed: Actual result {actual_result}, Expected result {expected_result}')

verify_solution()