import numpy as np

class KMeans:
    def __init__(self, n_clusters=8, max_iters=300):
        self.n_clusters = n_clusters  # 聚类的簇数
        self.max_iters = max_iters  # 最大迭代次数

    def fit(self, data):
        self.cluster_centers_ = data[np.random.choice(len(data), self.n_clusters, replace=False)]  # 随机初始化聚类中心
        
        for _ in range(self.max_iters):
            # 将每个数据点分配到最近的聚类中心
            labels = np.argmin(np.linalg.norm(data[:, np.newaxis] - self.cluster_centers_, axis=2), axis=1)
            
            # 根据分配给每个簇的数据点的均值更新聚类中心
            new_centroids = np.array([data[labels == k].mean(axis=0) for k in range(self.n_clusters)])
            
            # 检查是否收敛
            if np.all(new_centroids == self.cluster_centers_):
                break
            
            self.cluster_centers_ = new_centroids

        self.labels_ = labels

if __name__ == "__main__":
    pass
