class LinearCongruentialGenerator:
    def __init__(self, k, a, b, x0):
        self.k = k
        self.a = a        # Множитель
        self.b = b        # Приращение
        self.m = 2**k    # Модуль (используем 2^k для эффективности)
        self.x = x0       # Начальное значение
        
        
    def next(self):
        # Генерируем следующее случайное число по линейному конгруэнтному методу
        self.x = (self.a * self.x + self.b) % self.m
        return self.x / self.m  # Нормализуем к [0, 1)