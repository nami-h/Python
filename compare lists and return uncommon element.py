def finder(arr1, arr2):
    if arr1>arr2:
        gt=arr1
        ls=arr2
    else:
        gt=arr2
        ls=arr1
        
        
    for x in gt:
        if x not in ls:
            l=x
    return l

print(finder([11,1,2,5,7,3],[11,1,2,5,7,3]))

    
