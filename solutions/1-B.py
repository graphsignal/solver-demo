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

import re

def excel_to_rxcy(column_alpha):
    col_number = 0
    for char in column_alpha:
        col_number = col_number * 26 + (ord(char) - ord('A') + 1)
    return col_number


def rxcy_to_excel(col_number):
    column_alpha = []
    while col_number > 0:
        col_number -= 1
        column_alpha.append(chr(col_number % 26 + ord('A')))
        col_number //= 26
    return ''.join(reversed(column_alpha))


def convert_coordinates(n, coordinates):
    converted = []
    for coord in coordinates:
        if re.match(r'^[A-Z]+[0-9]+$', coord):
            # Excel-style to RXCY-style
            match = re.match(r'^([A-Z]+)([0-9]+)$', coord)
            column_alpha, row = match.groups()
            col_number = excel_to_rxcy(column_alpha)
            converted.append(f'R{row}C{col_number}')
        elif re.match(r'^R[0-9]+C[0-9]+$', coord):
            # RXCY-style to Excel-style
            match = re.match(r'^R([0-9]+)C([0-9]+)$', coord)
            row, col_number = match.groups()
            col_number = int(col_number)
            column_alpha = rxcy_to_excel(col_number)
            converted.append(f'{column_alpha}{row}')
    return converted

# Verification
n = 3
coordinates = ['BC23', 'R23C55', 'A1']
expected_output = ['R23C55', 'BC23', 'R1C1']
output = convert_coordinates(n, coordinates)

if output == expected_output:
    print('verified')
else:
    print(f'incorrect, got {output}, expected {expected_output}')