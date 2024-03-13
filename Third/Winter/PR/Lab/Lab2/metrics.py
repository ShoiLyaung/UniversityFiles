import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

def accuracy_score(true_labels, predicted_labels):
    correct_predictions = np.sum(true_labels == predicted_labels)
    total_predictions = len(true_labels)
    accuracy = correct_predictions / total_predictions
    return accuracy

def confusion_matrix(true_labels, predicted_labels):
    pass

def classification_report(true_labels, predicted_labels):
    pass

def get_metrics(true_labels, predicted_labels, predicted_score):
    acc = accuracy_score(true_labels, predicted_labels)
    conf_matrix = metrics.confusion_matrix(true_labels, predicted_labels)
    cls_report = metrics.classification_report(true_labels, predicted_labels)
    # ROC
    label_mapping = {'男': 1, '女': 0}
    true_labels = np.vectorize(label_mapping.get)(true_labels)
    predicted_labels = np.vectorize(label_mapping.get)(predicted_labels)
    roc_auc_score = metrics.roc_auc_score(true_labels, predicted_score)
    fpr, tpr, thresholds = metrics.roc_curve(true_labels, predicted_score)
    
    print("准确率为: {}".format(acc))
    print("混淆矩阵为:\n{}".format(conf_matrix))
    print("分类报告为:\n{}".format(cls_report)) 
    print("ROC曲线下面积为: {}".format(roc_auc_score))
    print("-------------------------------------------------------------------------------")
    return fpr, tpr
    
def plot_roc_curves(metrics_list, labels_list):
    plt.figure(figsize=(4, 4))
    
    for i, metrics_data in enumerate(metrics_list):
        if metrics_data is not None:
            fpr, tpr = metrics_data
            label = labels_list[i]
            plt.plot(fpr, tpr, label=f'{label}')
        else:
            print(f"Metrics data for label {labels_list[i]} is None.")

    plt.plot([0, 1], [0, 1], linestyle='--', color='k', label='随机猜测')
    plt.xlabel('假正率')
    plt.ylabel('真正率')
    plt.title('多组数据ROC曲线对比')
    plt.legend()
    plt.show()

 
def get_metrics_accuracy(true_labels, predicted_labels, predicted_score):
    print("准确率为: {}".format(metrics.accuracy_score(true_labels, predicted_labels)))
    print("-------------------------------------------------------------------------------")
