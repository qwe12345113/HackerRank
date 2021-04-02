#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    c_a = 0
    for i in s:
        if i == 'a':
            c_a += 1

    ans = (n // len(s)) * c_a
    for j in range(n % len(s)):
        if s[j] == 'a':
            ans += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
