a=input()
b=input()

alice=0
bob=0

a_split=a.split(' ')
b_split=b.split(' ')

n=3
while(n>0): 
    for i in range (0, len(a_split)):
        a_split[i]=int(a_split[i])
        b_split[i]=int(b_split[i])
        if a_split[i]<b_split[i]:
            bob+=1
        elif a_split[i]>b_split[i]:
            alice+=1
        n-=1
        
print(alice, bob)            
            
