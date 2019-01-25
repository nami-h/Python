def makeArrayConsecutive2(statues):
    minimum=min(statues)
    maximum=max(statues)
    l=list(range(minimum, maximum+1))
    
    for num in statues:
        
        l.remove(num)
        
    return len(l)
    
