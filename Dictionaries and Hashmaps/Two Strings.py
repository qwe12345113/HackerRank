#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    tmp = {}
    # make dict
    for i, val in enumerate(s1):
        tmp[val] = i + 1
    yes = 0
    for c in s2:
        if c in tmp:
            yes += 1

    if yes != 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':

    s1 = 'hi'

    s2 = 'world'

    result = twoStrings(s1, s2)
    print(result)