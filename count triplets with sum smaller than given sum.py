def countTriplet(arr, n, sum):
    count=0
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if(arr[i]+arr[j]+arr[k]<sum):
                    count+=1
    return count



arr=[5, 1, 3, 4, 7]
n=len(arr)
sum=12
print(countTriplet(arr, n, sum))
