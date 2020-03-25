import numpy as np

a = np.array([230, 10, 284, 39, 76])

while np.any(a < 100):
    a[a < 100] *= 2
    print(a)
