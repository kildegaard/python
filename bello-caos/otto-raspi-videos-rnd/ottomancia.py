#! C:\ProgramData\Anaconda3\python.exe

import os
import random

# print(os.getcwd())
# print(os.listdir('folder1/carpeta_con_videos'))

'''
for _, directorios, archivos in os.walk('.'):
    print(f'Directorios: {directorios}\nArchivos: {archivos}\n\n')
'''

directorio_util = 'folder1/carpeta_con_videos'

# print(os.listdir(directorio_util))

print(random.choice(os.listdir(directorio_util)))
