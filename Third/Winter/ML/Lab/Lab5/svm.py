import numpy as np

class SVM:
    def __init__(self, C=1.0, tol=0.01, max_passes=5):
        self.C = C  # regularization parameter
        self.tol = tol  # tolerance for numerical errors
        self.max_passes = max_passes  # maximum number of iterations without changing alpha values

        self.X = None
        self.y = None
        self.m = None
        self.n = None

        self.alpha = None
        self.b = 0
        self.E = None

    def fit(self, X, y):
        self.X = X
        self.y = y
        self.m, self.n = X.shape

        # Initialize alpha, b, and error cache
        self.alpha = np.zeros(self.m)
        self.b = 0
        self.E = np.zeros(self.m)

        passes = 0
        while passes < self.max_passes:
            num_changed_alphas = 0
            for i in range(self.m):
                E_i = self.decision_function(self.X[i]) - self.y[i]

                if ((self.y[i] * E_i < -self.tol and self.alpha[i] < self.C) or
                        (self.y[i] * E_i > self.tol and self.alpha[i] > 0)):
                    j = self.select_second_alpha(i)
                    E_j = self.decision_function(self.X[j]) - self.y[j]

                    alpha_i_old, alpha_j_old = self.alpha[i], self.alpha[j]

                    L, H = self.compute_L_H(self.alpha[i], self.alpha[j], self.y[i], self.y[j])

                    if L == H:
                        continue

                    eta = 2 * self.X[i].dot(self.X[j]) - self.X[i].dot(self.X[i]) - self.X[j].dot(self.X[j])

                    if eta >= 0:
                        continue

                    self.alpha[j] -= (self.y[j] * (E_i - E_j)) / eta
                    self.alpha[j] = min(H, max(L, self.alpha[j]))

                    if abs(self.alpha[j] - alpha_j_old) < 1e-5:
                        continue

                    self.alpha[i] += self.y[i] * self.y[j] * (alpha_j_old - self.alpha[j])

                    b1 = (self.b - E_i -
                          self.y[i] * (self.alpha[i] - alpha_i_old) * self.X[i].dot(self.X[i]) -
                          self.y[j] * (self.alpha[j] - alpha_j_old) * self.X[i].dot(self.X[j]))

                    b2 = (self.b - E_j -
                          self.y[i] * (self.alpha[i] - alpha_i_old) * self.X[i].dot(self.X[j]) -
                          self.y[j] * (self.alpha[j] - alpha_j_old) * self.X[j].dot(self.X[j]))

                    if 0 < self.alpha[i] < self.C:
                        self.b = b1
                    elif 0 < self.alpha[j] < self.C:
                        self.b = b2
                    else:
                        self.b = (b1 + b2) / 2

                    num_changed_alphas += 1

            if num_changed_alphas == 0:
                passes += 1
            else:
                passes = 0

    def decision_function(self, x):
        return np.dot(self.alpha * self.y, self.X.dot(x)) - self.b

    def predict(self, X):
        return np.sign(np.array([self.decision_function(x) for x in X]))

    def select_second_alpha(self, i):
        j = i
        while j == i:
            j = np.random.randint(self.m)
        return j

    def compute_L_H(self, alpha_i, alpha_j, y_i, y_j):
        if y_i != y_j:
            return max(0, alpha_j - alpha_i), min(self.C, self.C + alpha_j - alpha_i)
        else:
            return max(0, alpha_i + alpha_j - self.C), min(self.C, alpha_i + alpha_j)
