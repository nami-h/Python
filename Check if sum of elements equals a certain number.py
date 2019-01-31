def sumOfTwo(a, b, v):
    x=0
    if len(a)==0 or len(b)==0:
        if v in b or v in a:
            return False
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if a[i]+b[j]==v:
                return True
                break
            else:
                x = False
    return x
