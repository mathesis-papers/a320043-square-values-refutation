import json
from fractions import Fraction
from math import gcd, isqrt, prod


SOURCE_PREFIX = [
    1, 6, 13, 50, 37, 196, 189, 384, 351, 1210, 601, 2366, 1471,
    2156, 2941, 6936, 3277, 10830, 5563, 9022, 9681, 23276, 9897,
    26300, 19267, 30030, 23043, 58870, 21087, 76880, 46717, 59296,
    57801, 83546, 50281, 156066, 90973, 117968, 90539, 235340,
    86179, 284746,
]


def row(index):
    total = 0
    for column in range(1, index + 1):
        complement = index + 1 - column
        divisor = gcd(complement, column)
        quotient, remainder = divmod(complement ** 2 * column, divisor ** 3)
        assert remainder == 0
        assert quotient == (complement // divisor) ** 2 * (column // divisor)
        total += quotient
    return total


def rational_row(index):
    return sum(
        (Fraction((index + 1 - column) ** 2 * column,
                  gcd(index + 1 - column, column) ** 3)
         for column in range(1, index + 1)),
        Fraction(0),
    )


def trial_prime(number):
    return number >= 2 and all(
        number % divisor for divisor in range(2, isqrt(number) + 1)
    )


def divisors(number):
    smaller = []
    larger = []
    for divisor in range(1, isqrt(number) + 1):
        quotient, remainder = divmod(number, divisor)
        if remainder == 0:
            smaller.append(divisor)
            if quotient != divisor:
                larger.append(quotient)
    return smaller + larger[::-1]


def prime_factors(number):
    factors = []
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            while number % divisor == 0:
                number //= divisor
        divisor += 1
    if number > 1:
        factors.append(number)
    return factors


def divisor_row(successor):
    total = 0
    for divisor in divisors(successor):
        factors = prime_factors(divisor)
        totient = divisor
        for prime in factors:
            totient = totient // prime * (prime - 1)
        euler_product = prod(1 - prime for prime in factors)
        total += divisor ** 3 * totient - divisor ** 2 * euler_product
    quotient, remainder = divmod(total, 12)
    assert remainder == 0
    return quotient


def triangle_product(successor):
    product = 1
    for column in range(1, successor):
        divisor = gcd(successor, column)
        numerator = (successor - column) ** 2 * column
        quotient, remainder = divmod(numerator, divisor ** 3)
        assert remainder == 0
        product *= quotient
    target = prod(column // gcd(column, successor)
                  for column in range(1, successor + 1))
    assert product == target ** 3
    grouped = prod(prod(column for column in range(1, divisor + 1)
                        if gcd(column, divisor) == 1)
                   for divisor in divisors(successor))
    assert target == grouped


def polynomial_add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, 0) + coefficient
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient}


def polynomial_scale(polynomial, scalar):
    return {exponent: coefficient * scalar
            for exponent, coefficient in polynomial.items() if coefficient * scalar}


def polynomial_multiply(*polynomials):
    result = {(0, 0): 1}
    for polynomial in polynomials:
        product = {}
        for first, first_coefficient in result.items():
            for second, second_coefficient in polynomial.items():
                exponent = (first[0] + second[0], first[1] + second[1])
                product[exponent] = product.get(exponent, 0) + first_coefficient * second_coefficient
        result = {exponent: coefficient for exponent, coefficient in product.items()
                  if coefficient}
    return result


def polynomial_telescope():
    one = {(0, 0): 1}
    prime_variable = {(1, 0): 1}
    index_variable = {(0, 1): 1}

    def primitive(argument):
        predecessor = polynomial_add(argument, polynomial_scale(one, -1))
        return polynomial_add(
            polynomial_scale(polynomial_multiply(prime_variable, prime_variable,
                                                 argument, predecessor), 6),
            polynomial_scale(polynomial_multiply(prime_variable, argument, predecessor,
                                                 polynomial_add(polynomial_scale(argument, 2),
                                                                polynomial_scale(one, -1))), -4),
            polynomial_scale(polynomial_multiply(argument, argument,
                                                 predecessor, predecessor), 3),
        )

    difference = polynomial_add(primitive(polynomial_add(index_variable, one)),
                                polynomial_scale(primitive(index_variable), -1))
    complement = polynomial_add(prime_variable, polynomial_scale(index_variable, -1))
    target = polynomial_scale(polynomial_multiply(index_variable, complement, complement), 12)
    assert difference == target
    assert primitive(one) == {}
    assert primitive(prime_variable) == {(4, 0): 1, (2, 0): -1}


