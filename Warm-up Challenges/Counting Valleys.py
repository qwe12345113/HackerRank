#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(path):
    inV = False
    countV = 0
    sealevel = 0
    str2num = []
    for i in path:
        if i == 'U':
            str2num.append(1)
        else:
            str2num.append(-1)

    for j in str2num:
        sealevel += j
        if sealevel < 0 and not inV:
            inV = True
        if sealevel == 0 and inV:
            countV += 1
            inV = False
    return countV

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(path)

    fptr.write(str(result) + '\n')

    fptr.close()
