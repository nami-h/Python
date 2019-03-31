#!/bin/python3

import os
import sys

def timeConversion(s):
    
    if s[0]=='1' and s[1]=='2' and s[-2]=='P':
        x=s 
    elif s[-2]=='P':
        v=str((int(s[0:2]))+12)
        x=s.replace(s[0:2], v)
    elif s[0]=='1' and s[1]=='2' and s[-2]=='A':
        v='00'
        x=s.replace(s[0:2], v)      
    else:
        x=s
    b=""
    for char in x:
        if char.isalpha()!=True:
            b+=char
    return b

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()
