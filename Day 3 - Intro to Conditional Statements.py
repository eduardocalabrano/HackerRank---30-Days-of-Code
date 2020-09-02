#!/bin/python3

# Task
# Given an integer, N, perform the following conditional actions:
#
# If N is odd, print Weird
# If N is even and in the inclusive range of 2 to 5, print Not Weird
# If N is even and in the inclusive range of 6 to 20, print Weird
# If N is even and greater than 20, print Not Weird

import math
import os
import random
import re
import sys

def evalua_par(num):
    if(num%2==0):
        return(True)
    else:
        return(False)

if __name__ == '__main__':
    N = int(input())
    if(N >= 1 and N <= 100):
        flag = evalua_par(N)
        if(flag):
            if(N >= 2 and N <= 5):
                print('Not Weird')
            if(N >= 6 and N <= 20):
                print('Weird')
            if(N > 20):
                print('Not Weird')
        else:
            print('Weird')
