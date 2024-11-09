from os import walk
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("abalone.csv")
ax = plt.subplot(2, 2, 1)
data.plot.scatter(x="length_mm", y="rings",ylabel="Number of growth rings", s=2.0, color="red", ax=ax)
ax = plt.subplot(2, 2, 2)
data.plot.scatter(x="diameter_mm", y="rings",ylabel="Number of growth rings", s=2.0, color="green", ax=ax)
ax = plt.subplot(2, 2, 3)
data.plot.scatter(x="height_mm", y="rings",ylabel="Number of growth rings", s=2.0, color="blue", ax=ax)
ax = plt.subplot(2, 2, 4)
data.plot.scatter(x="shell_weight_gm", y="rings",ylabel="Number of growth rings", s=2.0, color="violet", ax=ax)
plt.suptitle("Relationship beetween shell size and growth rings");
plt.tight_layout()
plt.show()
