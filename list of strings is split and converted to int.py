s=int(input())
tot=0
l=" "

ele=input()               #Elements input
l+=ele

x=l.split()               #split into a list of strings

for j in range(len(x)):
    x[j]=int(x[j])        #list elements from string to int 

for i in range(len(x)):  
    tot+=x[i]             #list addition 
    
print(tot)
