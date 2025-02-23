import numpy as np

class DichotomySearch:
    def __init__(self, func, start, end, eps):
        self._func = func
        self._start = start
        self._end = end
        self._eps = eps

    @property
    def func(self):
        return self._func

    @func.setter
    def func(self, value):
        self._func = value

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        if value >= self.end:
            raise ValueError("Start должно быть меньше end.")
        self._start = value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        if value <= self.start:
            raise ValueError("End должно быть больше start.")
        self._end = value

    @property
    def eps(self):
        return self._eps

    @eps.setter
    def eps(self, value):
        if value <= 0:
            raise ValueError("Epsilon должно быть положительным.")
        self._eps = value

    def search(self, flag):
        a = self.start
        b = self.end
        delta = self.eps
        iteration = 0

        while True:
            iteration += 1

            x1 = (b + a - delta) / 2
            x2 = (b + a + delta) / 2
            
            f_x1 = self.func(x1)
            f_x2 = self.func(x2)

            if flag:  # true для максимума
                if f_x1 >= f_x2:
                    b = x2
                else:
                    a = x1
            else:  # false для минимума
                if f_x1 <= f_x2:
                    b = x2
                else:
                    a = x1

            epsilon_n = (b - a) / 2

            if epsilon_n < self.eps:
                break

        return (a + b) / 2, iteration