import pandas as pd
import numpy as np

def gaussian_pdf(x , mean , std):
    """
    正态分布概率密度函数

    $$\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}$$
    """
    prob_density = (1/std*np.sqrt(2*np.pi)) * np.exp(-((x - mean) ** 2) / (2 * std ** 2))
    return prob_density

# 以身高为特征的Bayes分类器
def bayes_classifier_by(train_data, test_data, feature='身高(cm)', target='性别', prior_prob_male=0.5):
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

class MyGaussianNB:
    def __init__(self):
        self.class_probs = {}  # 类别概率
        self.class_params = {}  # 每个类别的均值和方差

    def fit(self, X, y):
        # 计算每个类别的先验概率
        unique_classes, class_counts = np.unique(y, return_counts=True)
        total_samples = len(y)
        self.class_probs = dict(zip(unique_classes, class_counts / total_samples))
        # 计算每个类别的均值和方差
        for cls in unique_classes:
            cls_data = X[y == cls]
            mean = np.mean(cls_data, axis=0)
            variance = np.var(cls_data, axis=0)
            self.class_params[cls] = {'mean': mean, 'variance': variance}

    def _calculate_probability(self, x, mean, variance):
        # 正态分布概率密度函数
        exponent = np.exp(-(x - mean) ** 2 / (2 * variance))
        return (1 / np.sqrt(2 * np.pi * variance)) * exponent

    def _calculate_class_probability(self, sample, cls):
        # 计算后验概率
        class_prob = np.log(self.class_probs[cls])
        for i, feature in enumerate(sample):
            mean = self.class_params[cls]['mean'][i]
            variance = self.class_params[cls]['variance'][i]
            class_prob += np.log(self._calculate_probability(feature, mean, variance))
        return class_prob

    def predict(self, X):
        predictions = []
        for sample in X:
            max_prob = None
            predicted_class = None
            for cls in self.class_probs:
                class_prob = self._calculate_class_probability(sample, cls)
                if max_prob is None or class_prob > max_prob:
                    max_prob = class_prob
                    predicted_class = cls
            predictions.append(predicted_class)
        return np.array(predictions)

# 使用示例
# my_nb_classifier = MyGaussianNB()
# my_nb_classifier.fit(X_train.to_numpy(), y_train.to_numpy())
# y_pred_custom = my_nb_classifier.predict(X_test.to_numpy())
