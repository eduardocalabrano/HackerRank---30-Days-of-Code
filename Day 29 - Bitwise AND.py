#!/bin/python3

import math
import os
import random
import re
import sys

def calcula_maximo(n, k):
    max = 0
    #posa = 0
    #posb = 0
    for a in range(1, k):
        for b in range(a+1, n+1):
            resultado = a & b #Bitwise Operators
            #print('A= {} , B= {}, A&B = {}'.format(a, b, resultado))
            if(resultado > max and resultado < k):
                max = resultado
                posa = a
                posb = b
                if(resultado == a):
                    break
    else:
        #print('A-{} y B-{}'.format(posa, posb))
        return(max)




if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        print(calcula_maximo(n, k))
