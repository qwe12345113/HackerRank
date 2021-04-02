#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for i in range(len(q) - 1, 1, -1):
        if q[i] != i + 1:
            if q[i - 1] == i + 1:
                tmp = q[i]
                q[i] = i + 1
                q[i - 1] = tmp
                bribes += 1

            elif q[i] != i + 1 and q[i - 2] == i + 1:
                bribes += 2
                for j in range(2, 0, -1):
                    tmp = q[i - (j - 1)]
                    q[i - (j - 1)] = q[i - j]
                    q[i - j] = tmp

            else:
                return 'Too chaotic'
    if q[0] != 1:
        bribes += 1
    return bribes


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
