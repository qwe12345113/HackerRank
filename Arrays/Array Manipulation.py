import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * n
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
    return arr


if __name__ == '__main__':
    n = 10
    m = 4
    queries = [[2, 6, 8],
               [3, 5, 7],
               [1, 8, 1],
               [5, 9, 15]]


    result = arrayManipulation(n, queries)
    print(result)
