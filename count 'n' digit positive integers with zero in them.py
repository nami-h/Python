import math

def number(n):
    return(9*(pow(10, n-1)-pow(9, n-1)))


n=int(input())
print(number(n))
