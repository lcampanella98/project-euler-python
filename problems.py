from problem import Problem
import math
import tools
import esieve
import os
import io
import re


class Problem8(Problem):

    name = 'Largest product in a series'

    @staticmethod
    def _prod(iterable, default=1):
        p = default
        for var in iterable:
            p *= var
        return p

    def get_solution(self):
        greatest_prod = 0
        number = "731671765313306249192251196744265747423553491949349698352031277" \
                 "45063262395783180169848018694788518438586156078911294949545950173" \
                 "795833195285320880551112540698747158523863050715693290963295227443043" \
                 "5576689664895044524452316173185640309871112172238311362229893423380308" \
                 "135336276614282806444486645238749303589072962904915604407723907138105" \
                 "158593079608667017242712188399879790879227492190169972088809377665727" \
                 "3330010533678812202354218097512545405947522435258490771167055601360483958" \
                 "6446706324415722155397536978179778461740649551492908625693219784686224828" \
                 "39722413756570560574902614079729686524145351004748216637048440319989000889" \
                 "524345065854122758866688116427171479924442928230863465674813919123162824586" \
                 "178664583591245665294765456828489128831426076900422421902267105562632111" \
                 "11093705442175069416589604080719840385096245544436298123098787992724428490" \
                 "9188845801561660979191338754992005240636899125607176060588611646710940507754" \
                 "100225698315520005593572972571636269561882670428252483600823257530420752963450"
        num_adj_digits = 13
        counter = 0
        prod = 1
        for i in range(0, len(number)):
            if counter == num_adj_digits:
                greatest_prod = max(prod, greatest_prod)
                lastnum = int(number[i - num_adj_digits])
                if lastnum != 0:
                    prod //= lastnum
                else:
                    prod = self._prod(map(lambda x: int(x), number[i-num_adj_digits+1:i]))
                counter -= 1
            prod *= int(number[i])
            counter += 1
        return str(greatest_prod)


class Problem9(Problem):

    name = 'Special Pythagorean triplet'

    def get_solution(self):
        m = 2
        n = 1
        sol = 0
        a = 0
        b = 0
        c = 0
        target = 1000
        not_found = True
        while not_found:
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            ssum = a + b + c
            if target % ssum == 0:
                p = target // ssum
                a *= p
                b *= p
                c *= p
                sol = a * b * c
                break
            if ssum > target:
                n += 1
                m = n + 1
            else:
                m += 2
            while math.gcd(m, n) != 1:
                m += 2
        return "The triple [{0}, {1}, {2}] sums to {3}. It's product is {4}".format(a, b, c, target, sol)


class Problem10(Problem):

    name = 'Summation of primes'

    def get_solution(self):
        return str(sum(esieve.get_primes(0, 2000000)))


def triangle_generator():
    tnum = 0
    ti = 1
    while True:
        tnum += ti
        yield tnum
        ti += 1


class Problem12(Problem):

    name = 'Highly divisible triangular number'

    def get_solution(self):
        target_divisors = 500
        for triangle_num in triangle_generator():
            if tools.get_divisor_count(triangle_num) > target_divisors:
                return str(triangle_num)


class Problem13(Problem):

    name = 'Large sum'

    def get_solution(self):
        with open(os.path.join(os.getcwd(), r'resources\problem_13_numbers.txt')) as f:
            return str(sum(map(lambda x: int(x), f.readlines())))[:10]


class Problem14(Problem):

    name = 'Longest Collatz sequence'

    def get_solution(self):
        longest_starting_number = 0
        longest_chain = 0
        memo = []
        for i in range(1, 1000000):
            numterms = 1
            term = i

            while term != 1:
                if term - 1 < len(memo):
                    numterms += memo[term - 1] - 1
                    break
                if term % 2 == 0:
                    term //= 2
                else:
                    term = 3 * term + 1
                numterms += 1
            memo.append(numterms)
            if numterms > longest_chain:
                longest_chain = numterms
                longest_starting_number = i
        return str(longest_starting_number) + " produces " + str(longest_chain) + " terms."


class Problem16(Problem):

    name = 'Power digit sum'

    def get_solution(self):
        num = Problem16.pow(2, 1000)
        return str(tools.digit_sum(num))

    @staticmethod
    def pow(base, power):
        n = base
        cp = 1
        while cp != power:
            if 2*cp <= power:
                n *= n
                cp *= 2
            else:
                n *= base
                cp += 1
        return n


