#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n, acumulado):
    if(n == 1):
        return(acumulado)
    else:
        acumulado = acumulado * n
        return(factorial(n-1, acumulado))

if __name__ == '__main__':

    n = int(input())
    result = factorial(n, 1)
    print(result)
