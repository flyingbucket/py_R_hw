import numpy as np
from scipy.stats import skew, kurtosis

data = [150] * 4 + [160] * 8 + [170] * 6 + [180] * 2
data = np.array(data)
mean = np.mean(data)
var = np.var(data, ddof=1)
skewness = skew(data, bias=True)
kurt = kurtosis(data, bias=True)

print(mean, "\n", var, "\n", skewness, "\n", kurt, "\n")
print("all done!")
