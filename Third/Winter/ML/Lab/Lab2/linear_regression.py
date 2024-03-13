# linear_regression.py

import numpy as np

class LinearRegression:
    def __init__(self):
        self.w = None
        self.b = None

    def fit(self, X, y):
        # 添加偏差列
        X_b = np.c_[np.ones((X.shape[0], 1)), X]

        # 使用最小二乘法计算权重
        self.w = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

        # 提取偏差项
        self.b = self.w[0]
        self.w = self.w[1:]

    def predict(self, X):
        # 添加偏差列
        X_b = np.c_[np.ones((X.shape[0], 1)), X]

        # 预测
        y_pred = X_b.dot(np.insert(self.w, 0, self.b))

        return y_pred

    def score(self, X, y):
        y_pred = self.predict(X)

        # 使用均方误差（MSE）作为评估指标
        mse = np.mean((y_pred - y) ** 2)

        # 返回评估分数
        return 1 - mse / np.var(y)
