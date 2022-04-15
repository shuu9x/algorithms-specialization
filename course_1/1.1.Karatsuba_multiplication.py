"""
    Suppose 2 numbers is x and y, n is the highgest number of digits.
    let x = (10^(n/2)) * a + b
        y = (10^(n/2)) * c + d
    then x * y = [(10^(n/2)) * a + b] * [(10^(n/2)) * c + d]
               = (10^n)*(a*c) + (10^(n/2))*(a*d + b*c) + b*d
"""
def karatsuba_multiplication(factor_1, factor_2):
    """multiplication 2 numbers using karatsuba algorithm.

    Args:
        factor_1 (int): factor 1
        factor_2 (int): factor 2

    Returns:
        int: product of factor 1 and factor 2
    """
    if (factor_1 < 10) or (factor_2 < 10):
        return factor_1 * factor_2

    n = max(len(str(factor_1)), len(str(factor_2)))
    half_of_n = int(n / 2)

    a = factor_1 // (10**half_of_n)
    b = factor_1 % (10**half_of_n)
    c = factor_2 // (10**half_of_n)
    d = factor_2 % (10**half_of_n)

    ac = karatsuba_multiplication(a, c)
    bd = karatsuba_multiplication(b, d)
    ad_plus_bc = karatsuba_multiplication(a+b, c+d) - ac - bd

    return (10**half_of_n)**2 * ac + (10**half_of_n) * ad_plus_bc + bd

print(karatsuba_multiplication(12345, 100))