def containsDuplicates(a):
   
    l=a.sort()
    x=set(a)
    if len(a)==len(x):
        return False
    elif len(a)!=len(x):
        return True
