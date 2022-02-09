# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 01:14:28 2020

Autor: Gustavo Kildegaard (gustavo.kildegaard@gmail.com)
"""
#%%     ## IMPORTS ##
from matplotlib import pyplot as plt
import numpy as np

#%%     ## Inicios ##

# Creamos algunos vectorcitos
X = [x for x in range(-100, 101)]
Y1 = [x**3 for x in X]
Y2 = [(x**3 + 2 * x**2) for x in X]

"""
Primero definimos la figura (fig) que sería el marco donde vamos a meter n cantidad de gráficos (axes)

Se usa el método .subplots(# de filas, # de columnas)
De esta forma, queda definido una "grilla" de ejes en donde vamos a poder graficar; para ese, hay que
aclarar en qué gráfico se quiere operar usando notación matricial
"""

fig, ax = plt.subplots(1, 2, sharey=True)

fig.suptitle('Varios Axes en una sola Figure')

ax[0].set_xlabel('Valores de X')
ax[0].set_ylabel('Valores de Y')
ax[0].set_xlim((-150, 150))
ax[0].grid(True)

ax[0].plot(X, Y1)

ax[1].set_xlabel('Valores de X')
ax[1].grid(True)

ax[1].plot(X, Y2)

# %%

'''
Hay dos formas de hacer las cosas en Matplotlib, la forma tipo POO y la forma tipo "pyplot-style"
'''

# %%

'''
POO Style
'''

x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.


# %%

'''
Pyplot Style
'''

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

# %%

'''
Como uno tiende a usar frecuentemente un mismo tipo de gráfico, lo cómodo es armar una función con todos los parámetros
y ya.
Por ejemplo:
'''


def graficar(graf, ax, data1, data2, parametros=None):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    parametros : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    if graf == 'plot':
        if parametros:
            out = ax.plot(data1, data2, **parametros)
        else:
            out = ax.plot(data1, data2)
    elif graf == 'scat':
        if parametros:
            out = ax.scatter(data1, data2, **parametros)
        else:
            out = ax.scatter(data1, data2)
    return out

# %%


'''
Esto anterior lo usamos así!
'''

data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
graficar(ax, data1, data2, {'marker': 'x'})

# %%
import matplotlib.pyplot as plt
plt.ion()
# O por ejemplo:

np.random.seed(1337)

X = np.linspace(-100, 100, 100)
Err = np.random.normal(loc=0, scale=5, size=100)
Y = [2 * x + 1 + er for x, er in zip(X, Err)]

fig, ax = plt.subplots(1, 1)

graficar('scat', ax, X, Y, {'marker': 'x', 's': 20})


# %%


# %%

'''
Esto es una boludez que estaba probando

Podés primero crear la figura con plt.figure() y dp añadirle axes con add_subplot

O podés hacer todo junto con el fig, ax = plt.subplots

'''

fig = plt.figure()

fig.suptitle('Figura vacia')

ax = fig.add_subplot(1, 1, 1)
ax.set_title('Un subplot')

ax2 = fig.add_subplot(2, 2, 4)
ax2.set_title('qué onda')
frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])

X = np.linspace(-100, 100, 100)
Err = np.random.normal(loc=0, scale=5, size=100)
Y = [2 * x + 1 + er for x, er in zip(X, Err)]

ax.plot(X, Y)
ax2.scatter([1, 2, 3, 4, 5, 6, 7, 8], [5, 3, 7, 2, 78, 12, 0, 12])

# %%


fig, ax = plt.subplots(nrows=1, ncols=2)

ax[0].scatter(X, Y, s=10, marker='o', facecolors='none', edgecolors='red')
# ax[0].set_axis_off()
ax[1].plot(X, Y, linewidth=1, c='red')
== == == =
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 01:14:28 2020

Autor: Gustavo Kildegaard (gustavo.kildegaard@gmail.com)
"""
#%%     ## IMPORTS ##
from matplotlib import pyplot as plt
import numpy as np

#%%     ## Inicios ##

# Creamos algunos vectorcitos
X = [x for x in range(-100, 101)]
Y1 = [x**3 for x in X]
Y2 = [(x**3 + 2 * x**2) for x in X]

"""
Primero definimos la figura (fig) que sería el marco donde vamos a meter n cantidad de gráficos (axes)

Se usa el método .subplots(# de filas, # de columnas)
De esta forma, queda definido una "grilla" de ejes en donde vamos a poder graficar; para ese, hay que
aclarar en qué gráfico se quiere operar usando notación matricial
"""

fig, ax = plt.subplots(1, 2, sharey=True)

fig.suptitle('Varios Axes en una sola Figure')

ax[0].set_xlabel('Valores de X')
ax[0].set_ylabel('Valores de Y')
ax[0].set_xlim((-150, 150))
ax[0].grid(True)

ax[0].plot(X, Y1)

ax[1].set_xlabel('Valores de X')
ax[1].grid(True)

ax[1].plot(X, Y2)

# %%

'''
Hay dos formas de hacer las cosas en Matplotlib, la forma tipo POO y la forma tipo "pyplot-style"
'''

# %%

'''
POO Style
'''

x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.


# %%

'''
Pyplot Style
'''

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

# %%

'''
Como uno tiende a usar frecuentemente un mismo tipo de gráfico, lo cómodo es armar una función con todos los parámetros
y ya.
Por ejemplo:
'''


def graficar(graf, ax, data1, data2, parametros=None):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    parametros : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    if graf == 'plot':
        if parametros:
            out = ax.plot(data1, data2, **parametros)
        else:
            out = ax.plot(data1, data2)
    elif graf == 'scat':
        if parametros:
            out = ax.scatter(data1, data2, **parametros)
        else:
            out = ax.scatter(data1, data2)
    return out

# %%


'''
Esto anterior lo usamos así!
'''

data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
graficar(ax, data1, data2, {'marker': 'x'})

# %%
import matplotlib.pyplot as plt
plt.ion()
# O por ejemplo:

np.random.seed(1337)

X = np.linspace(-100, 100, 100)
Err = np.random.normal(loc=0, scale=5, size=100)
Y = [2 * x + 1 + er for x, er in zip(X, Err)]

fig, ax = plt.subplots(1, 1)

graficar('scat', ax, X, Y, {'marker': 'x', 's': 20})


# %%


# %%

'''
Esto es una boludez que estaba probando

Podés primero crear la figura con plt.figure() y dp añadirle axes con add_subplot

O podés hacer todo junto con el fig, ax = plt.subplots

'''

fig = plt.figure()

fig.suptitle('Figura vacia')

ax = fig.add_subplot(1, 1, 1)
ax.set_title('Un subplot')

ax2 = fig.add_subplot(2, 2, 4)
ax2.set_title('qué onda')
frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])

X = np.linspace(-100, 100, 100)
Err = np.random.normal(loc=0, scale=5, size=100)
Y = [2 * x + 1 + er for x, er in zip(X, Err)]

ax.plot(X, Y)
ax2.scatter([1, 2, 3, 4, 5, 6, 7, 8], [5, 3, 7, 2, 78, 12, 0, 12])

# %%


fig, ax = plt.subplots(nrows=1, ncols=2)

ax[0].scatter(X, Y, s=10, marker='o', facecolors='none', edgecolors='red')
# ax[0].set_axis_off()
ax[1].plot(X, Y, linewidth=1, c='red')
