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
