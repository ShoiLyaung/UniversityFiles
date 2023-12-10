import numpy as np

class LinearRegression:
    def __init__(self, learning_rate=0.001, epochs=10000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.w = None
        self.b = None

    def fit(self, X, y):
        # 添加偏差列
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        # 初始化权重和偏差
        self.w = np.zeros(X_b.shape[1])
        self.b = 0
        m = len(y)  # 样本数

        # 梯度下降迭代
        for epoch in range(self.epochs):
            # 计算预测值
            y_pred = np.dot(X_b, self.w)
            # 计算误差
            error = y_pred - y
            # 计算梯度
            dw = (1/m) * np.dot(X_b.T, error)
            db = (1/m) * np.sum(error)
            # 更新权重和偏差
            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db
            # 打印每500次迭代的损失
            if epoch % 500 == 0:
                cost = (1/(2*m)) * np.sum(np.square(error))
                print(f'Epoch {epoch}, Cost: {cost}')

    def predict(self, X):
        # 添加偏差列
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        # 预测
        y_pred = np.dot(X_b, self.w) + self.b
        return y_pred
