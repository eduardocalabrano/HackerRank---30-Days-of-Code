#!/bin/python3
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
flag = False
swaps = 0

while flag == False:
    flag = True
    for x in range(len(a) - 1):
        if(a[x] > a[x + 1]):
            numero = a[x]
            a[x] = a[x + 1]
            a[x + 1] = numero
            flag = False
            swaps += 1

print('Array is sorted in {} swaps.'.format(swaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[len(a) - 1]))
