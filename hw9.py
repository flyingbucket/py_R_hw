# %% [markdown]
# # hw9
# 使用iris数据集进行神经网络练习：其中variety是标签，其他四个是输入特征。构建神经网络（架构不限）对variety
# 进行预测，输入为sepal.length，sepal.width，petal.length，petal.width四个变量。可对数据集分为训练集和测试集，
# 比较模型在训练集和测试集上的预测效果。

# %% cell 1
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# %% cell 2
iris = pd.read_csv("iris.csv")
iris.head()

# %% cell 3
X = iris[["sepal.length", "sepal.width", "petal.length", "petal.width"]].values
y = iris["variety"].values
y = LabelEncoder().fit_transform(y)

# %% cell 4
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.long)
y_test = torch.tensor(y_test, dtype=torch.long)


# %% cell 5
class IrisNN(nn.Module):
    def __init__(self) -> None:
        super(IrisNN, self).__init__()
        self.fc1 = nn.Linear(4, 10)
        self.fc2 = nn.Linear(10, 5)
        self.fc3 = nn.Linear(5, 3)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


# %% cell6
iris_model = IrisNN()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(iris_model.parameters(), lr=0.01)
num_epochs = 100

# %% cell 7
for epoch in range(num_epochs):
    iris_model.train()
    optimizer.zero_grad()
    outputs = iris_model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()
    if (epoch + 1) % 5 == 0:
        print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}")

# %% cell 8
with torch.no_grad():
    outputs_test = iris_model(X_test)
    _, predicted_test = torch.max(outputs_test, 1)
    accuracy_test = (predicted_test == y_test).sum().item() / y_test.size(0)
    print(f"Test Accuracy: {accuracy_test * 100:.2f}%")
