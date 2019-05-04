def array(arr,n):
    
    a=arr[0]
    b=arr[1]
    for i in range(0, n):
        for j in range(i+1, n):
            if (arr[i]*arr[j]>a*b):
                a=arr[i]; b=arr[j]
    
    print("{",a,",",b,"}")
    

arr=[1, 4, 3, 6, 7, 0]
n=len(arr)
array(arr, n)
