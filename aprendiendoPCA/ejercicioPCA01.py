import pandas as pd
import numpy as np
import random as rnd
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt


def main():
    genes = ['gen' + str(i) for i in range(1, 101)]

    wildType = ['wt' + str(i) for i in range(1, 6)]
    knockOut = ['ko' + str(i) for i in range(1, 6)]

    # Para armar las columnas, le mandamos las variables con * delante, que lo hace es "unpack", es decir, "abre" la lista
    # de forma tal que cada elemento de la lista wildType es una propia columna del df (sino quedaría como que el df tiene)
    # "dos columnas"
    data = pd.DataFrame(columns=[*wildType, *knockOut], index=genes)

    # print(data)

    # Ahora cargamos los valores con datos random

    for genes in data.index:
        data.loc[genes, 'wt1':'wt5'] = np.random.poisson(
            lam=rnd.randrange(10, 1000), size=5)
        data.loc[genes, 'ko1':'ko5'] = np.random.poisson(
            lam=rnd.randrange(10, 1000), size=5)

    print(data.head(15))
    print(data.tail(15))


if __name__ == '__main__':
    main()
