from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

def get_metrics(true_labels, predicted_labels, predicted_score):
    print("准确率为: {}".format(metrics.accuracy_score(true_labels, predicted_labels)))
    print("混淆矩阵为:\n{}".format(metrics.confusion_matrix(true_labels, predicted_labels)))
    print("分类报告为:\n{}".format(metrics.classification_report(true_labels, predicted_labels))) 
    label_mapping = {'男': 1, '女': 0}
    true_labels = np.vectorize(label_mapping.get)(true_labels)
    predicted_labels = np.vectorize(label_mapping.get)(predicted_labels)
    print("ROC曲线下面积为: {}".format(metrics.roc_auc_score(true_labels, predicted_score)))
    # 绘制ROC曲线
    fpr, tpr, thresholds = metrics.roc_curve(true_labels, predicted_score)
    plt.plot(fpr, tpr, label='ROC曲线')
    plt.plot([0, 1], [0, 1], linestyle='--', color='k', label='随机猜测')
    plt.xlabel('假正率')
    plt.ylabel('真正率')
    plt.title('ROC曲线')
    plt.legend()
    plt.show()
    print("-------------------------------------------------------------------------------")

    