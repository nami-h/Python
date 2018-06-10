mylist=[1,2,24,5,7,8,2,90,21,0,21,43,21,1,3,5]
half_1=int(len(mylist)/2)
for num in range(half_1, len(mylist)):
    print("second half: ", mylist[num])
for num in range(0, half_1):
    print("first half: ", mylist[num])
