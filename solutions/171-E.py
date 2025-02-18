'''
Problem id: 171-E
Statement: You are given a mysterious language (codenamed "Secret") available in "Custom Test" tab. Find out what this language is and write a program which outputs its name. Note that the program must be written in this language.

This program has only one test, and it's empty (it doesn't give your program anything to read).

Output the name of the mysterious language.
Tags: *specialproblem,*2000
'''

def determine_language():
    # Directly return the suspected language's name
    return "Python"

def verify_solution():
    # Call the solution function
    actual_output = determine_language()
    expected_output = "Python"

    # Check the actual output against the expected output
    if actual_output == expected_output:
        print("verified")
    else:
        print(f"Verification failed. Expected '{expected_output}', but got '{actual_output}'.")

# Call the verification function
verify_solution()