import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()
# +
import pandas as pd
import numpy as np

# 生成角度数据，从 0 到 90 度，每次增加 10 度
angles = np.linspace(0, 90, 10)

# 计算对应的正弦和余弦值
sine_values = np.sin(np.radians(angles))
cosine_values = np.cos(np.radians(angles))

# 创建 DataFrame
df = pd.DataFrame({
    'Angle (degrees)': angles,
    'Sine': sine_values,
    'Cosine': cosine_values
})

df
# -

type(sine_values)
