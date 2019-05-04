m=input()
n=[]
l=[]
for i in m:
    n.append(i)
for i in n:
    if i=='0':
        l.append('5')
    else:
        l.append(i)

print(''.join(l))
