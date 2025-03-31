import numpy as np

class BetaGenerator:
    def __init__(self, size=1, alpha=1.0, beta_param=1.0):
        self.size = size
        self.alpha = alpha
        self.beta_param = beta_param
        
    def generate(self):
        # Генерация случайных чисел из бета-распределения
        return np.random.beta(self.alpha, self.beta_param, self.size)