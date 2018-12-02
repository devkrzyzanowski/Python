import matplotlib.pyplot as plt
import pylab as p
import numpy as np

f1x = p.arange(-5, 5)
f1y = 1.1*f1x

f2x = p.arange(-2, 3, 0.1)
f2y = f2x**2

f3x = p.arange(-3, 2, 0.1)
f3y = 2**f3x

plt.plot(f1x, f1y, label="funkcja liniowa")
plt.plot(f2x, f2y, label="funkcja kwadratowa")
plt.plot(f3x, f3y, label="funkcja wykladnicza")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Funkcje")
plt.legend(loc="upper left")
plt.grid(True)
ax = plt.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

plt.show()

