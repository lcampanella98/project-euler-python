from tools import tools


class DigitNum:
    def __init__(self, n):
        self.digits = []
        self.set_digits(n)

    def set_digits(self, n):
        self.digits = tools.get_digits(n)

    def increment(self):
        for i in range(len(self.digits) - 1, -1, -1):
            if self.digits[i] != 9:
                self.digits[i] += 1
                break
            else:
                self.digits[i] = 0
                if i != 0:
                    continue
                else:
                    self.digits.insert(0, 1)