'''
Problem id: 100-G
Statement: The famous singer, Aryo, is going to publish a new album of his great work!

Unfortunately these days, there are many albums, Aryo wants to choose a new name for his album, a name that has not been used or at least has not been used recently.

He has a list of all used album names together with the year the albums were published. He also has a list of suitable names for his album.

If he finds a suitable name which has not been used before, he'll use it. Otherwise he will use the name which was used as long ago as possible. If two such names are found (that haven't been used or were used at the same year), he uses the name that is alphabetically latest.

Help him name his album.

The first line contains a single integer n (0 ≤ n ≤ 105), the number of used names. 

The following n lines each contain a string (the album name) and an integer (the year album was published). Album names are made of lowercase Latin letters and contain at most 14 letters. The year is in range [1900, 2011].

The following line contains a single integer m (1 ≤ m ≤ 104), the number of suitable album names.

The following m lines each contain a string — a suitable name. It contains at most 14 lowercase Latin letters.

All album names and suitable names are non-empty.

Write a single string. The name of the new album.
Tags: *specialproblem,datastructures,implementation,*1800
'''

def find_album_name(used_names_info, suitable_names):
    # Transform the list of used names and years into a dictionary
    used_names = {}
    for name, year in used_names_info:
        if name not in used_names or used_names[name] > year:
            used_names[name] = year

    best_name = None
    best_year = 2012  # Start with year beyond possible range

    for name in suitable_names:
        if name not in used_names:
            # Name has not been used
            return name
        else:
            # Name has been used, check the year
            year = used_names[name]
            if year < best_year:
                best_year = year
                best_name = name
            elif year == best_year:
                # Select the alphabetically later one
                if best_name is None or name > best_name:
                    best_name = name

    return best_name

# Example verification call
used_names_info = [
    ('classical', 1990),
    ('rock', 1985),
    ('pop', 2000),
    ('jazz', 1995),
    ('blues', 1950)
]
suitable_names = ['rock', 'jazz', 'electronic', 'pop', 'opera']

# Expected result: 'electronic' because it hasn't been used.
expected_result = 'electronic'

# Get the result from the function
actual_result = find_album_name(used_names_info, suitable_names)

# Verify the result
if actual_result == expected_result:
    print('verified')
else:
    print(f'Failed verification. Expected: {expected_result}, but got: {actual_result}')