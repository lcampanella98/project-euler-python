import time


def stopwatch(my_function):
    def wrapper(*args, **kwargs):
        start = time.time()
        sol = my_function(*args, **kwargs)
        end = time.time()
        print(sol)
        print("======================")
        print("Code excecuted in " + str(1000 * (end - start)) + " ms")

    return wrapper


class Problem:

    name = ''

    @stopwatch
    def run(self):
        return self.get_solution()

    def get_solution(self):
        pass
