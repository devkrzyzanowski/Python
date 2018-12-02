import matplotlib.pyplot as plt
import pylab as p
import numpy as np
a = input("Podaj a = ")

f1x = p.arange(-10, 0, 0.5)
f1y = f1x /(-3) + int(a)

f2x = p.arange(0, 10, 0.5)
f2y = f2x*f2x/3



plt.plot(f1x, f1y, label="x/(-3)+a")
plt.plot(f2x, f2y, label="x^2/3")

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


