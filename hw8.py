# %% [markdown]
# # hw8

# %% [markdown]
# 1. 使用housing_renamed.csv中的数据构建3个不同的线性回归模型：因变量为value_per_sq_ft,
# 自变量请自己选择(并不要求使用变量选择方法，自行选择即可)。

# %% cell 1
import numpy as np
import pandas as pd
from sklearn import linear_model
import statsmodels.formula.api as smf

# %% cell 2
house = pd.read_csv("housing_renamed.csv")
house
##%% cell 3

# %%
lf = linear_model.LinearRegression()
unit_model = lf.fit(X=house[["units"]], y=house["value_per_sq_ft"])
unit_model.coef_
# %%
unit_model.intercept_
# %%
income_model = lf.fit(X=house[["income"]], y=house["value_per_sq_ft"])
income_model.coef_
# %%
income_model.intercept_
# %%
sq_ft_model = lf.fit(X=house[["sq_ft"]], y=house["value_per_sq_ft"])
sq_ft_model.coef_
# %%
sq_ft_model.intercept_
# %% [markdown]
# 2. 使用iris.csv数据进行聚类分析：不用variety列，使用前四列数据进行Kmeans聚类分析(k=3)，
# 并使用pca降维后作图显示聚类结果，然后与variety进行比较。

# %%
df = pd.read_csv("iris.csv")
iris = df.drop("variety", axis=1)
iris.head()
# %%
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

iris_kmenans = KMeans(n_clusters=3)
iris_kmenans.fit(iris)
labels = iris_kmenans.labels_
# %%
pca = PCA(n_components=2)
iris_pca = pca.fit_transform(iris)
print(len(iris_pca[:, 0]), "\n", len(iris_pca[:, 1]))
# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.scatter(
    x=iris_pca[:, 0],
    y=iris_pca[:, 1],
    c=labels,
    cmap="viridis",
    alpha=0.8,
    label="kmeans clusterd data",
)
# %%
variety_mapping = {"Setosa": 0, "Versicolor": 1, "Virginica": 2}
variety_labels = df["variety"].map(variety_mapping)
plt.figure(figsize=(8, 6))

plt.scatter(
    x=iris_pca[:, 0],
    y=iris_pca[:, 1],
    c=variety_labels,
    cmap="viridis",
    alpha=0.8,
    label="kmeans clusterd data",
)
# %% [markdown]
# 3. 参考statistical simulation中的Monte Carlo Integration，模拟计算PI的值。


# %%
total = 10**6
x = np.random.rand(total)
y = np.random.rand(total)
inside=x**2+y**2<=1
rate=np.sum(inside)/total
pi_estimater=4*rate
pi_estimater

# %%
plt.figure(figsize=(6,6))
plt.scatter(x[inside], y[inside], s=1, color='blue', label='Inside Circle')
plt.scatter(x[~inside], y[~inside], s=1, color='red', label='Outside Circle')
plt.title(f'Monte Carlo π Estimate: {pi_estimater:.5f}')
plt.legend()
plt.axis('equal')
plt.show()

# %%
