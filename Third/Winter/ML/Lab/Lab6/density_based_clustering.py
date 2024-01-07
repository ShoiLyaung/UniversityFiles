import numpy as np

class DBSCAN:
    def __init__(self, eps=0.5, min_samples=5):
        self.eps = eps
        self.min_samples = min_samples

    def fit(self, data):
        self.data = data
        self.labels_ = np.full(len(data), -1)  # -1 represents noise
        self.cluster_label = 0

        for i, point in enumerate(data):
            if self.labels_[i] != -1:
                continue

            neighbors = self._region_query(point)

            if len(neighbors) < self.min_samples:
                self.labels_[i] = -1  # mark as noise
            else:
                self._expand_cluster(i, neighbors)

    def _region_query(self, point):
        return [j for j, other_point in enumerate(self.data) if np.linalg.norm(point - other_point) < self.eps]

    def _expand_cluster(self, current_point, neighbors):
        self.cluster_label += 1
        self.labels_[current_point] = self.cluster_label

        i = 0
        while i < len(neighbors):
            neighbor = neighbors[i]

            if self.labels_[neighbor] == -1:
                self.labels_[neighbor] = self.cluster_label

            elif self.labels_[neighbor] == 0:
                self.labels_[neighbor] = self.cluster_label

                new_neighbors = self._region_query(self.data[neighbor])

                if len(new_neighbors) >= self.min_samples:
                    neighbors.extend(new_neighbors)

            i += 1

# 示例用法
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from sklearn.datasets import make_moons

    # 生成一些随机数据
    data, _ = make_moons(n_samples=300, noise=0.05, random_state=42)

    # 使用自己实现的 DBSCAN 密度聚类算法
    dbscan = DBSCAN(eps=0.3, min_samples=5)
    dbscan.fit(data)
    labels = dbscan.labels_

    # 可视化结果
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', alpha=0.7, edgecolors='b')
    plt.title('DBSCAN Density-Based Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
