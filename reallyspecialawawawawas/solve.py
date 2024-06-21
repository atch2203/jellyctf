import functools
import math


def egcd(a, b):
    """Extended gcd of a and b. Returns (d, x, y) such that
    d = a*x + b*y where d is the greatest common divisor of a and b."""
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def inverse(a, n):
    """Returns the inverse x of a mod n, i.e. x*a = 1 mod n. Raises a
    ZeroDivisionError if gcd(a,n) != 1."""
    d, a_inv, n_inv = egcd(a, n)
    if d != 1:
        raise ZeroDivisionError('{} is not coprime to {}'.format(a, n))
    else:
        return a_inv % n


def lcm(*x):
    """
    Returns the least common multiple of its arguments. At least two arguments must be
    supplied.
    :param x:
    :return:
    """
    if not x or len(x) < 2:
        raise ValueError("at least two arguments must be supplied to lcm")
    lcm_of_2 = lambda x, y: (x * y) // math.gcd(x, y)
    return functools.reduce(lcm_of_2, x)


def carmichael_pp(p, e):
    phi = pow(p, e - 1) * (p - 1)
    if (p % 2 == 1) or (e >= 2):
        return phi
    else:
        return phi // 2


def carmichael_lambda(pp):
    """
    pp is a sequence representing the unique prime-power factorization of the
    integer whose Carmichael function is to be computed.
    :param pp: the prime-power factorization, a sequence of pairs (p,e) where p is prime and e>=1.
    :return: Carmichael's function result
    """
    return lcm(*[carmichael_pp(p, e) for p, e in pp])

n = 40095322948381328531315369020145890848992927830000776301309425505
e = 65537
cip = 35622053067320123838840878683947610930876835359945867019927573838

from sympy.ntheory import factorint
#factors = factorint(n)
#print(factors)
# {5: 1, 23: 1, 460465412038271581: 1, 757179525420813109550252454787205779901919127: 1}

factors = [(5,1), (23,1), (460465412038271581,1), (757179525420813109550252454787205779901919127,1)]
#d = inverse(e, carmichael_lambda(factors))
#print(d)
d = 287458461584463336135331697997301511216944981741119712297623893

m=pow(cip,d,n)
h = hex(m)
print(h)
print(bytes.fromhex(h[2:]).decode())


"""
https://stackoverflow.com/questions/58750417/how-to-decrypt-an-rsa-encryption
https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Decryption
https://crypto.stackexchange.com/questions/74891/decrypting-multi-prime-rsa-with-e-n-and-factors-of-n-given

jellyCTF{awawas_4_every1}
"""

