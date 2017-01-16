import io
import math
import os
import re
import bisect

from problem import Problem
from tools import tools, esieve, permutation, digit_num


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
                    prod = self._prod(map(lambda x: int(x), number[i - num_adj_digits + 1:i]))
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
            if 2 * cp <= power:
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
                lines[i - 1][j] += max(lines[i][j], lines[i][j + 1])
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
        amicable_sum = 0

        for i in range(2, limit):
            di = tools.sum_of_factors_prime(i, primes)
            if di > i:
                if tools.sum_of_factors_prime(di, primes) == i:
                    amicable_sum += i + di

        return 'The sum of amicable numbers under {0} is {1}'.format(limit, amicable_sum)


class Problem22(Problem):
    name = 'Names scores'

    def get_solution(self):
        score_total = 0
        with io.open(os.path.join(os.getcwd(), r'resources\p022_names.txt')) as f:
            names = list(map(lambda x: re.sub(r'"', '', x), f.readline().split(',')))
        names.sort(key=tools.cmp_to_key(Problem22.letter_cmp))

        for i in range(0, len(names)):
            score_total += Problem22.name_points(names[i]) * (i + 1)
        return 'The total score is {0}'.format(score_total)

    @staticmethod
    def name_points(name):
        a_val = ord('A')
        pts = 0
        for c in name:
            pts += ord(c) - a_val + 1
        return pts

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

        #  find all abundant numbers
        for i in range(2, limit + 1):
            di = tools.sum_of_factors_prime(i, primes)
            if di > i:
                abundant_nums.append(i)

        # find all sums of two abundant numbers
        sums_list = [False] * limit
        for i in range(0, len(abundant_nums)):
            ab1 = abundant_nums[i]
            for j in range(i, len(abundant_nums)):
                if ab1 + abundant_nums[j] < limit:
                    sums_list[ab1 + abundant_nums[j]] = True
                else:
                    break

        # sum all numbers < limit that cannot be written as a sum
        non_abundant_sum = 0
        for i in range(0, len(sums_list)):
            if not sums_list[i]:
                non_abundant_sum += i

        return 'the sum of integers is {0}'.format(non_abundant_sum)


class Problem24(Problem):
    name = 'Lexicographic Permutations'

    def get_solution(self):
        num = 10
        i = 1000000
        permutations = permutation.Permutation(num).permute(i)
        return str(permutations[i - 1])


class Problem25(Problem):
    name = '1000-digit Fibonacci Number'

    def get_solution(self):
        target_digits = 1000
        index = 3
        terms = []
        to_store = 150
        fm1 = 1
        fm2 = 1
        while True:
            f = fm1 + fm2
            if len(terms) < to_store:
                terms.append(f)
            else:
                if tools.num_digits(f) >= target_digits:
                    for i, t in enumerate(terms):
                        if tools.num_digits(t) == target_digits:
                            return 'The index of first fib term to contain 1000 digits is {0}'.format(index - len(terms) + i)
                else:
                    terms.clear()
            fm2 = fm1
            fm1 = f
            index += 1

        return 'not found'


class Problem26(Problem):
    name = 'Reciprocal Cycles'

    def get_solution(self):
        longest_d = 0

        longest_recurring_cycle_ct = 0
        for d in range(2, 1000):
            remainders = []
            r = 1
            while True:
                while r < d:
                    r *= 10
                qd = r // d
                r -= d * qd
                if r == 0:
                    break
                elif r in remainders:
                    ccount = len(remainders) - remainders.index(r)
                    if longest_recurring_cycle_ct < ccount:
                        longest_recurring_cycle_ct = ccount
                        longest_d = d
                    break
                else:
                    remainders.append(r)
        return "The denominator less than 1000 with the longest reciprocal count was {0} with a cycle count of {1} "\
            .format(longest_d, longest_recurring_cycle_ct)


class Problem27(Problem):
    name = 'Quadratic Primes'

    def get_solution(self):
        primes = esieve.get_primes(1000)
        max_consec = 0
        max_prod = 0
        max_pair = ()
        for b in primes:
            for a in range(-999, 1000, 2):
                n = 1
                while tools.is_prime(n * n + a * n + b):
                    n += 1
                if n - 1 > max_consec:
                    max_consec = n - 1
                    max_prod = a * b
                    max_pair = (a, b)
        return 'The maximum product with {} consecutive primes is {} with pair {}'.format(max_consec, max_prod, max_pair)


