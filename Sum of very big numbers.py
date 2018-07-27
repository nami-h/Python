n=int(input())
ar=input()
sum=0

x=ar.split(' ')

for i in range (0, n):
    x[i]=int(x[i])

for i in range (0, n):
    sum+=x[i]

print(sum)
