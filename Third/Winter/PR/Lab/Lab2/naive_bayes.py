import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

def gaussian_pdf(x , mean , std):
    '''
    正态分布概率密度函数

    $$\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}$$

    :param x:       输入值
    :param mean:    均值
    :param std:     标准差
    :return:        概率密度
    '''
    prob_density = (1/std*np.sqrt(2*np.pi)) * np.exp(-((x - mean) ** 2) / (2 * std ** 2))
    return prob_density

def bayes_classifier_by(train_data, test_data, feature='身高(cm)', target='性别', prior_prob_male=0.5):
    '''
    单特征特征的Bayes分类器
    :param train_data:      训练集
    :param test_data:       测试集
    :param feature:         特征
    :param target:          目标
    :param prior_prob_male: 先验概率1（先验概率2=1-先验概率1）
    :return:                预测结果
    '''
    prior_prob_female= 1 - prior_prob_male
    # 提取训练集中男女身高的均值和标准差
    male_mean = train_data[train_data[target] == '男'][feature].mean()
    male_std = train_data[train_data[target] == '男'][feature].std()
    female_mean = train_data[train_data[target] == '女'][feature].mean()
    female_std = train_data[train_data[target] == '女'][feature].std()
    # 计算男女身高的概率密度函数
    male_pdf = gaussian_pdf(test_data[feature], male_mean, male_std)
    female_pdf = gaussian_pdf(test_data[feature], female_mean, female_std)
    # 计算后验概率
    posterior_prob_male = prior_prob_male * male_pdf
    posterior_prob_female = prior_prob_female * female_pdf
    # 进行分类
    predictions = np.where(posterior_prob_male > posterior_prob_female, '男', '女')
    # for male_prob, female_prob, prediction in zip(posterior_prob_male, posterior_prob_female, predictions):
    #     print("男性后验概率为{:.6f}，女性后验概率为{:.6f}，故预测结果为'{}'".format(male_prob, female_prob, prediction))
    return predictions

def bayes_classifier_by_with_prob(train_data, test_data, feature='身高(cm)', target='性别', prior_prob_male=0.5):
    '''
    单特征特征的Bayes分类器
    :param train_data:      训练集
    :param test_data:       测试集
    :param feature:         特征
    :param target:          目标
    :param prior_prob_male: 先验概率1（先验概率2=1-先验概率1）
    :return:                分数
    '''
    prior_prob_female= 1 - prior_prob_male
    # 提取训练集中男女身高的均值和标准差
    male_mean = train_data[train_data[target] == '男'][feature].mean()
    male_std = train_data[train_data[target] == '男'][feature].std()
    female_mean = train_data[train_data[target] == '女'][feature].mean()
    female_std = train_data[train_data[target] == '女'][feature].std()
    # 计算男女身高的概率密度函数
    male_pdf = gaussian_pdf(test_data[feature], male_mean, male_std)
    female_pdf = gaussian_pdf(test_data[feature], female_mean, female_std)
    # 计算后验概率
    posterior_prob_male = prior_prob_male * male_pdf
    posterior_prob_female = prior_prob_female * female_pdf
    # 返回男性的后验概率
    return posterior_prob_male

class MyGaussianNB:
    '''
    多特征高斯朴素贝叶斯分类器，假设特征间相互独立
    '''
    def fit(self, X, y, prior_probs=None):
        '''
        训练
        :param X:               训练集特征
        :param y:               训练集标签
        :param prior_probs:     先验概率
        :return:                None
        '''
        self.classes, class_counts = np.unique(y, return_counts=True)
        if prior_probs is not None:
            prior_probs = {'男': prior_probs, '女': 1 - prior_probs}
        else:
            prior_probs = dict(zip(self.classes, class_counts / len(y)))
        self.class_probs = np.array([prior_probs[class_label] for class_label in self.classes])
        self.means = {}
        self.stds = {}
        for class_label in self.classes:
            class_data = X[y == class_label]
            self.means[class_label] = np.mean(class_data, axis=0)
            self.stds[class_label] = np.std(class_data, axis=0)

    def predict(self, X):
        '''
        预测
        :param X:   测试集特征
        :return:    预测结果
        '''
        predictions = []
        for x in X:
            class_scores = []
            for i, class_label in enumerate(self.classes):
                prior_prob = np.log(self.class_probs[i])
                mean = self.means[class_label]
                std = self.stds[class_label]
                likelihood = np.sum(-0.5 * ((x - mean) / std) ** 2 - np.log(np.sqrt(2 * np.pi) * std))
                class_scores.append(prior_prob + likelihood)
            predictions.append(self.classes[np.argmax(class_scores)])   #最大错误率
        return np.array(predictions)
    
    def predict_proba(self, X):
        '''
        预测概率
        :param X:   测试集特征
        :return:    各类别的概率
        '''
        probas = []
        for x in X:
            class_probs = []
            for i in range(len(self.classes)):
                class_label = self.classes[i]
                prior_prob = np.log(self.class_probs[i])
                mean = self.means[class_label]
                std = self.stds[class_label]
                likelihood = np.sum(-0.5 * ((x - mean) / std) ** 2 - np.log(np.sqrt(2 * np.pi) * std))
                class_probs.append(np.exp(prior_prob + likelihood))
            class_probs /= np.sum(class_probs)  # Normalize to get probabilities
            probas.append(class_probs)
        return np.array(probas)

    def plot_decision_boundary(self, X, y):
        # Plot decision boundary:
        h = .02  # 步长
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
        Z = self.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.Paired_r, alpha=0.8)
        # Plot data points
        sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y, palette='Set1', edgecolor='k', s=100)
        # Adding axes annotations:
        plt.xlabel('身高')
        plt.ylabel('体重')
        plt.title('决策边界')
        plt.show()

    def plot_3d_gaussian_grid(self, X, y, grid_resolution=100):
        # Plot 3D Gaussian distributions with grid:
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        h = .02  # 步长
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, grid_resolution),
                             np.linspace(y_min, y_max, grid_resolution))
        for class_label in np.unique(y):
            class_data = X[y == class_label]
            mean = np.mean(class_data, axis=0)
            cov_matrix = np.cov(class_data.T)
            mvn = multivariate_normal(mean=mean, cov=cov_matrix)
            Z = mvn.pdf(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)
            ax.plot_surface(xx, yy, Z, alpha=0.3, cmap='viridis', edgecolor='k', linewidth=0.5)
        # Plot data points
        # scatter = ax.scatter(X[:, 0], X[:, 1], zs=0, c=y, cmap='Set1', edgecolor='k', s=100)
        # Adding axes annotations:
        ax.set_xlabel('Feature 1')
        ax.set_ylabel('Feature 2')
        ax.set_zlabel('Density')
        ax.set_title('3D Gaussian Distributions with Grid')
        # Add color bar
        # fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=10)
        plt.show()

