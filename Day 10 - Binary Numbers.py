#!/bin/python3

import math
import os
import random
import re
import sys

def transforma_binario(n):
    n_transformado = bin(n)
    n_transformado = n_transformado[2:len(n_transformado)]
    return(n_transformado)

def contador_unos(n_binario):
    acumulador_1 = 0
    maximo_1 = 0
    for num in n_binario:
        if(num == '1'):
            acumulador_1 += 1
        else:
            if(acumulador_1 > maximo_1):
                maximo_1 = acumulador_1
            acumulador_1 = 0
    else:
        if(acumulador_1 > maximo_1):
            maximo_1 = acumulador_1
        return(maximo_1)

if __name__ == '__main__':
    n = int(input())
    n_binario = transforma_binario(n)
    print(contador_unos(n_binario))
