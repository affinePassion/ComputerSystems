import math
import sys
from methods import DichotomySearch, ChordSearch
import numpy as np  
import matplotlib.pyplot as plt 
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
        self.ui.foundResult_3.clicked.connect(lambda: self.chord_search())
        self.ui.graphButton.clicked.connect(lambda: self.plot_graph())
        self.ui.graphButton_3.clicked.connect(lambda: self.plot_graph())
        

    def dichotomy_search(self):   
        try:
            # Начальные и конечные значения, а также точность из текстовых полей
            start = float(self.ui.start.text())
            end = float(self.ui.end.text())
            accuracy = float(self.ui.epsilon.text())

            # Начальное и конечное значения были в диапазоне от -5 до 5
            if not (-10 <= start <= 5 and -5 <= end <= 10):
                Error_Handler.show_error_message("Начальное и конечное значения должны быть в диапазоне от -5 до 5.")
                return
            
            # Начальное значение меньше конечного
            if start >= end:
                Error_Handler.show_error_message("Начальное значение должно быть меньше конечного.")
                return
            
            # Точность
            if not (0.00000001 <= accuracy <= 0.1):
                Error_Handler.show_error_message("Точность должна быть в пределах от 10^-7 до 10^-1.")
                return

            d = DichotomySearch(self.funnc, start, end, accuracy)
            min_value, iterations = d.search(False)  # Находим минимум
            max_value, iterations = d.search(True)  # Находим максимум
            self.ui.extremus.setPlainText(f"Метод дихотомии:\nМинимум: {min_value} \nМаксимум: {max_value}\nКол-во итераций: {iterations}")

        except ValueError as e:
            Error_Handler.show_error_message(f"Ошибка: {e}")
        except Exception as e:
            Error_Handler.show_error_message(f"Произошла ошибка: {str(e)}")

    def chord_search(self):     
        try:
            start = float(self.ui.start_3.text())
            end = float(self.ui.end_3.text())
            accuracy = float(self.ui.epsilon_3.text())

            # Начальное и конечное значения были в диапазоне от -5 до 5
            if not (-5 <= start <= 5 and -5 <= end <= 5):
                Error_Handler.show_error_message("Начальное и конечное значения должны быть в диапазоне от -5 до 5.")
                return
            
            # Начальное значение меньше конечного
            if start >= end:
                Error_Handler.show_error_message("Начальное значение должно быть меньше конечного.")
                return
            
            # Точность
            if not (0.00000001 <= accuracy <= 0.1):
                Error_Handler.show_error_message("Точность должна быть в пределах от 10^-7 до 10^-1.")
                return

            chord_search = ChordSearch(self.funnc, start, end, accuracy)
            root, iterations = chord_search.search()  # Находим экстремум
            self.ui.extremus_3.setPlainText(f"Метод хорд:\nЭкстремум: {root}\nКол-во итераций: {iterations}")

        except ValueError as e:
            Error_Handler.show_error_message(f"Ошибка: {e}")
        except Exception as e:
            Error_Handler.show_error_message(f"Произошла ошибка: {str(e)}") 

    def plot_graph(self):
        x_vals = np.linspace(-5, 5, 10000)
        y_vals = self.funnc(x_vals)

        plt.plot(x_vals, y_vals, label="funnc(x) = x^5 * sin(5x)", linewidth=2)
        plt.title("График функции f(x) = x^5 * sin(5x)")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()
        plt.show() 

    def funnc(self, x):
        return np.power(x, 5) * np.sin(5 * x)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())