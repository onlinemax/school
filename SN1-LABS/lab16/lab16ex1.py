import pandas as pd
data = pd.read_csv("penguins.csv")
print(data.pivot_table(index="species", columns="sex", values="body_mass_g", aggfunc="mean"))

