#!/bin/python3

import math
import os
import random
import re
import sys

def muestra_reloj(arreglo):
    largo_i = len(arreglo) - 2
    suma = 0
    for i in range(largo_i):
        largo_j = len(arreglo[i]) - 2
        if(largo_j > 1):
            for j in range(largo_j):
                for i1 in range(0,3):
                    for j1 in range(0,3):
                        if(i1 == 1 and j1 != 1):
                            continue
                        else:
                            suma += arreglo[i + i1][j + j1]
                            #print(arreglo[i + i1][j + j1])
                    #print('\n')
                else:
                    #print('\n=========\n')
                    #print(suma)
                    #print('\n=========\n')
                    if((i == 0 and j == 0) or suma > mayor):
                        mayor = suma
                    suma = 0
    else:
        return(mayor)

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    #arr = [[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5], [-1, -1, -1, -2, -3, -4], [-1, -9, -2, -4, -4, -5], [-7, -3, -3, -2, -9, -9], [-1, -3, -1, -2, -4, -5]]
    print(muestra_reloj(arr))
