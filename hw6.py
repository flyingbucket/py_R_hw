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
    if row.group == "a":
        A.append(row.value)
    elif row.group == "b":
        B.append(row.value)


def slide_avg(lst):
    res = []
    running_sum = 0  # 维护滑动窗口的和
    count = 0  # 维护窗口内非 NaN 值的数量

    for i in range(len(lst)):
        new_value = lst[i]

        if not pd.isna(new_value):
            running_sum += new_value
            count += 1

        if i >= 3:
            old_value = lst[i - 3]
            if not pd.isna(old_value):
                running_sum -= old_value
                count -= 1

        if count == 0:
            res.append(np.nan)  # 避免除以 0
        else:
            res.append(running_sum / count)

    return res


res_A = slide_avg(A)
res_B = slide_avg(B)

avg = []
for tag in df["group"]:
    if tag == "a":
        avg.append(res_A.pop(0))
    else:
        avg.append(res_B.pop(0))

df["avg"] = avg
print(df["avg"])

# %% [markdown]
#
# 3. 扫雷游戏。创建一个dataframe来模拟扫雷游戏：
# (1) 创建一个扫雷游戏，即创建一个dataframe，包含两列X和Y，例如5*4的扫雷游戏，这个dataframe分别记录5*4个格子的坐标，
# 这个dataframe为两列，20行，它的一部分如下：
#     x  y
# 0  0  0
# 1  0  1
# 2  0  2
# （2）增加一列，此列为格子是否为雷，如果是的话值为1，否则为0. （使用随机函数，每个位置为雷的概率为0.4）
# （3）再增加一列adjacent，此列记录当前格子相邻的格子的雷的数目，如果当前格子为雷，则值为NaN。
# （4）创建一个新的5行4列的dataframe，其中值为(3)中计算得到的雷的数目。
#

# %% cell 3
rows, cols = 5, 4
data = {"x": [], "y": []}
for i in range(rows):
    for j in range(cols):
        data["x"].append(i)
        data["y"].append(j)
df = pd.DataFrame(data)

df["mine"] = np.random.choice([0, 1], size=len(df), p=[0.6, 0.4])


def count_adjacent_mines(row, df):
    if row["mine"] == 1:
        return np.nan

    x, y = row["x"], row["y"]
    adjacent_positions = [
        (x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx, dy) != (0, 0)
    ]
    count = sum(
        df[(df["x"] == adj_x) & (df["y"] == adj_y)][
            "mine"
        ].sum()  # treat it like a dataframe not a matrics
        for adj_x, adj_y in adjacent_positions
    )
    return count


df["adjacent"] = df.apply(lambda row: count_adjacent_mines(row, df), axis=1)

grid = df.pivot(index="x", columns="y", values="adjacent")

print(df, "\n", grid)
