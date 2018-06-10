mon=["jan","feb","mar","apr","may","jun", "jul"]   
temp=[]
mon_len=int(len(mon)/2)
print(mon_len)
for num in range(mon_len-1, mon_len+2):
    temp.append(mon[num])
print("3rd, 4th and 5th are: ", temp)  
