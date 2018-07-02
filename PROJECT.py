def get_names():
    ans=[]
    tot=5
    while tot:
    
        e1=input("Enter element: ")
        tot-=1
        x=e1.upper()
        if x in ans:                         #duplication 
            print("already there")
        elif (e1=='' or e1==" "):            #space and empty string  
            print("unacceptable")
        else: 
            ans.append(x)                 #add to list
            
    return ans
    
print(get_names())
