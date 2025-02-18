'''
Problem id: 1-B
Statement: In the popular spreadsheets systems (for example, in Excel) the following numeration of columns is used. The first column has number A, the second — number B, etc. till column 26 that is marked by Z. Then there are two-letter numbers: column 27 has number AA, 28 — AB, column 52 is marked by AZ. After ZZ there follow three-letter numbers, etc.

The rows are marked by integer numbers starting with 1. The cell name is the concatenation of the column and the row numbers. For example, BC23 is the name for the cell that is in column 55, row 23. 

Sometimes another numeration system is used: RXCY, where X and Y are integer numbers, showing the column and the row numbers respectfully. For instance, R23C55 is the cell from the previous example.

Your task is to write a program that reads the given sequence of cell coordinates and produce each item written according to the rules of another numeration system.

The first line of the input contains integer number n (1 ≤ n ≤ 105), the number of coordinates in the test. Then there follow n lines, each of them contains coordinates. All the coordinates are correct, there are no cells with the column and/or the row numbers larger than 106 .

Write n lines, each line should contain a cell coordinates in the other numeration system.
Tags: implementation,math,*1600
'''

def solution(n, coordinates):
    def to_rx_cy(coord):
        # "Letter-Number" to "RxCy": e.g., BC23 to R23C55
        i = 0
        while not coord[i].isdigit():
            i += 1
        column_letters = coord[:i]
        row_number = coord[i:]
        # Convert column letters to number
        column_number = 0
        for letter in column_letters:
            column_number = column_number * 26 + (ord(letter) - ord('A') + 1)
        return f"R{row_number}C{column_number}"

    def to_letter_number(coord):
        # "RxCy" to "Letter-Number": e.g., R23C55 to BC23
        rc_split = coord.split('C')
        row_number = rc_split[0][1:]  # Remove the 'R'
        column_number = int(rc_split[1])
        # Convert column number to letters
        column_letters = ''
        while column_number > 0:
            column_number -= 1
            letter = chr(column_number % 26 + ord('A'))
            column_letters = letter + column_letters
            column_number //= 26
        return f"{column_letters}{row_number}"

    results = []
    for coord in coordinates:
        if coord[0] == 'R' and 'C' in coord:
            results.append(to_letter_number(coord))
        else:
            results.append(to_rx_cy(coord))
    return results

# Verification test case
input_n = 2
input_coordinates = ['BC23', 'R23C55']  # BC23 should convert to R23C55 and vice versa
expected_output = ['R23C55', 'BC23']

# Call the solution function
actual_output = solution(input_n, input_coordinates)

# Verification step
output_verified = actual_output == expected_output

# Print the result of verification
if output_verified:
    print("verified")
else:
    print(f"Failed: expected {expected_output}, but got {actual_output}")