def main():
    for index, expected in enumerate(SOURCE_PREFIX, 1):
        assert row(index) == expected
    values = {index: row(index) for index in range(1, 257)}
    assert all(rational_row(index) == value for index, value in values.items())
    squares = [[index, value, isqrt(value)] for index, value in values.items()
               if isqrt(value) ** 2 == value]
    assert squares == [[1, 1, 1], [6, 196, 14], [96, 7376656, 2716]]
    polynomial_telescope()
    primes = [number for number in range(2, 258) if trial_prime(number)]
    assert len(primes) == 55
    for prime in primes:
        assert all(gcd(prime - column, column) == 1 for column in range(1, prime))
        assert 12 * row(prime - 1) == prime ** 2 * (prime ** 2 - 1)

    witness_prime = 708158977
    witness_pell_y = 204427888
    factors = {2: 9, 3: 1, 7: 2, 97: 2}
    assert prod(factor ** exponent for factor, exponent in factors.items()) == witness_prime - 1
    assert all(trial_prime(factor) for factor in factors)
    assert pow(5, witness_prime - 1, witness_prime) == 1
    expected_residues = {2: 708158976, 3: 259204175, 7: 342172932, 97: 617955608}
    certificate = []
    for factor, expected_residue in expected_residues.items():
        exponent = (witness_prime - 1) // factor
        residue = pow(5, exponent, witness_prime)
        assert residue == expected_residue
        assert gcd(residue - 1, witness_prime) == 1
        certificate.append([factor, exponent, residue, 1])
    assert isqrt(witness_prime) == 26611
    assert trial_prime(witness_prime)
    assert witness_prime ** 2 - 12 * witness_pell_y ** 2 == 1
    square_root = witness_prime * witness_pell_y
    assert square_root == 144767444036350576
    numerator = witness_prime ** 2 * (witness_prime ** 2 - 1)
    value, remainder = divmod(numerator, 12)
    assert remainder == 0
    assert value == square_root ** 2 == 20957612852817895952216852375531776

    pell_pairs = [[1, 0]]
    for step in range(8):
        pell_x, pell_y = pell_pairs[-1]
        pell_pairs.append([7 * pell_x + 24 * pell_y, 2 * pell_x + 7 * pell_y])
    assert pell_pairs[-1] == [witness_prime, witness_pell_y]
    assert [pair[0] for pair in pell_pairs] == [
        1, 7, 97, 1351, 18817, 262087, 3650401, 50843527, 708158977,
    ]
    for position, (pell_x, pell_y) in enumerate(pell_pairs):
        assert pell_x ** 2 - 12 * pell_y ** 2 == 1
        if position:
            assert [7 * pell_x - 24 * pell_y, 7 * pell_y - 2 * pell_x] == pell_pairs[position - 1]
        if position >= 2:
            assert pell_x == 14 * pell_pairs[position - 1][0] - pell_pairs[position - 2][0]
    intermediate_factors = {3: 7, 4: 31, 5: 7, 6: 97, 7: 7}
    for position, factor in intermediate_factors.items():
        assert 1 < factor < pell_pairs[position][0]
        assert pell_pairs[position][0] % factor == 0
    assert [pair[0] for pair in pell_pairs if trial_prime(pair[0])] == [7, 97, 708158977]

    for successor in range(2, 258):
        expected = row(successor - 1)
        assert divisor_row(successor) == expected
        triangle_product(successor)
    for position in range(1, 257):
        assert position ** 3 // gcd(position, position) ** 3 == 1
        assert gcd(position, position + 1) == 1

    extended_pell = [1, 7]
    for position in range(2, 241):
        extended_pell.append(14 * extended_pell[-1] - extended_pell[-2])
    for index in range(1, 17):
        for odd_multiplier in range(3, 16, 2):
            assert extended_pell[index * odd_multiplier] % extended_pell[index] == 0
    base_pell = [1, 2]
    for position in range(2, 129):
        base_pell.append(4 * base_pell[-1] - base_pell[-2])
    assert all(base_pell[2 * position] == extended_pell[position]
               for position in range(65))
    assert all(base_pell[position] % 2 == 0 for position in range(1, 129, 2))
    power_index_residue = 7
    for exponent in range(65):
        assert power_index_residue == 7
        power_index_residue = (2 * power_index_residue ** 2 - 1) % 30

    modulus = 1310719
    candidate_residues = [2]
    for exponent in range(16):
        candidate_residues.append((2 * candidate_residues[-1] ** 2 - 1) % modulus)
    assert candidate_residues == [
        2, 7, 97, 18817, 370717, 481720, 1068965, 72611, 1291005,
        27224, 1179881, 1184207, 192869, 491881, 1285182, 111332, 0,
    ]
    assert 1 < modulus < base_pell[16]
    assert row(3) == 13 and 4 ** 2 * (4 ** 2 - 1) // 12 == 20

    result = {
        'status': 'PASS',
        'source_prefix_terms': len(SOURCE_PREFIX),
        'integer_and_rational_row_range': [1, 256],
        'square_rows_in_that_range': squares,
        'polynomial_telescope': 'all coefficients and both endpoints agree',
        'prime_row_checks': {'maximum_prime': 257, 'count': len(primes)},
        'primality_certificate_base': 5,
        'primality_certificate_rows_q_exponent_residue_gcd': certificate,
        'independent_trial_division_maximum_divisor': 26611,
        'pell_pairs_t_0_through_8': pell_pairs,
        'witness': {'index': witness_prime - 1, 'root': square_root, 'value': value},
        'all_row_divisor_formula_successor_range': [2, 257],
        'triangle_product_and_totative_product_successor_range': [2, 257],
        'triangle_diagonal_and_adjacent_gcd_range': [1, 256],
        'pell_odd_multiple_divisibility': {'base_indices': [1, 16], 'odd_multipliers': [3, 15]},
        'base_pell_even_index_identity_range': [0, 64],
        'base_pell_odd_index_parity_range': [1, 127],
        'power_of_two_index_residue_modulo_30': {'doubling_steps': 65, 'residue': 7},
        'excluded_candidate': {'sequence': 'A001075', 'index': 65536, 'proper_factor': modulus,
                              'doubling_residues_modulo_factor': candidate_residues},
        'composite_successor_boundary_example': {'index': 3, 'row_sum': 13, 'prime_polynomial_value': 20},
        'coverage': 'Finite arithmetic certificates and bounded row checks; universal identities and Pell descent have written proofs in note.tex.',
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
