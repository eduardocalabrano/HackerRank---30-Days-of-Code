#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    while(len(arr) > n):
        arr.pop(len(arr) - 1)
    rev = arr.copy()
    rev.reverse()
    res = ''
    for x in rev:
        res += '{} '.format(x)
    print(res)
