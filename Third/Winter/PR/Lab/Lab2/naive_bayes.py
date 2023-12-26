import pandas as pd
import numpy as np

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
    def fit(self, X, y):
        '''
        训练模型
        :param X:   训练集特征
        :param y:   训练集目标
        '''
        self.classes, class_counts = np.unique(y, return_counts=True)
        self.class_probs = class_counts / len(y)

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
                prior_prob = np.log(self.class_probs[i])  # Use the index 'i' for class_probs
                mean = self.means[class_label]
                std = self.stds[class_label]
                likelihood = np.sum(-0.5 * ((x - mean) / std) ** 2 - np.log(np.sqrt(2 * np.pi) * std))
                class_scores.append(prior_prob + likelihood)
            predictions.append(self.classes[np.argmax(class_scores)])
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
            for i in range(len(self.classes)):  # Iterate over indices
                class_label = self.classes[i]
                prior_prob = np.log(self.class_probs[i])  # Use the index 'i' for class_probs
                mean = self.means[class_label]
                std = self.stds[class_label]
                likelihood = np.sum(-0.5 * ((x - mean) / std) ** 2 - np.log(np.sqrt(2 * np.pi) * std))
                class_probs.append(np.exp(prior_prob + likelihood))
            class_probs /= np.sum(class_probs)  # Normalize to get probabilities
            probas.append(class_probs)
        return np.array(probas)
