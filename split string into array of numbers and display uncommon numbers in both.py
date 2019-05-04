l=[]
m=[]
x=int(input())
y=input().split(' ')
for i in y: 
    i=int(i)
    l.append(i)
a=int(input())
b=input().split(' ')
for j in b:
    j=int(j)
    m.append(j) 
l=set(l)
m=set(m)
new=[]
for i in l:
    if i not in m:
        new.append(i)
for j in m:
    if j not in l:
        new.append(j)
n=[]
new=sorted(new)
for k in new:
    print(k)
    
    

'''

I/P
4
2 4 5 9
4
2 4 11 12

O/P
5
9
11
12


'''
