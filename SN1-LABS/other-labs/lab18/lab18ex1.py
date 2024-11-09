import pandas as pd


data = pd.read_csv("abalone.csv")
new_index = ["M","F", "I"]
fil = data.groupby("sex").agg(count=("sex", "count"), length=("length_mm", "mean"),height=("height_mm", "mean"),weight=("whole_weight_gm", "mean"), rings=("rings", "mean")).round(decimals=1).reindex(new_index).reset_index()
# [["length_mm","diameter_mm","height_mm","whole_weight_gm","rings"]].mean().round(decimals=1)
open("report.txt", mode="w").write(fil.to_string(index=False));
# pd.pivot_table(data, index="sex", columns=["count", "length", "height", "weight", "rings"], aggfunc=[]