class Problem17(Problem):

    name = 'Number letter counts'

    _one_to_nine = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    _teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    _tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    @staticmethod
    def get_num_string(num):
        num_str = []
        if num < 10:
            num_str.append(Problem17._one_to_nine[num - 1])
        elif num < 100:
            if 20 > num > 10:
                num_str.append(Problem17._teens[num % 10 - 1])
            else:
                num_str.append(Problem17._tens[num // 10 - 1])
                if num % 10 != 0:
                    num_str.append(Problem17._one_to_nine[num % 10 - 1])
        elif num < 1000:
            num_str.append(Problem17._one_to_nine[num // 100 - 1])
            num_str.append('hundred')
            if num % 100 != 0:
                num_str.append('and')
                num_str.extend(Problem17.get_num_string(num % 100))
        elif num == 1000:
            num_str.append('one')
            num_str.append('thousand')
        return num_str

    @staticmethod
    def char_count(a):
        count = 0
        for var in a:
            count += len(var)
        return count

    def get_solution(self):
        charsum = 0
        for i in range(1, 1001):
            num_str = Problem17.get_num_string(i)
            charsum += Problem17.char_count(num_str)

        return str(charsum)


class Problem18(Problem):

    name = 'Maximum path sum I'

    def get_solution(self):
        with io.open(os.path.join(os.getcwd(), r'resources\problem_18_triangle.txt')) as f:
            lines = list(map(lambda x: list(map(lambda y: int(y), x.split(' '))), f.readlines()))
        for i in range(len(lines) - 1, 0, -1):
            for j in range(0, len(lines[i]) - 1):
                lines[i-1][j] += max(lines[i][j], lines[i][j+1])
        return str(lines[0][0])


class Problem19(Problem):

    name = 'Counting Sundays'

    def get_solution(self):
        dow = 0  # 0 : monday ... 6 : sunday
        month_days_dict = {1: 31, 3: 31, 4: 30, 5: 31, 6: 31, 7: 30, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        sunday_count = 0
        for year in range(1901, 2001):
            for month in range(1, 13):
                if month == 2:
                    if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
                        days = 29
                    else:
                        days = 28
                else:
                    days = month_days_dict[month]
                dow = (days + dow) % 7
                if dow == 6:
                    sunday_count += 1
        return str(sunday_count) + ' sundays.'


class Problem100(Problem):

    name = 'Arranged probability'

    def get_solution(self):
        limit = int(math.pow(10, 12))
        b = 15
        t = 21
        while t < limit:
            btemp = 3 * b + 2 * t - 2
            ttemp = 4 * b + 3 * t - 3

            b = btemp
            t = ttemp
        return str(b)


class Problem20(Problem):

    name = 'Factorial Digit Sum'

    def get_solution(self):
        num = 100
        return 'The sum of digits in ' + str(num) + '! is ' + str(tools.digit_sum(tools.factorial(num)))


class Problem21(Problem):

    name = 'Amicable numbers'

    def __init__(self):
        self._memo = []

    def get_solution(self):
        limit = 10000
        primes = esieve.get_primes(int(math.sqrt(limit) + 1))
        self._memo = [0] * limit
        amicable_sum = 0
        for i in range(2, limit):
            self._memo[i] = tools.sum_of_factors_prime(i, primes)
        for i in range(2, limit):
            try:
                di = self._memo[i]
                ddi = self._memo[di]
                if i == ddi and i != di:
                    print('d({0}) = {1}'.format(i, di))
                    print('adding {0} to the sum'.format(i))
                    amicable_sum += i
            except IndexError:
                pass
        return 'The sum of amicable numbers under {0} is {1}'.format(limit, amicable_sum)


class Problem22(Problem):

    name = 'Names scores'

    def get_solution(self):
        with io.open(os.path.join(os.getcwd(), r'resources\p022_names.txt')) as f:
            names = list(map(lambda x: re.sub(r'"', '', x), f.readline().split(',')))
        names.sort(key=tools.cmp_to_key(Problem22.letter_cmp))

    @staticmethod
    def letter_cmp(x, y):
        for i in range(0, min(len(x), len(y))):
            cx = ord(x[i])
            cy = ord(y[i])
            if cx > cy:
                return 1
            elif cx < cy:
                return -1
        return -1


class Problem23(Problem):

    name = 'Non-abundant sums'

    def get_solution(self):
        limit = 28123
        primes = esieve.get_primes(limit)
        abundant_nums = []

        for i in range(1, limit):
            di = tools.sum_of_factors_prime(i, primes)
            if di > i:
                abundant_nums.append(i)
        can_be_written = set()
        for i in range(0, len(abundant_nums)):
            ab1 = abundant_nums[i]
            for j in range(i, len(abundant_nums)):
                isum = ab1 + abundant_nums[j]
                if isum < limit:
                    can_be_written.add(isum)
                    pass
                else:
                    break
        zsum = int(tools.sum_sequence(1, 1, limit - 1))

        return 'the sum of integers is {0}'.format(str(zsum - sum(can_be_written)))





