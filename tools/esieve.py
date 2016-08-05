import math


def get_primes(ceiling, floor=2):
    flags = [True] * (ceiling+1)
    primes = []
    flags[0] = False
    flags[1] = False
    bound = int(math.sqrt(ceiling))
    for i in range(2, bound + 1, 1):
        if flags[i]:
            for j in range(2*i, len(flags), i):
                flags[j] = False

    for i in range(floor, ceiling):
        if flags[i]:
            primes.append(i)
    return primes
