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
        temp = self.value[i]
        self.value[i] = self.value[j]
        self.value[j] = temp
