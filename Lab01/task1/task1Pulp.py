from pulp import LpVariable, LpProblem, LpMinimize, value
import time

start = time.time()
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)
x4 = LpVariable("x4", lowBound=0)
problem = LpProblem('0', LpMinimize)
problem += 5*x1 + 6*x2 + 7*x3 + 4*x4, "Функция цели"
problem += x1 + x2 + 4*x4 >= 26, "1"
problem += 2*x1 + 3*x3 + 5*x4 >= 30, "2"
problem += x1 + 2*x2 + 4*x3 + 6*x4 >= 24, "3"
problem.solve()
print("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print("Минимальная стоимость:")
print(value(problem.objective))
stop = time.time()
print ("Время :")
print(stop - start)