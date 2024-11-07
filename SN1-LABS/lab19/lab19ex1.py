import matplotlib.pyplot as plt
from math import factorial, pi, sin
def T(x, m):
    accum = 0
    negate = False
    for k in range(m + 1):
        accum += x ** (2 * k + 1) / factorial(2 * k + 1) * (-1 if negate else 1)
        negate = not negate
    return accum
x = [0.] * 100
for i in range(100):
    x[i] = -2 * pi + i * 4 * pi / 99
# Checking that they are equal but since it's a flowt. Checking the difference beetween the two values is really small.
assert(abs(x[99] - 2 * pi) < 1e-05)
assert(abs(x[0] - -2 * pi) < 1e-05)
y = [0.] * 100
a = [x.copy(), x.copy(), x.copy(), x.copy()]

for v in range(len(x)):
    y[v] = sin(x[v])
    for t in range(len(a)):
       a[t][v] = T(a[t][v], t)
plt.plot(x, y)
for yval in a:
    plt.plot(x, yval)
plt.ylim([-2, 2])
plt.suptitle("Taylor polymonial approximations of sine")
plt.legend(["sin(x)", "T_1(x)","T_3(x)", "T_5(x)", "T_7(x)"])
plt.show()
