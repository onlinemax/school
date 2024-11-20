import matplotlib.pyplot as plt
import pandas as pd
import statistics as st


y_columns = ["y1", "y2", "y3", "y4"]
x_columns = ["x1", "x2", "x3", "x4"]
stats = [[], []]
plots = [];

df = pd.read_csv("anscombe.csv")

for i in range(len(y_columns)):
    y = y_columns[i]
    x = x_columns[i]
    stats[0].append(st.mean(df[y]))
    stats[1].append(st.stdev(df[y]))
    m, b = st.linear_regression(df[x].tolist(), df[y].tolist())
    plt.subplot(4, 1, i + 1)
    plt.scatter(df[x], df[y])
    plt.plot([min(df[x]), max(df[x])], [m * min(df[x]) + b, m * max(df[x]) + b], c="red")
    plt.xlabel(x)
    plt.yticks([0, 10])
    plt.ylim([0, max(df[y]) + 2])
    plt.ylabel(y)
    plt.text(min(df[x]), 8, f"m:{m:.2f} b:{b:.2f}")
print(f"{"":10s}{"y1":6s}{"y2":6s}{"y3":6}{"y4":6s}")
line = "";
line += f"{"mean":8}"
for mean in stats[0]:
    line += f"{mean:6.2f}"
print(line)
line = ""
line += f"{"std_dev":8s}"
for stdev in stats[1]:
    line += f"{stdev:6.2f}"
print(line)
plt.tight_layout()
plt.show()
