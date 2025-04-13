import numpy as np
import scipy.special as sp


def mle_gamma_newton_raphson(X, tol=1e-6, max_iter=100):
    n = len(X)
    x_bar = np.mean(X)
    log_x_bar = np.mean(np.log(X))

    # 初始化 alpha 和 lambda
    alpha = 0.5 / (np.log(x_bar) - log_x_bar)  # 初始估计
    for _ in range(max_iter):
        psi_alpha = sp.psi(alpha)  # Digamma function
        psi_prime_alpha = sp.polygamma(1, alpha)  # Trigamma function

        # 更新 alpha
        step = (np.log(alpha) - psi_alpha - np.log(x_bar) + log_x_bar) / (
            1 / alpha - psi_prime_alpha
        )
        alpha_new = alpha - step

        if abs(alpha_new - alpha) < tol:
            break
        alpha = alpha_new

    lambda_ = alpha / x_bar  # 由得分方程得到 lambda
    return alpha, lambda_


def mle_gamma_fisher_scoring(X, tol=1e-6, max_iter=100):
    n = len(X)
    x_bar = np.mean(X)
    log_x_bar = np.mean(np.log(X))

    # 初始化 alpha
    alpha = 0.5 / (np.log(x_bar) - log_x_bar)
    for _ in range(max_iter):
        psi_alpha = sp.psi(alpha)
        psi_prime_alpha = sp.polygamma(1, alpha)

        # Fisher Scoring 更新
        step = (np.log(alpha) - psi_alpha - np.log(x_bar) + log_x_bar) / psi_prime_alpha
        alpha_new = alpha - step

        if abs(alpha_new - alpha) < tol:
            break
        alpha = alpha_new

    lambda_ = alpha / x_bar
    return alpha, lambda_


def estimate_lambda_given_alpha(X, alpha, method="newton"):
    x_bar = np.mean(X)
    if method == "newton":
        lambda_ = alpha / x_bar
    elif method == "fisher":
        lambda_ = alpha / x_bar
    return lambda_


# 生成 Gamma 样本并估计参数
np.random.seed(42)
true_alpha, true_lambda = 2.0, 3.0
X_sample = np.random.gamma(true_alpha, 1 / true_lambda, size=100)

alpha_nr, lambda_nr = mle_gamma_newton_raphson(X_sample)
alpha_fs, lambda_fs = mle_gamma_fisher_scoring(X_sample)

print("Newton-Raphson 估计:", alpha_nr, lambda_nr)
print("Fisher Scoring 估计:", alpha_fs, lambda_fs)

# (b) 运行 30 组不同的初始值
np.random.seed(42)
initial_alphas = np.random.uniform(0.5, 5.0, 30)
results_nr = []
results_fs = []

for alpha_init in initial_alphas:
    alpha_nr, lambda_nr = mle_gamma_newton_raphson(X_sample)
    alpha_fs, lambda_fs = mle_gamma_fisher_scoring(X_sample)
    results_nr.append((alpha_nr, lambda_nr))
    results_fs.append((alpha_fs, lambda_fs))

# 计算平均估计值和标准差
results_nr = np.array(results_nr)
results_fs = np.array(results_fs)

print(
    "Newton-Raphson 平均估计:",
    np.mean(results_nr, axis=0),
    "标准差:",
    np.std(results_nr, axis=0),
)
print(
    "Fisher Scoring 平均估计:",
    np.mean(results_fs, axis=0),
    "标准差:",
    np.std(results_fs, axis=0),
)

# (c) 设 alpha 已知, 估计 lambda
known_alpha = true_alpha
lambda_nr_given_alpha = estimate_lambda_given_alpha(
    X_sample, known_alpha, method="newton"
)
lambda_fs_given_alpha = estimate_lambda_given_alpha(
    X_sample, known_alpha, method="fisher"
)

print("已知 alpha, Newton-Raphson 估计 lambda:", lambda_nr_given_alpha)
print("已知 alpha, Fisher Scoring 估计 lambda:", lambda_fs_given_alpha)
