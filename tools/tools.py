import math


def get_divisor_count(num):
    dcount = 2
    sroot = int(math.sqrt(num))
    if sroot * sroot == num:
        dcount += 1
    for i in range(2, sroot):
        if num % i == 0:
            dcount += 2
    return dcount


def simplify_fraction(n, d):
    gcd = math.gcd(n, d)
    return [n // gcd, d // gcd]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    nd = num_digits(n)
    digits = []
    for _ in range(nd // 2):
        digits.append(n % 10)
        n //= 10
    if nd % 2 == 1:
        n //= 10
    for d in reversed(digits):
        if n % 10 != d:
            return False
        n //= 10
    return True


def is_palindrome_binary(b):
    m = 0
    nd = num_digits(b, 2)
    for i in range(nd // 2):
        m = (m << 1) + (b & 1)
        b >>= 1
    if nd % 2 == 1:
        b >>= 1
    for _ in range(nd // 2):
        if b & 1 != m & 1:
            return False
        b >>= 1
        m >>= 1
    return True


def rotate(n):
    l = n % 10
    r = n // 10
    n = r
    m = 1
    while n > 0:
        m *= 10
        n //= 10
    return m * l + r


def are_lists_equal(l1, l2):
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True


def get_digits(n):
    digits = [n % 10]
    n //= 10
    while n > 0:
        digits.insert(0, n % 10)
        n //= 10
    return digits


def digit_sum(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s


def is_square(apositiveint):
    x = apositiveint // 2
    seen = {x}
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen:
            return False
    seen.add(x)
    return True


def num_digits(n, base=10):
    if base == 10:
        l = math.log10(n)
    elif base == 2:
        l = math.log2(n)
    else:
        l = math.log(n, base)
    return int(math.floor(l) + 1)


def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 1


def factorial(n):
    if n == 0:
        return 1
    fact = n
    while n > 1:
        n -= 1
        fact *= n
    return fact


def cmp_to_key(mycmp):
    """Convert a cmp= function into a key= function"""

    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


def sum_sequence(a0, d, n):
    an = a0 + d * (n - 1)
    return n * (a0 + an) / 2


def prime_factorization(n, primes):
    factorization = {}
    if n == 1:
        return factorization
    i = 0
    while n > 0 and i < len(primes):
        p = primes[i]
        if p > n:
            break
        if n % p == 0:
            factorization[p] = 1
            n //= p
            while n % p == 0:
                factorization[p] += 1
                n //= p
        i += 1
    if len(factorization) == 0:
        factorization[n] = 1
    return factorization


def sum_of_factors_prime(num, primes):
    n = num
    fsum = 1
    p = primes[0]
    i = 0
    while p * p <= n and n > 1 and i < len(primes):
        p = primes[i]
        i += 1
        if n % p == 0:
            j = p * p
            n //= p
            while n % p == 0:
                j *= p
                n //= p
            fsum *= (j - 1) // (p - 1)
    if n > 1:
        fsum *= n + 1
    return fsum - num


def made_a_random_function():
    pass
