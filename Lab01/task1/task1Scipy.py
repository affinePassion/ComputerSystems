from scipy.optimize import linprog
import time
start = time.time()
c = [5, 6, 7, 4] #Функция цели
A_ub = [[-1, -1, 0, -4],
        [-2, 0, -3, -5],
        [-1, -2, -4, -6]]  #'1, 2, 3 левая часть'
b_ub = [-26, -30, -24] #'1, 2, 3 правая часть'
print (linprog(c, A_ub, b_ub))
stop = time.time()
print ("Время :")
print(stop - start)