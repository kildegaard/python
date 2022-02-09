# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:57:55 2020

Autor: Gustavo Kildegaard (gustavo.kildegaard@gmail.com)
"""

#%%

from matplotlib import pyplot as plt
import numpy as np

#%%

'''
Vamos a ver modificaciones a los gráficos para que queden como uno quiere
'''

# X1 y X2 hacen lo mismo, solo lo pongo para poder recordarlo

# Acá defino algunas cositas para graficar
X1 = np.arange(1, 101, 1)
X2 = np.linspace(1, 100, 100)
Y1 = [2*(x**2) -3*x + 1 for x in X1]
Y2 = [3*(x**(0.5))+x**2 - 5 for x in X1]

# Puedo definir el tamaño de la figura de antemano, está en pulgadas
fig, ax = plt.subplots(1, 2, figsize=(7, 5), sharey = False)

ax[0].scatter(X1, 200*X1,
           marker = '*',
           s = 15,
           color = 'black',
           label = 'Recta')

ax[0].plot(X1, Y2,
        linestyle = '--',
        label='Raíz')

ax[0].plot(X1, Y1,
        marker = 'o',
        markerfacecolor='green',
        markersize = 3,
        linewidth = 0.5,
        label = 'Cuadrática')


ax[0].set_title('Gráfico de funciones')
ax[0].set_xlabel('X')
ax[0].set_ylabel('Y')

# ax.set_xlim((0, 100))
# ax.set_ylim((min(Y1), max(Y1)))

ax[0].grid(True)
ax[0].legend(loc = 'upper left')

# Puedo ajustar varios parámetros ""desde afuera"" de los métodos con el plt.rc

font = {'family' : 'DejaVu Sans',
        'weight' : 'regular',
        'size'   : 12}

plt.rc('font', **font)

# Ahora vamos por el otro

X3 = np.linspace(0, 20, 20)
ax[1].plot(X3, 2*X3,
           marker = 'o',
           markerfacecolor = 'Yellow',
           label = 'Recta')

ax[1].legend(loc = 'upper left')
ax[1].grid(True)

xticks = [0, 5, 10, 15, 20]
xticks_m = [2.5, 7.5, 12.5, 17.5]
xticklab = ['A', 'B', 'C', 'D']

yticks = [0, 10, 20, 30, 40]

ax[1].set_xticks(xticks)
ax[1].set_xticks(xticks_m, minor=True)
ax[1].set_xticklabels(xticklab, minor=True, fontsize=8)

ax[1].set_yticks(yticks)


#%%

# Empezamos otro en limpio para ver otras cosas

fig = plt.figure(figsize=(8, 6))

# Aca estamos creando los ejes a mano, lo cual puede ser conveniente
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.72, 0.72, 0.16, 0.16])


#%%

# Acá tenemos un ejemplo de ejes compartidos

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax2 = ax1.twinx()
t = np.linspace(0., 10., 100)
ax1.plot(t, t ** 2, 'b--')
ax2.plot(t, 1000 / (t + 1), 'r-')
ax1.set_ylabel('Density (cgs)', color='red')
ax2.set_ylabel('Temperature (K)', color='blue')
ax1.set_xlabel('Time (s)')


#%%

# Acá tengo la forma de poder modificar lo que quiera cuando quiera!

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
title = ax.set_title("My plot", fontsize='large')
points = ax.scatter([1,2,3], [4,5,6])

title.set_color('red')
title.set_text('Cambio el título')


#%%

# Para configurar toda la "estética" de una y no tener que andar preocupándose, se puede hacer uso del RC

plt.rc('xtick', color='r', labelsize='medium', direction='in')
plt.rc('xtick.major', size=6, pad=1)
plt.rc('xtick.minor', size=3, pad=4)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.rcdefaults()
#%%

# VAMOS A SEGMENTAR LAS COSAS AHORA POR TIPO DE OBJETO (EJE, TICKS, LO QUE SEA)

#%%

# ######### TICKS ##########


fig, ax = plt.subplots()

xtick = [0, 1, 2, 3, 4]
mxtick = [0.5, 3.5]

ytick = [0, 2, 4, 6, 8, 10]
ymtick = [1, 3, 5, 7, 9]

# Esto setea los xtick que yo quiera
ax.set_xticks(xtick)
ax.set_xticks(mxtick, minor=True)

ax.set_yticks(ytick)
ax.set_yticks(ymtick, minor=True)

# Esto pone los Ticks en la parte superior, puede ser top, bottom, both, default
ax.xaxis.set_ticks_position('both')

# Esto elije la dirección en la que van a estar los ticks, si para adentro, afuera o ambos
ax.xaxis.set_tick_params(direction = 'in', which = 'major', size = 8)

ax.xaxis.set_tick_params(direction = 'inout', which = 'minor', size = 5)


ax.yaxis.set_ticks_position('both')
ax.yaxis.set_tick_params(direction='in', size=8, which='major')
ax.yaxis.set_tick_params(direction='inout', size=5, which='minor')

# Y ahora podemos agregar labels

xlabel = ['Hola', 'Chau']
ax.set_xticklabels(xlabel, minor=True)