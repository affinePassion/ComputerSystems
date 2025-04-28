from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def func(eq, t, r1, l1, l2, b2):
    x,y = eq
    return [r1*x-l1*x*y, l2*x*y-b2*y]

def solution(r1 = 0.5, l1 = 0.01, l2 = 0.01, b2 = 0.2, x0 = 25, y0 = 5):
    ti = np.arange(0, 100, 0.1)
    n0 = [x0, y0]
    sol = odeint(func, n0, ti, args=(r1, l1, l2, b2))
    x = sol[:,0]
    y = sol[:,1]
    

    plt.subplot(121)
    plt.plot(ti,x,"red",label="x")
    plt.plot(ti,y,"blue",label="y")
    plt.xlabel("t",fontsize=17)
    plt.ylabel("x,y",fontsize=17)
    plt.grid()
    plt.legend()
    plt.title("a)")

    plt.subplot(122)
    plt.plot(x,y,color = "green")
    plt.xlabel("x",fontsize=17)
    plt.ylabel("y",fontsize=17)
    plt.grid()
    plt.title("b)")
    plt.tight_layout()
    plt.savefig("Fig3.png")
    plt.show()


if __name__ == "__main__":
    solution()