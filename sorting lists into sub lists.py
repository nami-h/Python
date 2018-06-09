new= [2,-4,-6,23,0,1,6,8,5,7,9,21,41]
print(new)
short=[]
long=[]
for num in new:
    if(num%2==0):
        short.append(num)
    else:
        long.append(num)
print("even list: ",short," and odd list: ", long)   
