def adjacentElementsProduct(inputArray):
    i=0
    l=[]
    while(i<len(inputArray)-1):
        l.append(inputArray[i]*inputArray[i+1])
        i+=1
        
    return max(l)
