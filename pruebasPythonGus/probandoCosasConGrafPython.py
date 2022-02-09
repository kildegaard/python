import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-np.pi, np.pi, 0.01)

y = np.sin(x)

fig = plt.figure()

plt.title('Grafiquinho')
plt.xlabel('$ \int_0^1 \\frac{1}{1+e^{-x}} dx $')
plt.ylabel('y')


plt.plot(x, y)

plt.show()
