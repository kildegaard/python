#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:15:43 2020

@author: gus
"""
import sys

def main(argv):
    arch_entrada = argv[1]
    arch_salida =  argv[2]
    
    lineas_entrada = []
    with open(arch_entrada, 'r') as file_in:
        for linea in file_in:
            linea = linea.strip('\n')
            campos_de_linea = linea.split(',')
            lineas_entrada.append(campos_de_linea[1:])
            # print(lineas_entrada)
    # print(lineas_entrada)
    # print(lineas_entrada[0][0])
    lineas_salida = trasponerListaDeListas(lineas_entrada)
    
    with open(arch_salida, 'w') as file_out:
        for elemento in lineas_salida:
            print(','.join(elemento), file = file_out)
            
def trasponerListaDeListas(lista): 
	""" 
	Dada una lista de listas, la traspone como si tratara de una matriz. 
	Así, si se recibe una lista que contiene cinco (5) listas, y cada lista contiene tres (3) elementos,  
	esta función devolverá una lista que contendrá 3 listas, y cada lista contendrá 5 elementos. 
	
	Por ejemplo, si lista es [ [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12] ]
	trasponerListaDeListas(lista) devolverá [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
	
	 
	Recibe: 
	    lista: [[]] - Una lista de listas que contiene elementos de algún tipo (e.g., int). Se espera que todas las sublistas tengan la misma longitud. 
	     
	Devuelve: 
	    result: [[]] - Una lista de listas, con la trasposición de la lista original. 
	 
	""" 
	cantFilas = len(lista[0]) 
	traspuesta = [[] for _ in range(cantFilas)] # Creo una lista que sólo contiene las listas vacías a llenar 
	 
	for pos in range(cantFilas): 
	    for sublista in lista:      
	        traspuesta[pos].append(sublista[pos]) 
	         
	return traspuesta


if __name__ == '__main__':
    main(sys.argv)