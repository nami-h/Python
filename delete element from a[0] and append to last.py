x=input()
swit=x.split(' ')
me=[]
for k in swit:
    k=int(k)
    me.append(k)
for k in me:
    a=me[0]         #no. of array elements
    d=me[1]         #no. of rotations
    
l=[]
p=input()
splitup=p.split(' ') 
for x in splitup:
    x=int(x)
    l.append(x)

for item in l:
    while d:
        s=l[0]
        l.remove(s)
        l.append(s)
        d-=1

string=' '.join(str(e) for e in l)
print(string)
    
