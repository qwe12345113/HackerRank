#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    n = len(s)
    res = 0
    for l in range(1, n):  # 決定要找的字串的長度 長度從 1 到 len(s)
        cnt = {}
        for i in range(n - l + 1):
            tmp_list = []
            tmp_str = s[i:i + l]
            subs = ''
            for k in range(len(tmp_str)):  # 將字串的的每個char存到list
                tmp_list.append(tmp_str[k])
            tmp_list.sort()  # 排序
            for k in range(len(tmp_str)):  # char照list裡的順序組成字串
                subs += tmp_list[k]
            # 將字串存到dict 若dict有相同字串就+1 沒有就存該字串
            if subs in cnt:
                cnt[subs] += 1
            else:
                cnt[subs] = 1
            res += cnt[subs] - 1
            print(cnt[subs] - 1)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        fptr.write(str(result) + '\n')
    fptr.close()    
