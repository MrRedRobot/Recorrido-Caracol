#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 18:30:20 2019

@author: dav_o
"""

import numpy as np
from io import StringIO

def leerMatriz():
    return np.genfromtxt(StringIO((open('holamundo4','r')).read()), delimiter  = ',' )

def rotarMatriz(matriz):
    return np.rot90(matriz, k=1, axes=(0, 1))

def avanzar(matriz):
    if matriz.shape[0]==1:
        return matriz[0,0:1]
    else:
        return matriz[(matriz.shape[0]-1) , 1:matriz.shape[1]]

def recortar(matriz):
    return matriz[1:matriz.shape[0]-1 , 1:matriz.shape[1]-1]
               
def recorrer(matriz,l):   
    if matriz.shape[0]==1:
        print(avanzar(matriz))
        return "Fin"
    
    if matriz.shape[0]>0:
        if l>0:
            print(np.fliplr([avanzar(matriz)])[0])
            recorrer(rotarMatriz(matriz),l-1)
            
        else:
            recorrer(recortar(matriz),4)
            

print("Matriz Objetivo:")    
print(leerMatriz())
print("RECORRIDO CARACOL:") 
print(recorrer(leerMatriz(),4))
