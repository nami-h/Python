import numpy as np
a=np.array([1,2,3])
print(a)
print(a.shape)
print(a[0])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(b[0,0],b[0,1],b[1,0])
print(np.zeros((2,2)))        #double brackets for rank         
print(np.zeros((1,2)))
print(np.ones((1,2)))
print(np.full((2,2),7))
print(np.eye(3))
print(np.random.random((2,2)))
print(np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))





"""
[1 2 3]
(3,)
1
[[1 2 3]
 [4 5 6]
 [7 8 9]]
1 2 4
[[0. 0.]
 [0. 0.]]
[[0. 0.]]
[[1. 1.]]
[[7 7]
 [7 7]]
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
[[0.71801492 0.46652169]
 [0.8508548  0.72712303]]
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
 
 """
