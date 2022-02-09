import numpy as np
from matplotlib import pyplot as plt

ar1 = np.array([[0, 0, 0, 0], [2, 4, 8, 16]])
print(ar1)
print(ar1.shape)

plt.plot(ar1)
plt.show()

ar1 = ar1.sum(axis=1)
print(ar1)
print(ar1.shape)

plt.plot(ar1)
plt.show()
