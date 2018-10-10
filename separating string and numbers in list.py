n=int(input())
l=[]
req=''

while n!=0:
    arr=input()
    l.append(arr)
    n-=1

x=str(input())

for y in l:
    if x in y:
        req=y

for j in req:
    b=req.split(" ")

m=(float(b[1])+float(b[2])+float(b[3]))/3
print("%.2f" %round(m,2))
