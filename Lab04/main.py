from methods.linear import LinearCongruentialGenerator
from methods.beta_random import BetaGenerator
from scipy.optimize import newton
import numpy as np
import sys
import matplotlib.pyplot as plt  # Импортируем matplotlib
from form.myForm import Ui_MainWindow
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
        self.beta = []
        self.kong = []
        self.ui.generate_linear.clicked.connect(lambda: self.linear())
        self.ui.generate_beta.clicked.connect(lambda: self.beta_rand())
        self.ui.diagram_beta.clicked.connect(lambda: self.plot_graph(False))
        self.ui.diagram_linear.clicked.connect(lambda: self.plot_graph(True))

    def beta_rand(self):
        try:
            self.ui.generated_beta.clear()
            self.beta = []
            value = int(self.ui.count_beta.text())
            
            if not (1 <= value <= 10000):
                Error_Handler.show_error_message("Числа должны быть в пределах от 1 до 10000.")
                return
            beta_gen = BetaGenerator(value)  
            self.beta = beta_gen.generate()

            for i in range(min(20, len(self.beta))):
                self.ui.generated_beta.appendPlainText(f"{self.beta[i]:.6f}\n")
            
            if len(self.beta) > 20:
                self.ui.generated_beta.appendPlainText("...\n")
            
            less_than_0_5 = sum(1 for x in self.beta if x < 0.5)
            greater_than_0_5 = sum(1 for x in self.beta if x > 0.5)
            
            self.ui.generated_beta.appendPlainText(f"\nКоличество чисел меньше 0.5: {less_than_0_5}")
            self.ui.generated_beta.appendPlainText(f"Количество чисел больше 0.5: {greater_than_0_5}")

        except ValueError as e:
            # В случае ошибки выводим сообщение в текстовое поле
            Error_Handler.show_error_message(f"Ошибка: {e}")
        except Exception as e:
            # Общий обработчик ошибок
            Error_Handler.show_error_message(f"Произошла ошибка: {str(e)}")

    def linear(self):
        try:
            self.ui.generated_linear.clear()
            self.kong.clear()
            xi = int(self.ui.x.text())
            count = int(self.ui.count_linear.text())
            if not (1 <= xi <= 10000):
                Error_Handler.show_error_message("Число xi должно быть в пределах от 1 до 10000.")
                return

            generator = LinearCongruentialGenerator(k = 31, a = 16070093, b = 453816693, x0 = xi)
            
            for _ in range(min(20, count)):
                self.kong.append(generator.next())
                self.ui.generated_linear.appendPlainText(f"{self.kong[_]:.6f}\n")
            
            if count > 20:
                self.ui.generated_linear.appendPlainText("...\n")
                
                for _ in range(20, count):
                    self.kong.append(generator.next())

            less_than_0_5 = sum(1 for x in self.kong if x < 0.5)
            greater_than_0_5 = sum(1 for x in self.kong if x > 0.5)
            
            self.ui.generated_linear.appendPlainText(f"\nКоличество чисел меньше 0.5: {less_than_0_5}")
            self.ui.generated_linear.appendPlainText(f"Количество чисел больше 0.5: {greater_than_0_5}")

        except ValueError as e:
            # В случае ошибки выводим сообщение в текстовое поле
            Error_Handler.show_error_message(f"Ошибка: {e}")
        except Exception as e:
            # Общий обработчик ошибок
            Error_Handler.show_error_message(f"Произошла ошибка: {str(e)}")

    def plot_graph(self, flag):
        bins = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        
        if flag:
            counts, _ = np.histogram(self.kong, bins)
            label = 'Linear'
            color = 'skyblue'
        else:
            counts, _ = np.histogram(self.beta, bins)
            label = 'Beta'
            color = 'lightgreen'
        
        x = np.arange(len(bins) - 1)
        width = 0.8  
        
        fig, ax = plt.subplots(figsize=(10, 6)) 
        ax.bar(x, counts, width, label=label, color=color, edgecolor='black')

        ax.set_xlabel('Интервалы', fontsize=12)
        ax.set_ylabel('Количество чисел', fontsize=12)
        ax.set_title(f'Гистограмма для чисел из {label}', fontsize=16)
        
        ax.set_xticks(x)
        ax.set_xticklabels([f'{bins[i]:.1f} - {bins[i+1]:.1f}' for i in range(len(bins) - 1)], rotation=45)
        
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        ax.legend()

        plt.tight_layout()
        plt.show()

if __name__ == "__main__": 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())