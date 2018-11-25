n=int(input())
s=input()
count=0
extra=0
for i in s:
    if i == 'U':
        count+= 1
        if count == 0:
            extra += 1
    else:
        count -= 1
        
print(extra)





'''Input
8
UDDDUDUU

Output
1
'''
