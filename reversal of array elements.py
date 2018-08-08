n=int(input())
array=input()

l=[]
a=array.split(' ')
for x in a: 
    x=int(x)
    l.append(x)

x=l[::-1]
b=' '.join(str(e) for e in x)
print(b)
