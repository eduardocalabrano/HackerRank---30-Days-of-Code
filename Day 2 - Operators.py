#!/bin/python3

# Task
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
#
# Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

import math
import os
import random
import re
import sys


def solve(meal_cost, tip_percent, tax_percent):
    tip_percent_amount = float((meal_cost * tip_percent) / 100)
    tax_percent_amount = float((meal_cost * tax_percent) / 100)
    return(round(meal_cost + tip_percent_amount + tax_percent_amount))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))
