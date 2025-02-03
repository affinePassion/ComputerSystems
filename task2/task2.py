import matplotlib.pyplot as plt # импортируем построитель графиков из библиотеки matplotlib
import numpy as np # импортируем библиотеку numpy для работы с массивами numpy
from sklearn.metrics import r2_score # функция для расчёта критерия r^2
from datetime import datetime
import matplotlib.dates as mdates


# Массивы входных данных
x = [
    '15.03.2023', '14.03.2023', '13.03.2023', '10.03.2023', '09.03.2023', '08.03.2023',
    '07.03.2023', '06.03.2023', '03.03.2023', '02.03.2023', '01.03.2023', '28.02.2023',
    '27.02.2023', '24.02.2023', '23.02.2023', '22.02.2023', '21.02.2023', '17.02.2023', 
    '16.02.2023', '15.02.2023'
]
y = [
    179.58, 183.26, 174.48, 173.44, 172.92, 182,
    187.71, 193.81, 197.79, 190.9, 202.77, 205.71,
    207.63, 196.88, 202.07, 200.86, 197.37, 208.31,
    202.04, 214.24
]

# Массивы numpy по входным данным
base_date = datetime.strptime(x[-1], '%d.%m.%Y')  # Используем последнюю дату как базовую
numpy_x = np.array([(datetime.strptime(date, '%d.%m.%Y') - base_date).days for date in x])
numpy_y = np.array(y)

# Линии тренда
# линейный (автоматическое создание)
set_line_by_data = np.polyfit(numpy_x, numpy_y, 1) # полином первой степени
linear_trend = np.poly1d(set_line_by_data) # снижение размерности до одномерного массива
print("{0}x + {1}".format(*set_line_by_data)) # формула

# полиномиальный
# set_polinom_by_data = np.polyfit(numpy_x, numpy_y, 6) # работа с полиномом 6 степени
# polinom_trend = np.poly1d(set_polinom_by_data) # Рассчитать значение полинома в точках x
# print("${0}x^6 + {1}x^5 + {2}x^4 + {3}x^3 + {4}x^2 + {5}x + {6}$".format(*set_polinom_by_data)) # формула
# set_polinom_by_data = np.polyfit(numpy_x, numpy_y, 6)

set_polinom_by_data = np.polyfit(numpy_x, numpy_y, 2) # работа с полиномом 2 степени
polinom_trend = np.poly1d(set_polinom_by_data) # Рассчитать значение полинома в точках x

polinom_title = "${0}x^2 + {1}x + {2}$".format(*set_polinom_by_data)
print("${0}x^2 + {1}x + {2}$".format(*set_polinom_by_data)) # формула

# логарифмический
log_x = np.log(numpy_x + 1)  # Добавляем 1, чтобы избежать log(0)
set_log_by_data = np.polyfit(log_x, numpy_y, 1)
log_trend = [set_log_by_data[0]*np.log(x + 1) + set_log_by_data[1] for x in numpy_x] # создание одномерного массива для логарифмического тренда
print("${0}ln(x) + {1}$".format(*set_log_by_data))  # формула

# экспоненциальный
set_exp_by_data = np.polyfit(numpy_x, np.log(numpy_y), 1) # работа с полиномом 1 степени + логарифмирование
exp_trend = [np.exp(set_exp_by_data[1]) * np.exp(set_exp_by_data[0] * x) for x in numpy_x] # создание одномерного массива для экспоненциального тренда
print("${1}e^{0}x$".format(*set_exp_by_data))  # формула

# Расчёт R^2
linear_r2 = r2_score(numpy_y, linear_trend(numpy_x))
polinom_r2 = r2_score(numpy_y, polinom_trend(numpy_x))
log_r2 = r2_score(numpy_y, log_trend)
exp_r2 = r2_score(numpy_y, exp_trend)


# Отображение графиков
plt.figure(figsize=(15, 15)) # размер графика


# 2 графика по горизонтали, 2 по вертикали
plt.subplot(2, 2, 1)

# !!! Текущая ячейка - 1 (левый верхний график)
plt.scatter(numpy_x, numpy_y, label = 'data') # точечный график по x_numpy, y_numpy
plt.plot(numpy_x, linear_trend(numpy_x), linestyle='dashed', color="orange", label = 'linear trend') # линейный тренд
plt.grid(color="gainsboro") # Сетка
plt.legend(loc='upper right', fontsize=12)
plt.title("Линейный \n$R^2=$" + str(linear_r2) + "\n{0}x + {1}".format(*set_line_by_data))

# !!! Текущая ячейка - 2
plt.subplot(2, 2, 2)
plt.scatter(numpy_x, numpy_y, label = 'data') # точечный график по x_numpy, y_numpy
x = np.linspace(numpy_x.min(), numpy_x.max()) # набор данных для x для большей гладкости графика (50 точек)
plt.plot(x, polinom_trend(x), linestyle='dashed', color="orange", label = 'polinomial trend') # полиномиальный тренд
plt.grid(color="gainsboro") # Сетка
plt.legend(loc = 'center left', fontsize=12, bbox_to_anchor=(1, 0.5))
plt.title("Полиномиальный \n$R^2=$" + str(polinom_r2) + polinom_title)

# !!! Текущая ячейка - 3
plt.subplot(2, 2, 3)
plt.scatter(numpy_x, numpy_y, label = 'data') # точечный график по x_numpy, y_numpy
plt.plot(numpy_x, log_trend, linestyle='dashed', color="orange", label = 'log trend') # логарифмический тренд
plt.grid(color="gainsboro") # Сетка
plt.legend(loc = 'upper right', fontsize=12)
plt.title("Логарифмический \n$R^2=$" + str(log_r2) + "\n${0}ln(x) + {1}$".format(*set_log_by_data))

# !!! Текущая ячейка - 4
plt.subplot(2, 2, 4)
plt.scatter(numpy_x, numpy_y, label = 'data') # точечный график по x_numpy, y_numpy
plt.plot(numpy_x, exp_trend, linestyle='dashed', color="orange", label = 'exp trend')
plt.grid(color="gainsboro") # Сетка
plt.legend(loc = 'center left', fontsize=12, bbox_to_anchor=(1, 0.5))
plt.title("Экспоненциальный \n$R^2=$" + str(exp_r2) + "\n{1}e^({0}x)".format(*set_exp_by_data))

fig = plt.gcf() # Взять текущую фигуру
fig.set_size_inches(15, 15) # Задать размеры графика

from datetime import timedelta

def format_func(value, tick_number):
    return (base_date + timedelta(days=int(value))).strftime('%d.%m')

for ax in fig.get_axes():
    ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')

plt.tight_layout(pad=4.0)  # Увеличим отступы между графиками
fig.subplots_adjust(bottom=0.1)  # Добавим место снизу для меток оси X

# Покажем окно с нарисованным графиком
plt.show()