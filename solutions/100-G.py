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

def find_album_name(n, used_names, m, suitable_names):
    # Dictionary to store the used album names and their year
    used_name_dict = {}
    for name, year in used_names:
        used_name_dict[name] = year
    
    # Initialize variables for finding the optimal name
    oldest_year = 2012  # Set to a number greater than any in range
    chosen_name = None
    
    for name in suitable_names:
        if name not in used_name_dict:
            # Name has not been used, we can use it
            return name
        else:
            # Name has been used, check the year
            year = used_name_dict[name]
            if year < oldest_year:
                oldest_year = year
                chosen_name = name
            elif year == oldest_year:
                # Choose the alphabetically latest name
                if chosen_name is None or name > chosen_name:
                    chosen_name = name
    
    return chosen_name

# Test function

def test_find_album_name():
    # Test case 1: No used names, one suitable name
    n = 0
    used_names = []
    m = 1
    suitable_names = ["newalbum"]
    result = find_album_name(n, used_names, m, suitable_names)
    expected = "newalbum"
    if result == expected:
        print("Test case 1: verified")
    else:
        print(f"Test case 1: Error - actual: {result}, expected: {expected}")
    
    # Test case 2: Used names but suitable name not used
    n = 2
    used_names = [("oldalbum", 2005), ("ancient", 1900)]
    m = 2
    suitable_names = ["newalbum", "ancient"]
    result = find_album_name(n, used_names, m, suitable_names)
    expected = "newalbum"
    if result == expected:
        print("Test case 2: verified")
    else:
        print(f"Test case 2: Error - actual: {result}, expected: {expected}")

    # Test case 3: Suitable names all used
    n = 3
    used_names = [("album1", 2000), ("album2", 1990), ("album3", 1985)]
    m = 3
    suitable_names = ["album3", "album1", "album2"]
    result = find_album_name(n, used_names, m, suitable_names)
    expected = "album3"
    if result == expected:
        print("Test case 3: verified")
    else:
        print(f"Test case 3: Error - actual: {result}, expected: {expected}")

    # Test case 4: Same year, choose alphabetically
    n = 3
    used_names = [("aaa", 2000), ("bbb", 2000), ("ccc", 2000)]
    m = 3
    suitable_names = ["aaa", "bbb", "ccc"]
    result = find_album_name(n, used_names, m, suitable_names)
    expected = "ccc"
    if result == expected:
        print("Test case 4: verified")
    else:
        print(f"Test case 4: Error - actual: {result}, expected: {expected}")
    
    print("All test cases reviewed!")

# Run test
test_find_album_name()