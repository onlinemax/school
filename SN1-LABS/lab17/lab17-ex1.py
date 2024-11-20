import matplotlib.pyplot as plt;
import statistics as st;

x = [0, 1, 2, 3, 4, 5]
y = [3.1738, 4.1605, 6.0860, 7.6511, 8.9429, 11.6408]
mean = st.mean(y)
std_dev = st.stdev(y)

m, b = st.linear_regression(x, y)


line_x = [min(x), max(x)]
line_y = [m * min(x) + b, m * max(x) + b]


plt.plot(line_x, line_y, c="red")
plt.scatter(x, y)
plt.xlabel("time (s)")
plt.ylabel("x (m)")
plt.suptitle("Fotchin 2431325")
plt.text(0, 11, f'm: {m:.4f} b: {b:.4f}')
plt.show()
