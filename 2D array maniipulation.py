from array import *
a=[[2,3,4],[6,8,9],[0,5,1]]
a.insert(1, [0,0,0])

for i in a:
    for j in i:
        print(j, end="")
    print() 
a[2]=[11,0]
a[0][2]=7

for i in a:
    for j in i:
        print(j, end="")
    print()     
    
    
'''
    
234
000
689
051
237
000
110
051


'''
