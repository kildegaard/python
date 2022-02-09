import matplotlib.pyplot as plt
import numpy as np


# plt.style.use('seaborn')        # Con esto podés poner varios estilos
plt.style.use('ggplot')


# x = np.linspace(0, 2 * np.pi, 1000)
# y1 = np.sin(2 * np.pi * x)
# y2 = np.cos(6 * np.pi * x)

# plt.plot(x, y1)
# plt.plot(x, y2)


''' Copado para poder cambiar el estilo de un gráfico sin tener que modificar
    el estilo del resto de los gráficos!
'''

# with plt.style.context('dark_background'):
#     plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')
# plt.show()


''' Hacer subplots
'''

# ax1 = plt.axes()  # standard axes
# ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])

''' en .axes pasás un list de 4 elementos:
    plt.axes ([left, bottom, width, height])
'''

# fig = plt.figure()          # Crea una nueva figura

# ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4], xticklabels=[], ylim=(-1.2, 1.2))
# ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4], ylim=(-1.2, 1.2))

''' xticklabel=[] le quita los tics
    ylim (o xlim) te setea los límies de los ejes x e y
'''

# x = np.linspace(0, 10)
# ax1.plot(np.sin(x))
# ax2.plot(np.cos(x))

''' Para hacer subplots tipo matriz de gráficos se hace lo siguiente.
'''

# for i in range(1, 7):
#     plt.subplot(2, 3, i)
#     plt.text(0.5, 0.5, str((2, 3, i)),
#              fontsize=18, ha='center')


''' o lo que es lo mismo
'''

# x = np.linspace(0, 2 * np.pi, 1000)
# y = np.sin(x)

# fig = plt.figure()
# fig.subplots_adjust(hspace=0.4, wspace=0.4)     # Esto te marca la separación intergráfico
# for i in range(1, 7):
#     ax = fig.add_subplot(2, 3, i)
#     plt.plot(x, np.sin(i * x))
#     ax.text(3, 0, str((2, 3, i)),
#            fontsize=18, ha='center')


# x = np.linspace(0, 10*np.pi, 1000)
# # y0 = x ** -0.5
# # y1 = x ** -0.25
# # y2 = x **  0
# # y3 = x **  0.25
# # y4 = x **  0.5
# # y5 = x **  1
# y0 = np.sin(-0.5  * x)
# y1 = np.sin(-0.25 * x)
# y2 = np.sin( 0.0  * x)
# y3 = np.sin( 0.25 * x)
# y4 = np.sin( 0.5  * x)
# y5 = np.sin( 1.0  * x)

# plt.subplot(321)
# plt.plot(x, y0)
# plt.text(np.average(x), np.average(y0), str('Gráfico 1'), fontsize=18, ha='center', va='center')
# plt.ylim(-1, 1)

# plt.subplot(322)
# plt.plot(x, y1)
# plt.text(np.average(x), np.average(y1), str('Gráfico 2'), fontsize=18, ha='center', va='center')
# plt.ylim(-1, 1)

# plt.subplot(323)
# plt.plot(x, y2)
# plt.text(np.average(x), np.average(y2), str('Gráfico 3'), fontsize=18, ha='center', va='center')
# plt.ylim(-1, 1)

# plt.subplot(324)
# plt.plot(x, y3)
# plt.text(np.average(x), np.average(y3), str('Gráfico 4'), fontsize=18, ha='center', va='center')
# plt.ylim(-1, 1)

# plt.subplot(325)
# plt.plot(x, y4)
# plt.text(np.average(x), np.average(y4), str('Gráfico 5'), fontsize=18, ha='center', va='center')
# plt.ylim(-1, 1)

# plt.subplot(326)
# plt.plot(x, y5)
# plt.text(np.average(x), np.average(y5), str('Gráfico 6'), fontsize=18, ha='center', va='center')
# plt.ylim(-1, 1)


# ************************* ESTE ESTÁ LINDO Y FÁCIL ************************

fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
# axes are in a two-dimensional array, indexed by [row, col]
for i in range(2):
    for j in range(3):
        ax[i, j].text(0.5, 0.5, str((i, j)),
                      fontsize=18, ha='center')
fig
x = np.linspace(0, 1, 100)
y = x ** 2

ax[0, 2].text(0, 0, 'hola')
ax[1, 2].plot(x, y)

ax[0, 1].set_ylim([0, 1])
ax[0, 1].plot(x, 2 * x)

ax[1, 1].set_ylim([0, 1])
ax[1, 1].plot(x, 0.5 * x)

plt.show()
