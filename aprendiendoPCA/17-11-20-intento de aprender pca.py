from matplotlib import pyplot as plt
import numpy as np

plt.rc('font', size=18)
plt.style.use('bmh')
# plt.xkcd(scale=2)

cell1 = np.array([3, 2.9, 2.2, 2, 1.3, 1.5, 1.1, 1, 0.4])
cell2 = np.array([0.25, 0.8, 1, 1.4, 1.6, 2, 2.2, 2.7, 3])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.scatter(cell1, cell2,
           marker='o',
           s=60,
           linewidth=2,
           facecolors='none',
           edgecolors='blue',
           label='genes')

ax.set_title('Comparación entre dos células')
ax.set_xlabel('Célula 1')
ax.set_ylabel('Célula 2')
ax.legend(loc='upper right')
ax.grid(True)

plt.show()

mat_cov = np.cov(cell1, cell2)
# print(mat_cov)

vec1 = np.array([1, 2])
vec2 = np.array([2, 4])


print(f'Desvío estándar: {np.std(vec1)}')
print(f'Varianza: {np.var(vec1)}')

X = np.stack((vec1, vec2), axis=0)
# print(X)
print(np.cov(X))
