from tools import tools


class Permutation:

    def __init__(self, n):
        self.n = n
        self.fact = tools.factorial(n)
        self.value = [i for i in range(0, n)]
        self.permutations = []

    def permute(self, stop=None):
        end = self.fact if stop is None else stop
        for i in range(0, end):
            self.permutations.append(list(self.value))
            try:
                self.get_next()
            except IndexError:
                pass
        return self.permutations

    def get_next(self):
        i = self.n - 1
        while self.value[i-1] >= self.value[i]:
            i -= 1
        j = self.n
        while self.value[j-1] <= self.value[i-1]:
            j -= 1
        self.swap(i-1, j-1)

        i += 1
        j = self.n
        while i < j:
            self.swap(i-1, j-1)
            i += 1
            j -= 1

    def swap(self, i, j):
        t = self.value[i]
        self.value[i] = self.value[j]
        self.value[j] = t


class DescendingPermutation:

    def __init__(self, a):
        self.a = a

    def get_next(self):
        len_a = len(self.a)
        i = len_a - 1
        while i > 0 and self.a[i - 1] <= self.a[i]:
            i -= 1

        if i <= 0:
            return False

        j = len_a - 1
        while self.a[j] >= self.a[i - 1]:
            j -= 1

        self.swap(i - 1, j)

        self.reverse(i, len_a - 1)

        return True

    def reverse(self, i, j):
        while i < j:
            self.swap(i, j)
            i += 1
            j -= 1

    def swap(self, i, j):
        t = self.a[i]
        self.a[i] = self.a[j]
        self.a[j] = t
