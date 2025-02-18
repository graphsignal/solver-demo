'''
Problem id: 100-F
Statement: You are given a polynom in form p(x) = (x + a1)·(x + a2)·... (x + an). Write Pike program to print it in a standard form p(x) = xn + b1xn - 1 + ... + bn - 1x + bn. You should write each addend in form «C*X^K» (for example, 5*X^8).

Please, write the polynom in the shortest way, so you should skip unnecessary terms: some terms «C*X^K» should be reduced or even omitted. Look for the samples for clarification.

The first line of the input contains n (1 ≤ n ≤ 9). The following n lines contain integer ai ( - 10 ≤ ai ≤ 10).

Print the given polynom in a standard way. Note, that the answer in this problem response uniquely determined.
Tags: *specialproblem,implementation,*1800
'''

def multiply_polynomials(p1, p2):
    """Multiplies two polynomials p1 and p2 given as lists of coefficients"""
    # Initialize the result list with zeros
    result = [0] * (len(p1) + len(p2) - 1)
    # Multiply each term of the first polynomial with each term of the second
    for i, coeff1 in enumerate(p1):
        for j, coeff2 in enumerate(p2):
            result[i + j] += coeff1 * coeff2
    return result


def expand_polynomial(n, coefficients):
    # Start with the polynomial (1) which is [1] => 1
    current_poly = [1]
    # Iterate over each ai and form (x + ai)
    for ai in coefficients:
        # Current factor (x + ai) is represented as [1, ai]
        factor = [1, ai]
        # Update the current polynomial by multiplying it with the newest factor
        current_poly = multiply_polynomials(current_poly, factor)
    return current_poly


def format_polynomial(coeffs):
    terms = []
    degree = len(coeffs) - 1
    for i, coeff in enumerate(coeffs):
        if coeff == 0:
            continue  # Skip zero coefficients
        power = degree - i
        if power == 0:
            # Constant term
            terms.append(f"{coeff}")
        elif power == 1:
            # Linear term
            if abs(coeff) == 1:
                sign = "-" if coeff < 0 else ""
                terms.append(f"{sign}X")
            else:
                terms.append(f"{coeff}*X")
        else:
            # Higher power terms
            if abs(coeff) == 1:
                sign = "-" if coeff < 0 else ""
                terms.append(f"{sign}X^{power}")
            else:
                terms.append(f"{coeff}*X^{power}")
    # Join terms with a plus sign and replace '+-' with '-'
    return '+'.join(terms).replace('+-', '-')


def solution():
    # Example test case with n = 2, a1 = -1, a2 = -1
    # This corresponds to the polynomial: (x - 1)(x - 1) = x^2 - 2x + 1
    n = 2
    coefficients = [-1, -1]
    expected = "X^2-2*X+1"
    # Expand the polynomial
    expanded_coeffs = expand_polynomial(n, coefficients)
    # Format the expanded polynomial
    result = format_polynomial(expanded_coeffs)
    # Verification
    if result == expected:
        print('verified')
    else:
        print(f'Incorrect result. Expected: {expected}, got: {result}')

solution()