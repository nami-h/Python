#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    a=1
    y='#'
    while(a<=n):
        print((a*y).rjust(n))  
        a+=1  

if __name__ == '__main__':
    n = int(input())
    staircase(n)
    
 '''   
    Output:
     #
    ##
   ###
  ####
 #####
######
