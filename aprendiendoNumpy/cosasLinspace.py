# %%
import numpy as np
from matplotlib import pyplot as plt
'''
Todo esto sale de:
https://realpython.com/np-linspace-numpy/?__s=ys765jm76xn5wmdbddxy
'''

# %%
# Serie de números equiespaciados con una cantidad de datos DETERMINADA
# Contiene al start y al stop
# linspace genera float (a menos que se especifique otra cosa)

ej_1 = np.linspace(start=0, stop=10, num=11)
print(ej_1)
print(type(ej_1))
print(type(ej_1[0]))

# %%
# Podemos averiguar la separación entre elementos de linspace

numeros, step = np.linspace(start=0, stop=10, num=20, retstep=True)
print(numeros)
print(step)
# %%
# Serie de números con un ESPACIAMIENTO BIEN DEFINIDO
# arange genera enteros

ej_2 = np.arange(start=0, stop=10, step=1)
print(ej_2)
print(type(ej_2))
print(type(ej_2[0]))
# %%
# Cosas un poco más raras
# Armar matrices con valores

mat, esp = np.linspace(start=[1, 10, 100], stop=[10, 50, 200], num=10, retstep=True)
print(mat)
print(mat.shape)
print(esp)

# %%
# Podemos trasponer esto de una

mat_T = np.linspace(start=[1, 10, 100], stop=[10, 50, 200], num=10, axis=1)
print(mat_T)
print(mat_T.shape)
# %%
'''
En resumen, la función linspace tiene esta pinta:

linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

num = Cant de valores generados
endpoint = Si es True, incluye el Stop
retstep = Devuelve la longitud entre los valores
dtype = Especifica el tipo de dato
axis = 1 -> Traspone

'''

# %%
# Cosas lindas que se pueden hacer con el linspace

x_ = np.linspace(-5, 5, 100)
y_ = 4 * (x_**3) + 2 * (x_**2) + 5 * x_

plt.plot(x_, y_)

# %%
# Parameters for discretizing the mathematical function
sampling = 100
x_range = -10, 10
n_waves = 3

# Parameters are tuples with a value for each wave (2 in this case)
amplitudes = 1.7, 0.8, 5.3
wavelengths = 4, 7.5, 1
velocities = 2, 1.5, 7

time = 0  # You can set time to 0 for now

x_ = np.linspace(x_range[0], x_range[1], sampling)

# Create 2 (or more) waves using a list comprehension and superimpose
waves = [amplitudes[idx] * np.sin((2 * np.pi / wavelengths[idx]) * (x_ - velocities[idx] * time)) for idx in range(n_waves)]
superimposed_wave = sum(waves)

# Plot both waves separately to see what they look like
plt.subplot(2, 1, 1)
plt.plot(x_, waves[0])
plt.plot(x_, waves[1])
plt.plot(x_, waves[2])

# Plot the superimposed wave
plt.subplot(2, 1, 2)
plt.plot(x_, superimposed_wave)

plt.show()
# %%
for time in np.arange(0, 40, 0.2):
    # Create 2 (or more) waves using a list comprehension and superimpose
    waves = [amplitudes[idx] *
             np.sin((2 * np.pi / wavelengths[idx]) * (x_ - velocities[idx] * time)) for idx in range(n_waves)]
    superimposed_wave = sum(waves)

    plt.clf()  # Clear last figure
    plt.plot(x_, superimposed_wave)
    plt.ylim(-3, 3)  # Fix the limits on the y-axis
    plt.pause(0.1)  # Insert short pause to create animation
