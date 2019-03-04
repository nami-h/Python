def strange_words(x):
    l=[]
    for i in x:
        if len(i)<6:
            l.append(i)
        elif i[0]=='e' or i[0]=='E':
            l.append(i)
        if len(i)<6 and (i[0]=='e' or i[0]=='E'):
            l.remove(i)
    return l

x=["taco", "eggs", "excellent", "exponential", "artistic", "cat", "eat", "proper", "key", "earth", "ether", "mountain"]
print(strange_words(x))


                
'''
['taco', 'excellent', 'exponential', 'cat', 'key']


'''
                
    
                
    
