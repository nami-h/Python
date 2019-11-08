#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d={}
    for i in ar:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    x=[]
    for i in d.keys():
        if d[i]%2==0:
            x.append(d[i])
        else:
            x.append(d[i]-1)
    s=0
    for i in x:
        s+=i
    
    return int(s/2)
        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
