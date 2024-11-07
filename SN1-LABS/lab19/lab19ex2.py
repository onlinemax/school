import numpy as np
import matplotlib.pyplot as plt
from math import factorial, pi

def T(x, m):
    accum = 0
    negate = False
    for k in range(m + 1):
        accum += x ** (2 * k + 1) / factorial(2 * k + 1) * (-1 if negate else 1)
        negate = not negate
    return accum
T_m = np.vectorize(T)
x = np.linspace(-2 * pi, 2 * pi, 100)
y = np.sin(x)
a = T_m(np.tile(x, (4, 1)), np.mgrid[0:4, 0:100][0] )

plt.plot(x, y)

for v in a:
    plt.plot(x, v)
plt.ylim([-2, 2])
plt.suptitle("Taylor polymonial approximations of sine")
plt.legend(["sin(x)", "T_1(x)","T_3(x)", "T_5(x)", "T_7(x)"])
plt.show()
