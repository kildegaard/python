# recordando grabar y leer archivos

# with open('archivito.txt', 'wt', encoding='utf8') as file:
#     file.write('Acá vamos a poner una oración')

lineas = []

with open('archivito.txt', 'rt', encoding='utf8') as f:
    for linea in f:
        lineas.append(linea)

print(lineas)
print(dir(lineas))
help(lineas.sort)

# %%


def doble(a):
    return -2 * a


num = [-5, 4, 30, -2, 1, 0]

num.sort(key=doble)

print(num)
