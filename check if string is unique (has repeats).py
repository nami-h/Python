def unique(s):
    x=[]
    for l in s:
        x.append(l)
    if sorted(x)==sorted(set(s)):
        return True
    else:
        return False
    
print(unique('abbdc'))
