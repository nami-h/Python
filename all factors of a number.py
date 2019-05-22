n=int(input())
l=[]
for i in range(1, n):
    if n%i==0:
        l.append(i)
print(l)                           



#better time complexity

n=int(input())
l=[]
for i in range(2, round(n/2)+1):
    if n%i==0:
        l.append(i)
    
print(l)



#better time complexity O(sqrt(n))

import math

n=int(input())
l=[]
for i in range(1, round(math.sqrt(n))+1):
    if n%i==0:
        l.append(i)
        if i!=int(math.sqrt(n)):
            l.append(int(n/i))
    
print(sorted(l))
