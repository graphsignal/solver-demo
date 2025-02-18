'''
Problem id: 172-A
Statement: Polycarpus has n friends in Tarasov city. Polycarpus knows phone numbers of all his friends: they are strings s1, s2, ..., sn. All these strings consist only of digits and have the same length. 

Once Polycarpus needed to figure out Tarasov city phone code. He assumed that the phone code of the city is the longest common prefix of all phone numbers of his friends. In other words, it is the longest string c which is a prefix (the beginning) of each si for all i (1 ≤ i ≤ n). Help Polycarpus determine the length of the city phone code. 

The first line of the input contains an integer n (2 ≤ n ≤ 3·104) — the number of Polycarpus's friends. The following n lines contain strings s1, s2, ..., sn — the phone numbers of Polycarpus's friends. It is guaranteed that all strings consist only of digits and have the same length from 1 to 20, inclusive. It is also guaranteed that all strings are different.

Print the number of digits in the city phone code.

A prefix of string t is a string that is obtained by deleting zero or more digits from the end of string t. For example, string "00209" has 6 prefixes: "" (an empty prefix), "0", "00", "002", "0020", "00209".

In the first sample the city phone code is string "00".

In the second sample the city phone code is an empty string.

In the third sample the city phone code is string "770123456789".
Tags: *specialproblem,bruteforce,implementation,*800
'''

def longest_common_prefix_length(n, phone_numbers):
    if n == 0:
        return 0
    # Take the first phone number as reference
    reference = phone_numbers[0]
    prefix_length = 0
    
    for i in range(len(reference)):
        current_digit = reference[i]
        # Check if this digit is present at the same position in all other numbers
        for number in phone_numbers[1:]:
            if number[i] != current_digit:
                return prefix_length
        # If digit matches for all numbers at this position, increase the prefix length
        prefix_length += 1
    return prefix_length

# Test the function with sample inputs

def test_longest_common_prefix_length():
    test_cases = [
        (3, ["002", "001", "000"], 2),     # Expected common prefix length is 2
        (2, ["123456", "234567"], 0),       # Expected common prefix length is 0
        (3, ["770123456789", "770123456700", "770123456788"], 9) # Expected common prefix length is 9
    ]
    
    for index, (n, phone_numbers, expected) in enumerate(test_cases, 1):
        result = longest_common_prefix_length(n, phone_numbers)
        if result == expected:
            print(f"Test case {index}: verified")
        else:
            print(f"Test case {index}: Failed. Expected {expected}, got {result}.")

# Run the test function
test_longest_common_prefix_length()