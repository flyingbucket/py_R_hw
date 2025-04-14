# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# # hw7

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 创建 DataFrame
df = pd.DataFrame(
    {
        "vals": np.random.RandomState(31).randint(-30, 30, size=15),
        "grps": np.random.RandomState(31).choice(["A", "B"], 15),
    }
)

# 分组均值
grouped_mean = df.groupby("grps")["vals"].mean()

# 新增 patched_vals 列
df["patched_vals"] = df.apply(
    lambda row: row["vals"] if row["vals"] >= 0 else grouped_mean[row["grps"]], axis=1
)

# 读取 iris 数据
iris = pd.read_csv("iris.csv")

# countplot
plt.figure(figsize=(6, 4))
sns.countplot(x="variety", data=iris, palette=["blue", "orange", "green"])
plt.title("Iris Variety Count")

# histplot
plt.figure(figsize=(6, 4))
iris.select_dtypes("number").mean().plot(
    kind="bar", color=["blue", "orange", "green", "red"]
)
plt.title("Mean of Numeric Columns")

# sepal.length KDE + hist
plt.figure(figsize=(6, 4))
sns.histplot(data=iris, x="sepal.length", kde=True)
plt.title("Histogram & KDE of Sepal Length")

# jointplot
joint_iris = sns.jointplot(
    data=iris,
    x="sepal.length",
    y="sepal.width",
    kind="reg",
    marginal_kws={"kde": True},
)

# boxplot of cols
iris_long = iris.copy().drop()
# 显示全部图像
plt.show()