class Problem33(Problem):
    name = 'Digit Cancelling Fractions'

    def get_solution(self):
        dtotal = 1
        ntotal = 1
        for d in range(10, 100):
            dmod10 = d % 10
            dover10 = d // 10
            if dmod10 == 0:
                continue
            for n in range(10, d):
                nmod10 = n % 10
                nover10 = n // 10
                n1 = 1
                d1 = 1
                if nmod10 == 0:
                    continue
                if dmod10 == nover10:
                    n1 = nmod10
                    d1 = dover10
                elif dmod10 == nmod10:
                    n1 = nover10
                    d1 = dover10
                elif dover10 == nmod10:
                    n1 = nover10
                    d1 = dmod10
                elif dover10 == nover10:
                    n1 = nmod10
                    d1 = dmod10
                if tools.are_lists_equal(tools.simplify_fraction(n, d), tools.simplify_fraction(n1, d1)):
                    print('{0}/{1} reduced to {2}/{3}'.format(n, d, n1, d1))
                    ntotal *= n
                    dtotal *= d
        return 'The result is: {0}'.format(tools.simplify_fraction(ntotal, dtotal)[1])


class Problem34(Problem):
    name = 'Digit Factorials'

    def get_solution(self):
        lim = 2540160
        total_sum = 0
        facts = list(map(lambda x: tools.factorial(x), (i for i in range(10))))
        digits = digit_num.DigitNum(10)
        for n in range(10, lim):
            if n == sum(facts[d] for d in digits.digits):
                total_sum += n
            digits.increment()
        return 'The sum of all digit factorials is {0}'.format(total_sum)


class Problem35(Problem):
    name = 'Circular Primes'

    def get_solution(self):
        num_circular = 0
        primes = esieve.get_primes(1000000)

        for p in primes:
            pr = tools.rotate(p)
            while pr != p:
                if not tools.is_prime(pr):
                    break
                pr = tools.rotate(pr)
            if pr == p:
                num_circular += 1
        return 'There are {0} circular primes below 1000000'.format(num_circular)


class Problem36(Problem):
    name = 'Double-Base Palindromes'

    def get_solution(self):
        lim = 1000000
        p_sum = 0
        print(tools.is_palindrome_binary(int('11110001111', base=2)))
        for i in range(1, lim):
            if tools.is_palindrome(i):
                if tools.is_palindrome_binary(i):
                    p_sum += i

        return 'The sum of all double-base palindromes < 1000000 is {0}'.format(p_sum)


