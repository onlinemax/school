from math import factorial, pi
import numpy as np
import matplotlib.pyplot as plt
def T(x, m):
    accum = 0
    for k in range(m + 1):
        accum += x ** k / factorial(k)
    return accum

T_m = np.vectorize(T)
x = np.linspace(-pi, pi, 100)
y = np.exp(x)
a = T_m(np.tile(x, (6, 1)), np.mgrid[0:6, 0:100][0])

plt.plot(x, y)

for v in a:
    plt.plot(x, v)
plt.legend(["exp(x)", "T_0(x)", "T_1(x)","T_2(x)", "T_3(x)", "T_4(x)", "T_5(x)"])
plt.show()
