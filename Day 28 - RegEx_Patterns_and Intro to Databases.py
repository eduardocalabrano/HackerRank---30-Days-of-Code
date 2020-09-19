#!/bin/python3

import math
import os
import random
import re
import sys

def evaluareg(correo):
    x = re.search("@gmail.com$", correo)
    return(x)



if __name__ == '__main__':
    N = int(input())
    listado_ok = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if(evaluareg(emailID)):
            listado_ok.append(firstName)
    else:
        listado_ok.sort()
        for x in listado_ok:
            print(x)
