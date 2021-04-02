#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(s1, s2):
    tmp = {}
    # make dict
    for val in s1:
        if val not in tmp:
            tmp[val] = 1
        else:
            tmp[val] += 1

    yes = 0
    for val2 in s2:
        if val2 in tmp and tmp[val2] != 0:
            yes += 1
            tmp[val2] -= 1

    if yes == len(s2):
        return 'Yes'
    else:
        return 'No'
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
