def max_and_sec(arr):
    max_num=0
    sec=0
    for num in arr:
        max_num=max(num,max_num)
    arr.remove(max_num)
    for val in arr:
        sec=max(val, sec)
    return max_num, sec

print(max_and_sec([2,3,-9,5,7,0,1]))