class Problem37(Problem):
    name = 'Truncatable Primes'
    lpds = [2, 3, 5, 7]
    rpds = [3, 7]
    ods = [1, 3, 7, 9]

    def __init__(self):
        self.t_primes = []

    def insert_next(self, n):
        if not tools.is_prime(n // 10):
            return
        is_t_prime = True
        for t in tools.truncate_to_right(n):
            if not tools.is_prime(t):
                is_t_prime = False
                break
        if is_t_prime:
            self.t_primes.append(n)
        nmod10 = n % 10
        for od in self.ods:
            self.insert_next(10 * (n - nmod10 + od) + nmod10)

    def get_solution(self):
        for pdright in self.rpds:
            for pdleft in self.lpds:
                n = 10 * pdleft + pdright
                self.insert_next(n)
        print(self.t_primes)
        return 'The sum of truncatable primes is {0}'.format(sum(self.t_primes))


class Problem38(Problem):
    name = 'Pandigital Multiples'

    def get_solution(self):
        base_num = 98765432
        largest_pandigital = 0
        starting_num = 0
        floor = 123456789
        ceil = 987654321
        while base_num > 0:
            base_num_digits = tools.num_digits(base_num)
            base_limit = int(math.floor(math.pow(10, base_num_digits - 1)))
            print('{0}, {1}'.format(base_num, base_limit))
            for num in range(base_num, 9 * base_limit, -1):
                if num % 5 == 0:
                    continue
                m = num
                con = num
                while con < floor:
                    m += num
                    con = con * int(math.pow(10, tools.num_digits(m))) + m

                if con <= ceil:
                    if tools.is_1_to_9_pandigital(con):
                        print('{0} -> {1}'.format(num, con))
                        if con > largest_pandigital:
                            largest_pandigital = con
                            starting_num = num
            base_num //= 10

        return 'The largest pandigital multiple is {0} with a starting numner of {1}'.format(largest_pandigital, starting_num)


class Problem39(Problem):
    name = 'Integer Right Triangles'

    def get_solution(self):
        ps = [0] * 1001
        max_perimeter = 1000
        n = 1
        m = n + 1
        just_set_n = True
        while True:
            while math.gcd(m, n) != 1:
                m += 2
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            p = a + b + c
            if p > max_perimeter:
                if just_set_n:
                    break
                n += 1
                m = n + 1
                just_set_n = True
                continue
            ps[p] += 1
            mul_p = p + p
            while mul_p <= max_perimeter:
                ps[mul_p] += 1
                mul_p += p
            just_set_n = False
            m += 2
        most_hit = 0
        max_hits = 0
        for i in range(len(ps)):
            if ps[i] > max_hits:
                most_hit = i
                max_hits = ps[i]
        return 'The most-hit perimeter for p <= {} was {}'.format(max_perimeter, most_hit)


class Problem40(Problem):
    name = 'Champerown\'s Constant'

    def get_solution(self):
        curr_n = 1
        lim_num_n = 7
        num_n = 0
        d = 0
        num_d = 0
        d_inc = 0
        mod = 1
        total = 1
        while num_n < lim_num_n:
            d += 1
            if d % mod == 0:
                d_inc += 1
                mod *= 10
            num_d += d_inc
            if num_d >= curr_n:
                d_list = tools.get_digits(d)
                curr_d = d_list[len(d_list) - 1 - (num_d - curr_n)]
                total *= curr_d
                curr_n *= 10
                num_n += 1
        return total


class Problem41(Problem):
    name = 'Pandigital Prime'

    def get_solution(self):
        for n in range(9, 1, -1):
            a = [i for i in range(n, 0, -1)]
            p = permutation.DescendingPermutation(a)
            while p.get_next():
                if a[-1] % 2 == 0:
                    continue
                if sum(a) % 3 == 0:
                    continue
                num = tools.get_num(p.a)
                if tools.is_prime(num):
                    return 'The largest pandigital prime is {}'.format(num)
        return 'not found'


class Problem42(Problem):
    name = 'Coded Triangle Numbers'

    def get_solution(self):
        words_file = open('resources/p042_words.txt')
        words = words_file.read().split(',')

        self.triangle_numbers = [1]
        t_count = 0
        for w in words:
            val = self.get_word_value(w.strip('"'))
            if val > self.triangle_numbers[-1]:
                self.extend_triangle_numbers(val)
            if val in self.triangle_numbers:
                t_count += 1

        return 'There are {} words with triangle coding in the file'.format(t_count)

    def extend_triangle_numbers(self, limit):
        n = len(self.triangle_numbers) + 1
        next_n = (n * (n + 1)) // 2
        while next_n <= limit:
            n += 1
            self.triangle_numbers.append(next_n)
            next_n = (n * (n + 1)) // 2

    upper_a = ord('A')

    @staticmethod
    def get_word_value(u_word):
        v = 0
        for c in u_word:
            v += Problem42.get_char_value(c)
        return v

    @staticmethod
    def get_char_value(uc):
        return ord(uc) - Problem42.upper_a + 1


class Problem43(Problem):
    name = 'Sub-String Divisibility'

    def __init__(self):
        self.div = [2, 3, 5, 7, 11, 13, 17]

    def get_solution(self):
        digits = [False] * 10
        self.found = []
        num_d = []
        num = 0
        self.get_next(digits, num_d, num)
        total = sum(self.found)
        return 'There were {} 1-9 pandigital numbers that satisfied the property with a sum of {}'.format(len(self.found), total)

    def get_next(self, digits, num_d, num):
        if len(num_d) < 3:
            start = 1 if len(num_d) == 0 else 0
            for i in range(start, len(digits)):
                if digits[i]:
                    continue
                digits[i] = True
                self.get_next(digits, num_d + [i], 10 * num + i)
                digits[i] = False
        elif len(num_d) == len(digits):
            self.found.append(num)
        else:
            ten_num = 10 * num
            for i in range(len(digits)):
                if digits[i]:
                    continue
                new_num = ten_num + i
                if (new_num % 1000) % self.div[len(num_d) + 1 - 4] == 0:
                    digits[i] = True
                    self.get_next(digits, num_d + [i], new_num)
                    digits[i] = False

    def get_solution_bf(self):
        a = [i for i in range(9, -1, -1)]
        p = permutation.DescendingPermutation(a)
        ct = 0
        n_sum = 0
        while True:
            # if self.satisfies_property(p.a):
            #     ct += 1
            #     n_sum += tools.get_num(p.a)
            if not p.get_next():
                break

        return 'There were {} 1-9 pandigital numbers that satisfied the property with a sum of {}'.format(ct, n_sum)

    def satisfies_property(self, a):
        offset = 3
        for i in range(3, len(a)):
            n = a[i] + 10 * a[i - 1] + 100 * a[i - 2]
            m = self.div[i - offset]
            if n % m != 0:
                return False
        return True


class Problem44(Problem):
    name = 'Pentagon Numbers'

    def __init__(self):
        self.p = []

    def get_solution(self):
        self.p = [1]
        n = 2
        d = None
        best_pair = None
        while True:
            if d is not None:# and self.p[n] - self.p[n - 1] >= d:
                return 'Found the pair {}, {} with a difference of {}'.format(best_pair[0], best_pair[1], d)
            ext_n = 2 * n - 1
            self.extend_numbers_to(ext_n)

            for jn in range(n + 1, ext_n + 1):
                if self.is_good_pair(n, jn):
                    best_pair = (self.p[n - 1], self.p[jn - 1])
                    d = best_pair[1] - best_pair[0]
            for jn in range(n // 2):
                if self.is_good_pair(jn + 1, n):
                    best_pair = (self.p[jn], self.p[n - 1])
                    d = best_pair[1] - best_pair[0]
            n += 1

        return 'not found'

    def extend_numbers_to(self, max_n):
        n = len(self.p) + 1
        for c_n in range(n, max_n + 1):
            self.p.append((c_n * (3 * c_n - 1)) // 2)

    def extend_numbers_while_lt(self, limit):
        n = len(self.p) + 1
        next_n = (n * (3 * n - 1)) // 2
        while next_n <= limit:
            n += 1
            self.p.append(next_n)
            next_n = (n * (3 * n - 1)) // 2

    def is_good_pair(self, n1, n2):
        p1, p2 = self.p[n1 - 1], self.p[n2 - 1]
        diff = p2 - p1
        ret = True
        if self.p[bisect.bisect_left(self.p, diff, lo=0, hi=n2)] != diff:
            ret = False
            # return False
        else:
            pass
            #print('{} and {} have difference {}'.format(p1, p2, diff))
        s = p2 + p1
        if s > self.p[-1]:
            self.extend_numbers_while_lt(s)
            if s != self.p[-1]:
                ret = False
            else:
                pass
                #print('{} and {} have sum {}'.format(p1, p2, s))
        else:
            if self.p[bisect.bisect_left(self.p, s, lo=n2)] != s:
                ret = False
            else:
                pass
                #print('{} and {} have sum {}'.format(p1, p2, s))
        return ret


class Problem45(Problem):
    name = 'Triangular, pentagonal, and hexagonal'

    def get_solution(self):
        pent_n = 166
        pent_v = 1
        while True:
            pent_v = pent_n * (3 * pent_n - 1) // 2
            if self.is_triangular_and_hexagonal(pent_v):
                break
            pent_n += 1
        return 'The next such number is {}'.format(pent_v)

    @staticmethod
    def is_triangular_and_hexagonal(num):
        rt = tools.is_square_get(8 * num + 1)
        if rt is None:
            return False
        return (rt + 1) % 4 == 0


class Problem46(Problem):
    name = 'Goldbach\'s other conjecture'

    def get_solution(self):
        p_floor, p_ceil = 3, 10000
        primes = esieve.get_primes(p_ceil, floor=p_floor)
        largest_square = int(math.sqrt((p_ceil - p_floor) / 2))
        largest_prime = primes[-1]
        p_squares = {p: 1 for p in primes}
        squares = [i * i for i in range(largest_square + 1)]
        nums = set()

        for p in primes:
            while True:
                n = p + 2 * squares[p_squares[p]]
                if n > largest_prime:
                    break
                nums.add(n)
                p_squares[p] += 1
                if p_squares[p] >= len(squares):
                    break
        n = 5
        found = set()
        while n <= largest_prime:
            if n not in nums and n not in primes:
                found.add(n)
            n += 2
        if len(found) == 0:
            return 'None found'
        else:
            return 'The smallest n found was {}'.format(min(found))


class Problem47(Problem):
    name = 'Distinct Prime Factors'

    def get_solution(self):
        p_ceil = 1000000
        primes = esieve.get_primes(p_ceil)
        target_dpf = 4
        target_consec = 4
        n = 647
        num_str = []
        while True:
            if tools.num_distinct_prime_factors(n, primes) == target_dpf:
                num_str.append(n)
                if len(num_str) == target_consec:
                    break
            else:
                num_str.clear()
            n += 1
            if n % 1000 == 0:
                print(n)

        return 'The first sequence of {} integers to have {} distinct prime factors is {}'.format(target_consec, target_dpf, str(num_str))


class Problem48(Problem):
    name = 'Self Powers'

    @staticmethod
    def ipow(x, y):
        r = 1
        for i in range(y):
            r *= x
        return r

    def get_solution(self):
        m = self.ipow(10, 10)
        s = 0
        for i in range(1, 1001):
            s += self.ipow(i, i)
            s %= m
        return 'The result is {}'.format(s)


class Problem49(Problem):
    name = 'Prime Permutations'

    def get_solution(self):
        primes = esieve.get_primes(9999, floor=1000)
        l_prime = primes[-1]
        seqs = []
        for i in range(len(primes)):
            pi = primes[i]
            for j in range(i + 1, len(primes)):
                pj = primes[j]
                pk = pj + pj - pi
                if pk > l_prime:
                    continue
                if primes[bisect.bisect_left(primes, pk, lo=j + 1)] == pk:
                    if tools.is_perm(pi, pj) and tools.is_perm(pj, pk):
                        seqs.append((pi, pj, pk))
        seq = seqs[1] if seqs[0][0] == 1487 else seqs[0]
        return 'The sequence is {}'.format(str(seq[0]) + str(seq[1]) + str(seq[2]))


class Problem50(Problem):
    name = 'Consecutive Prime Sum'

    def get_solution(self):
        lim = 1000000
        primes = esieve.get_primes(lim)
        n_primes = len(primes)
        l_prime = primes[-1]
        longest_str = 0
        longest_num = 0

        for i in range(n_primes):
            n = primes[i]
            j = i + 1
            str_len = 1
            while j < n_primes:
                str_len += 1
                n += primes[j]
                if n > l_prime:
                    break
                if str_len < longest_str:
                    j += 1
                    continue
                if tools.is_prime(n):
                    longest_str = str_len
                    longest_num = n
                j += 1
        return 'The number with the longest consecutive prime sum below {} is {} with {} consecutive primes'.format(lim, longest_num, longest_str)


class Problem51(Problem):
    name = 'Prime digit replacements'

    @staticmethod
    def get_digit_info(n):
        di = {}
        d = [n % 10]
        n //= 10
        while n > 0:
            d.insert(0, n % 10)
            n //= 10
        for i in range(len(d) - 2, -1, -1):
            if d[i] in di:
                di[d[i]].append(i)
            else:
                di[d[i]] = [i]
        return d, di

    def get_solution(self):
        lim = 300000
        prime_family_size = 8
        num_replacements = 3
        primes = esieve.get_primes(lim, floor=1000)
        patterns = set()
        for p in primes:
            digits, d_info_dict = self.get_digit_info(p)
            for d in d_info_dict:
                if len(d_info_dict[d]) != num_replacements:
                    continue
                pat_n = 0
                pat_rep = ''
                for i in range(len(digits)):
                    cd = digits[i]
                    if cd != d:
                        pat_n = 10 * pat_n + cd
                    else:
                        pat_rep += str(i)
                pat = (pat_n, pat_rep)
                if pat in patterns:
                    continue
                patterns.add(pat)

                smallest = p
                primes_needed = prime_family_size - 1
                nums_left = 9
                cur_primes = [p]
                for i in range(10):
                    if i == d:
                        continue
                    nums_left -= 1
                    if i == 0 and 0 in d_info_dict[d]:
                        continue
                    n = 0
                    digit_info_index = len(d_info_dict[d]) - 1
                    for j in range(len(digits)):
                        if digit_info_index < 0 or j != d_info_dict[d][digit_info_index]:
                            n = 10 * n + digits[j]
                        else:
                            digit_info_index -= 1
                            n = 10 * n + i
                    if tools.is_prime(n):
                        cur_primes.append(n)
                        if n < smallest:
                            smallest = n
                        primes_needed -= 1
                    if nums_left < primes_needed:
                        break
                if primes_needed <= 0:
                    return 'The smallest prime with an {}-prime value family is {} with family {}'.format(prime_family_size, smallest, cur_primes)


class Problem52(Problem):
    name = 'Permuted Multiples'

    def get_solution(self):
        start_n = [12, 123, 1234, 12345, 123456, 1234567, 12345678]
        max_n = [99, 999, 9999, 99999, 999999, 9999999, 99999999]
        for i in range(len(start_n)):
            n = start_n[i]
            limit = max_n[i]
            while 6 * n <= limit:
                digit_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                temp_n = n
                ok = True
                while temp_n > 0:
                    m = temp_n % 10
                    digit_counts[m] += 1
                    if digit_counts[m] > 1:
                        ok = False
                        break
                    temp_n //= 10
                if not ok:
                    n += 1
                    continue
                for m in range(2, 7):
                    if self.get_digit_counts(m * n) != digit_counts:
                        ok = False
                        break
                if ok:
                    return 'Found {}'.format(n)
                n += 1
        return 'Found nothing'

    @staticmethod
    def get_digit_counts(n):
        dc = [0] * 10
        while n > 0:
            dc[n % 10] += 1
            n //= 10
        return dc


class Problem53(Problem):
    name = 'Combinatoric Selections'

    def get_solution(self):
        ct = 0
        for n in range(23, 101):
            k = 1
            c = 1
            while k < n - k:
                c *= (n + 1 - k) / k
                if c > 1000000:
                    ct += 2
                k += 1
            if k == n - k:
                c *= (n + 1 - k) / k
                if c > 1000000:
                    ct += 1

        return 'Counted {} combinations over 1000000'.format(ct)


class Problem55(Problem):
    name = 'Lychrel Numbers'

    def __init__(self):
        self.lychrel_nums = set()

    def get_solution(self):
        for n in range(1, 10000):
            self.check_lychrel(n, [], 0)
        return 'There are {} lychrel numbers under 10000'.format(len(self.lychrel_nums))

    def check_lychrel(self, n, curr_pairs, iters):
        if iters >= 50 or n in self.lychrel_nums:
            return
        n_rev = self.get_reversed_num(n)
        new_n = n + n_rev
        if tools.is_palindrome(new_n):
            if n < 10000:
                self.lychrel_nums.add(n)
            if n_rev < 10000:
                self.lychrel_nums.add(n_rev)
            for p in curr_pairs:
                for num in p:
                    self.lychrel_nums.add(num)
            return
        if n < 10000:
            if n_rev < 10000:
                curr_pairs.append((n, n_rev))
            else:
                curr_pairs.append((n,))
        else:
            if n_rev < 10000:
                curr_pairs.append((n_rev,))
        self.check_lychrel(new_n, curr_pairs, iters + 1)

    @staticmethod
    def get_reversed_num(n):
        rev = 0
        while n > 0:
            rev = 10 * rev + n % 10
            n //= 10
        return rev
