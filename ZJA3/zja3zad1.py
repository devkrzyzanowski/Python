import matplotlib.pyplot as plt
import pylab as p
import numpy as np
a =int(input("Podaj a = "))
b =int(input("Podaj b = "))

x = p.arange(-10, 10)
y = a * x + b


plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykres f(x) = a*x + b")
plt.legend(["funkcja liniowa"])
plt.grid(True)
ax = plt.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

plt.show()

