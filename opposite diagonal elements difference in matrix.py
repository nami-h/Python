mylist=[]
n=int(input())
m=1
s1=[]
s=[]   
sum1=0
sum2=0

while(m<=n):
    tim=input()
    tam=tim.split(' ')
    s1.clear()
    for x in tam:
        x=int(x)
        s1.append(x)
        mylist.append(s1) 
    s.append(list(s1))  
    m+=1   

diag1=[s[i][i] for i in range(len(s))]
for i in diag1:
    sum1+=i

diag2=[s[n-i-1][i] for i in range(len(s))]
for i in diag2: 
    sum2+=i

print(abs(sum1-sum2))
