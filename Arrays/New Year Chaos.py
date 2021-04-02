#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes1(q):
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribes+=1

def minimumBribes(q):
    bribes = 0
    for i in range(len(q) - 1, 1, -1):
        if q[i] != i + 1:
            if q[i - 1] == i + 1:
                tmp = q[i]
                q[i] = i + 1
                q[i - 1] = tmp
                bribes += 1
                print(q)
            elif q[i] != i + 1 and q[i - 2] == i + 1:
                bribes += 2
                for j in range(2, 0, -1):
                    tmp = q[i - (j - 1)]
                    q[i - (j - 1)] = q[i - j]
                    q[i - j] = tmp
                    print(q)
            else:
                return 'Too chaotic'
    if q[0] != 1:
        bribes += 1
    return bribes



if __name__ == '__main__':
    n = 5
    q = [2, 1, 5, 3, 4]
    print(minimumBribes(q))

