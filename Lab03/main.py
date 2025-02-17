import math
import sys
from methods import DichotomySearch
import numpy as np  # Используем numpy для более точных значений
import matplotlib.pyplot as plt  # Импортируем matplotlib
from myForm.myForm import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

class Error_Handler:
    @staticmethod
    def show_error_message(message):
        msg = QMessageBox()
        msg.setInformativeText(message)
        msg.setWindowTitle("Ошибка")
        msg.exec_()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.foundResult.clicked.connect(lambda: self.dichotomy_search())
        self.ui.graphButton.clicked.connect(lambda: self.plot_graph())
        self.ui.graphButton_3.clicked.connect(lambda: self.plot_graph())

    def dichotomy_search(self):   
        try:
            # Получаем начальные и конечные значения, а также точность из текстовых полей
            start = float(self.ui.start.text())
            end = float(self.ui.end.text())
            accuracy = float(self.ui.epsilon.text())

            # Проверяем, чтобы начальное и конечное значения были в диапазоне от -5 до 5
            if not (-10 <= start <= 5 and -5 <= end <= 10):
                Error_Handler.show_error_message("Начальное и конечное значения должны быть в диапазоне от -5 до 5.")
                return
            
            # Проверяем, что начальное значение меньше конечного
            if start >= end:
                Error_Handler.show_error_message("Начальное значение должно быть меньше конечного.")
                return
            
            # Проверяем точность
            if not (0.00000001 <= accuracy <= 0.1):
                Error_Handler.show_error_message("Точность должна быть в пределах от 10^-7 до 10^-1.")
                return

            # Пример работы с методом золотого сечения
            d = DichotomySearch(self.funnc, start, end, accuracy)
            min_value = d.search(False)  # Находим минимум
            max_value = d.search(True)  # Находим максимум
            self.ui.extremus.setPlainText(f"Метод дихотомии:\nМинимум: {min_value} \nМаксимум: {max_value}")

        except ValueError as e:
            # В случае ошибки выводим сообщение в текстовое поле
            Error_Handler.show_error_message(f"Ошибка: {e}")
        except Exception as e:
            # Общий обработчик ошибок
            Error_Handler.show_error_message(f"Произошла ошибка: {str(e)}")

    def golden_search(self):     
        return 0 

    def plot_graph(self):
        # Создаем массив значений x с использованием numpy.linspace для равномерного распределения точек
        x_vals = np.linspace(-5, 5, 1000)  # 1000 точек для высокой точности
        y_vals = self.funnc(x_vals)

        # Построение графика с использованием matplotlib
        plt.plot(x_vals, y_vals, label="funnc(x) = x^5 * sin(5x)", linewidth=2)
        plt.title("График функции f(x) = x^5 * sin(5x)")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()
        plt.show()  # Отображаем график

    def funnc(self, x):
        return np.power(x, 5) * np.sin(5 * x)  # Используем numpy для более точных вычислений

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())