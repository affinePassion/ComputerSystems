import numpy as np

class ChordSearch:
    def __init__(self, func, start, end, eps, max_iter=1000):
        self._func = func
        self._start = start
        self._end = end
        self._eps = eps
        self._max_iter = max_iter 

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

    @property
    def max_iter(self):
        return self._max_iter

    @max_iter.setter
    def max_iter(self, value):
        if value <= 0:
            raise ValueError("Максимальное количество итераций должно быть положительным.")
        self._max_iter = value

    def _derivative(self, x):
        # Вычисление производной для функции x^5 * sin(5x)
        return 5 * x**4 * np.sin(5 * x) + 5 * x**5 * np.cos(5 * x)

    def search(self):
        a = self.start
        b = self.end
        prev_x = None
        current_x = None
        iteration = 0 

        while iteration < self.max_iter:
            iteration += 1

            # Вычисляем производные на концах интервала
            d_a = self._derivative(a)
            d_b = self._derivative(b)

            # Проверка деления на ноль
            if abs(d_b - d_a) < 1e-12:
                raise ZeroDivisionError("Знаменатель формулы равен нулю")

            # Вычисляем новое приближение по методу хорд
            current_x = a - (d_a * (b - a)) / (d_b - d_a)

            # Проверка, что current_x находится внутри интервала [a, b]
            if current_x < a or current_x > b:
                # Если current_x выходит за пределы интервала, ограничиваем его
                current_x = np.clip(current_x, a, b)

            # Проверка условия останова |x_k - x_{k-1}| < eps
            if prev_x is not None and abs(current_x - prev_x) < self.eps:
                break

            # Вычисляем производную в новой точке
            d_current = self._derivative(current_x)

            # Проверка условия завершения (производная близка к нулю)
            if abs(d_current) < self.eps:
                break

            # Обновление границ интервала согласно алгоритму
            if d_current * d_b > 0:
                b = current_x
            else:
                a = current_x

            prev_x = current_x

        if iteration >= self.max_iter:
            raise RuntimeError(f"Метод не сошелся за {self.max_iter} итераций.")

        return current_x, iteration