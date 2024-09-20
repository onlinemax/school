# This is the framework for solving part 3 of the lab.
import matplotlib.pyplot as plt
from math import pi, sin, cos

N = 50                          # The desired list length
x = [0] * N                     # Create a list of N zeroes.
y = [0] * N                
z = [0] * N 
 # Another list of N zeroes.
i = 0
for i in range(N):
    x[i] = 2*pi*i/N             # x ranges from 0 to 2*pi 
    y[i] = sin(x[i])
    z[i] = cos(x[i])           # y is just x**2
    i = i + 1

plt.plot(x, y, color='orange')  # Creates the line
plt.plot(x, z, color="purple")
plt.title("Programming in Science - Lab 7") # Sets the title
plt.legend(["sin(x)", "cos(x)"])
plt.show()                                  # Actually displays the chart.
