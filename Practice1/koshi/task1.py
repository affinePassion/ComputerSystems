from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def func1(y, t):
    return y**2 - y*t

def func2(y, t):
    return y**2 + 1

y0 = 0.1
ti = np.arange(0, 1.1, 0.1)
yi_1 = odeint(func1, y0, ti)
yi_2 = odeint(func2, y0, ti)
print("Значения функции 1:")
print(yi_1)
print("Значения функции 2:")
print(yi_2)

# График первой функции
plt.plot(ti, yi_1, "o-r", alpha = 0.7, lw = 5, mec = "g", mew = 2, ms = 10)
plt.xlabel("t, время", fontsize = 20)
plt.ylabel("y", fontsize = 20)
plt.tick_params(axis="both", labelsize = 15)
plt.grid(True)
plt.savefig("Fig1.png")
plt.show()

# График второй функции
plt.plot(ti, yi_2, "o-r", alpha = 0.7, lw = 5, mec = "g", mew = 2, ms = 10)
plt.xlabel("t, время", fontsize = 20)
plt.ylabel("y", fontsize = 20)
plt.tick_params(axis="both", labelsize = 15)
plt.grid(True)
plt.savefig("Fig2.png")
plt.show()