# 定义Parzen窗法概率密度估计函数
def parzen_window_pdf(x, data, h):
    '''
    Parzen窗法概率密度估计函数

    \text{{kernel\_sum}} = \frac{1}{n} \sum_{i=1}^{n} \frac{e^{-\frac{(x - x_i)^2}{2h^2}}}{\sqrt{2\pi}h}
    
    :param x:       输入值
    :param data:    数据
    :param h:       窗宽
    :return:        概率密度
    '''
    n = len(data)
    prob_density = np.sum(np.exp(-(x - data) ** 2 / (2 * h ** 2)) / (np.sqrt(2 * np.pi) * h)) / n
    return prob_density

# 以身高为特征的Bayes分类器（Parzen窗法）
def bayes_classifier_parzen_height(train_data, test_data, h=5.0, prior_prob_male=0.5, prior_prob_female=0.5):
    '''
    以身高为特征的Bayes分类器（Parzen窗法）
    :param train_data:          训练集
    :param test_data:           测试集
    :param h:                   窗宽
    :return:                    预测结果
    '''
    predictions = []

    for index, test_point in test_data.iterrows():
        # 提取训练集中男女身高数据
        male_height_data = train_data[train_data['性别'] == '男']['身高(cm)']
        female_height_data = train_data[train_data['性别'] == '女']['身高(cm)']

        # 计算男女身高的概率密度函数
        male_height_pdf = parzen_window_pdf(test_point['身高(cm)'], male_height_data, h)
        female_height_pdf = parzen_window_pdf(test_point['身高(cm)'], female_height_data, h)

        # 计算后验概率
        posterior_prob_male = prior_prob_male * male_height_pdf
        posterior_prob_female = prior_prob_female * female_height_pdf

        # 进行分类
        prediction = '男' if posterior_prob_male > posterior_prob_female else '女'
        predictions.append(prediction)

    return predictions

# 以身高为特征的Bayes分类器（Parzen窗法）
def bayes_classifier_parzen_height_with_prob(train_data, test_data, h=5.0, prior_prob_male=0.5, prior_prob_female=0.5):
    '''
    以身高为特征的Bayes分类器（Parzen窗法）
    :param train_data:          训练集
    :param test_data:           测试集
    :param h:                   窗宽
    :return:                    后验概率
    '''
    posterior_prob_male_list = []
    posterior_prob_female_list = []
    for index, test_point in test_data.iterrows():
        # 提取训练集中男女身高数据
        male_height_data = train_data[train_data['性别'] == '男']['身高(cm)']
        female_height_data = train_data[train_data['性别'] == '女']['身高(cm)']
        # 计算男女身高的概率密度函数
        male_height_pdf = parzen_window_pdf(test_point['身高(cm)'], male_height_data, h)
        female_height_pdf = parzen_window_pdf(test_point['身高(cm)'], female_height_data, h)
        # 计算后验概率
        posterior_prob_male = prior_prob_male * male_height_pdf
        posterior_prob_female = prior_prob_female * female_height_pdf
        # 添加到列表中
        posterior_prob_male_list.append(posterior_prob_male)
        posterior_prob_female_list.append(posterior_prob_female)
    return posterior_prob_male_list, posterior_prob_female_list
