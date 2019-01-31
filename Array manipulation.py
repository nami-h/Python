from array import *
array1=array('i',[10,20,30,40,50,60,70])
for x in array1:
    print(x)
    
print(array1)

print(array1[4])

array1.insert(7,80)
print(array1)

array1.remove(60)
print(array1)

del array1[3]
print(array1)

print(array1.index(30))

array1[4]=12

for x in array1:
    print(x)
    
    
    
'''

10
20
30
40
50
60
70
array('i', [10, 20, 30, 40, 50, 60, 70])
50
array('i', [10, 20, 30, 40, 50, 60, 70, 80])
array('i', [10, 20, 30, 40, 50, 70, 80])
array('i', [10, 20, 30, 50, 70, 80])
2
10
20
30
50
12
80


'''
