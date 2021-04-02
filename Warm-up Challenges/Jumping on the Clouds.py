#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count, step_now = 0, 0
    done = False
    while not done:
        if step_now+2 > (len(c) - 1) and c[step_now+1] != 1:
            count += 1
            done = True
        elif step_now+2 <= (len(c) - 1):
            if (c[step_now+1] != 1 and c[step_now+2] != 1) or (c[step_now+1] == 1 and c[step_now+2] != 1):
                step_now += 2
                count += 1
            elif (c[step_now+1] != 1 and c[step_now+2] == 1):
                step_now += 1
                count += 1

            if step_now == (len(c) - 1):
                done = True
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
