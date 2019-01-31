def almostIncreasingSequence(sequence):    
    l=[]
    
    if len(sequence)>2 and len(sequence) != len(set(sequence)):
        boo=False
        return boo 
            
    for i in sequence:
        l=[]
        l+=sequence
        l.remove(i)
        if sorted(l)==l:
            boo= True
            return boo
            continue
        else:
            boo= False    
    return boo
