import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("penguins.csv")
filtered = data[["species", "bill_depth_mm", "bill_length_mm"]] 
group = filtered.groupby('species')
fig, ax = plt.subplots()
species = ["Adelie", "Gentoo", "Chinstrap"]
for specy in species:
    d = group.get_group(specy)
    ax.scatter(x=d["bill_depth_mm"], y=d["bill_length_mm"])
# filtered.plot.scatter(x="bill_depth_mm", y="bill_length_mm", c="species", cmap="viridis");
ax.legend(species, loc="upper left")
ax.set_xlabel("Bill depth, mm")
ax.set_ylabel("Bill length, mm")
plt.show()
