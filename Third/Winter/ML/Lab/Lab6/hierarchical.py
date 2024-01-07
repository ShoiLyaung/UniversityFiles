import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

class Hierarchical:
    def __init__(self, n_clusters=2, linkage='ward'):
        self.n_clusters = n_clusters
        self.linkage = linkage

    def fit_predict(self, data):
        linkage_matrix = sch.linkage(data, method=self.linkage)
        labels = sch.fcluster(linkage_matrix, t=self.n_clusters, criterion='maxclust')
        return labels

# 示例用法
if __name__ == "__main__":
    from sklearn.datasets import make_blobs

    # 生成一些随机数据
    data, _ = make_blobs(n_samples=300, centers=4, random_state=42)

    # 使用 Hierarchical 聚类算法
    my_hierarchical = Hierarchical(n_clusters=4)
    labels = my_hierarchical.fit_predict(data)

    # 绘制树状图
    dendrogram = sch.dendrogram(sch.linkage(data, method='ward'))
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('Sample Index')
    plt.ylabel('Cluster Distance')
    plt.show()
