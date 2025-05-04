import numpy as np
import matplotlib.pyplot as plt

r = 0.2  
ρs = 10500  
ρг = 1260  
g = 9.81  
mu = 1480
k = 6 * np.pi * mu * r


V = (4/3) * np.pi * r**3
m = ρs * V

t_max = 1 
dt = 0.02  
time = np.arange(0, t_max, dt)


v = np.zeros_like(time)  
h = np.zeros_like(time)  


for i in range(1, len(time)):
    FА = ρг * V * g
    dv = (g - (k/m) * v[i-1] - FА / m) * dt
    v[i] = v[i-1] + dv
    h[i] = h[i-1] + v[i-1] * dt 

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(time, v)
plt.xlabel('Время (с)')
plt.ylabel('Скорость (м/с)')
plt.title('График изменения скорости')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(time, h)
plt.xlabel('Время (с)')
plt.ylabel('Высота (м)')
plt.title('График изменения высоты')
plt.grid()

plt.tight_layout()
plt.show()