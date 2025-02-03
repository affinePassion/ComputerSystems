from cvxopt.modeling import variable, op
import time

start = time.time()
x = variable(4, 'x')
z= (5*x[0] +6*x[1] + 7*x[2] + 4*x[3]) #Функция цели
mass1 = (1*x[0] + 1*x[1] + 0*x[2] + 4*x[3] >= 26) #"1"
mass2 = (2*x[0] + 0*x[1] + 3*x[2] + 5*x[3] >= 30 ) # "2"
mass3 = (1*x[0] + 2*x[1] + 4*x[2] + 6*x[3]  >= 24) #"3"
x_non_negative = (x >= 0) #"4"
problem = op(z,[mass1,mass2,mass3, x_non_negative])
problem.solve(solver='glpk')
problem.status

print ("Прибыль:")
print(abs(problem.objective.value()[0]))
print ("Результат:")
print(x.value)
stop = time.time()
print ("Время :")
print(stop - start)