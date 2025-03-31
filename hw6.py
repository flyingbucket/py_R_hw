# %% [markdown]
# # hw6

# %% [markdown]
# 1. 如果有dataframe
# df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]}),
# 那么对于列X的每一个值，计算相对于离其最近的0的相对位置
# （如果前面没有0，则计算从头开始的位置），这样就会得到
# [1, 2, 0, 1, 2, 3, 4, 0, 1, 2]，我们可以把它作为df的新的列'Y'.
# 问题：让用户输入任意一列整数，构造新的dataframe，以此列整数为列X，
# 并按照上述方法计算新的列Y。

# %% cell 1
import pandas as pd
import numpy as np

X = np.random.randint(0, 100, 10)
print(X, type(X))
zero_position = []
for i, num in enumerate(X):
    if num == 0:
        zero_position.append(i)
Y = []
if len(zero_position) == 0:
    Y = [i + 1 for i in range(len(X))]
else:
    for i, num in enumerate(X):
        if i < zero_position[0]:
            Y.append(i + 1)
        else:
            distance = min([abs(i - po) for po in zero_position])
df = pd.DataFrame({"X": X, "Y": Y})
print(df)
breakpoint()

# %% [markdown]
# 2. 滑动平均：给定dataframe包含两列，一列为group，一列为value，
# 例如 df = pd.DataFrame({'group': list('aabbabbbabab'), 'value': [1, 2, 3, np.nan, 2, 3, np.nan, 1, 7, 3, np.nan, 8]})
# 请根据group的进行滑动平均，自己定义窗口尺寸，如遇到nan请忽略（注意不是作为0处理，是忽略）。
# 例如上边的例子结果应为（窗口长度为3）：
# 0     1.000000
# 1     1.500000
# 2     3.000000
# 3     3.000000
# 4     1.666667
# 5     3.000000
# 6     3.000000
# 7     2.000000
# 8     3.666667
# 9     2.000000
# 10    4.500000
# 11    4.000000

# %%  cell 2
df = pd.DataFrame(
    {
        "group": list("aabbabbbabab"),
        "value": [1, 2, 3, np.nan, 2, 3, np.nan, 1, 7, 3, np.nan, 8],
    }
)
A = []
B = []
for row in df.itertuples(index=True):
    if row.group == "a" and row.value != np.nan:
        A.append(row.value)
    else:
        B.append(row.value)
