import time


def stopwatch(my_function):
    def wrapper(*args, **kwargs):
        start = time.time()
        my_function(*args, **kwargs)
        end = time.time()
        print("======================")
        print("Code excecuted in {0} ms".format(1000 * (end - start)))

    return wrapper


class Problem:

    name = ''

    @stopwatch
    def run(self):
        print(self.get_solution())

    def get_solution(self):
        pass
