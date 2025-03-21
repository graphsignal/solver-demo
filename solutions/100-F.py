'''
Problem id: 100-F
Statement: You are given a polynom in form p(x) = (x + a1)·(x + a2)·... (x + an). Write Pike program to print it in a standard form p(x) = xn + b1xn - 1 + ... + bn - 1x + bn. You should write each addend in form «C*X^K» (for example, 5*X^8).

Please, write the polynom in the shortest way, so you should skip unnecessary terms: some terms «C*X^K» should be reduced or even omitted. Look for the samples for clarification.

The first line of the input contains n (1 ≤ n ≤ 9). The following n lines contain integer ai ( - 10 ≤ ai ≤ 10).

Print the given polynom in a standard way. Note, that the answer in this problem response uniquely determined.
Tags: *specialproblem,implementation,*1800
'''

def expand_polynomial(n, a_list):
    # Start with a polynomial representing '1'
    coefficients = [1]

    # Multiply by each factor (x + ai)
    for a in a_list:
        # Multiply the current polynomial by (x + a)
        new_coeffs = [0] * (len(coefficients) + 1)
        for i in range(len(coefficients)):
            new_coeffs[i] += coefficients[i]  # 
            new_coeffs[i+1] += coefficients[i] * a
        coefficients = new_coeffs

    # Prepare the polynomial string
    terms = []
    degree = len(coefficients) - 1
    for i, coef in enumerate(coefficients):
        power = degree - i
        if coef == 0:
            continue
        if power == 0:
            terms.append(f'{coef}')
        elif power == 1:
            if coef == 1:
                terms.append('X')
            elif coef == -1:
                terms.append('-X')
            else:
                terms.append(f'{coef}*X')
        else:
            if coef == 1:
                terms.append(f'X^{power}')
            elif coef == -1:
                terms.append(f'-X^{power}')
            else:
                terms.append(f'{coef}*X^{power}')

    return '+'.join(terms).replace('+-', '-')

# Test the solution with a known case
test_case = (3, [-1, 0, 1])  # Corresponds to (x - 1)(x)(x + 1) => x^3 - x
expected_output = 'X^3-X'
result = expand_polynomial(*test_case)

# Verification
def verify_result(result, expected):
    if result == expected:
        print('verified')
    else:
        print(f'Incorrect. Expected {expected}, but got {result}.')

verify_result(result, expected_output)