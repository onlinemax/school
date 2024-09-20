import matplotlib.pyplot as plt
import numpy as np
def linearFunction(domain: list, f: callable, N: int): 
    y = [0] * N
    for i in range(N):
        y[i] = f(domain[0] + (domain[1] - domain[0]) * i / N)
    return y
N = 50
f = lambda x: x ** 2
fp = lambda x: 2 * x
a = 2
x = np.linspace(-5, 5, N)
y = linearFunction([-5, 5], f, N)
z = linearFunction([-5, 5], lambda x: fp(a) * (x - a) + f(a), N)
d = linearFunction([-5, 5], lambda x: (-1 / fp(a)) * (x - a) + f(a), N)
fig, ax, = plt.subplots()
print(len(x))
print(len(y))
print(len(z))
print(len(d))
ax.plot(x, y)
ax.set_ylim(0, 10)
ax.plot(x, z)
ax.plot(x, d)
plt.show()