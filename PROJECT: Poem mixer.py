def mixer(words):
    stuff=[]     
    for wer in words: 
        stuff.append(wer)   
    lis=[]                        #new list
    stuff.sort()
    if count>5: 
        for each in stuff: 
            lis.append(each)
        top=stuff[::-1]
        for each in stuff:
            if (top.index(each)==4):
                x=top[4]
                lis.append(x)
                lis.remove(x)      
        for first in stuff:
            if (stuff.index(first)==0):
                lis.append(first)
                lis.pop(0)
        y=stuff[-1]
        lis.append(y)
        lis.remove(y)
        bin=" ".join(lis)
    return bin
        
    
poem=input("Enter a few lines of poetry or a random sentence: ")
words=poem.split()                             # split poem into list of words 
count=0
for part in words: 
    count+=1                                   #count number of words in input
new=[]
for part in words: 
    if (len(part)<=3):
        low=part.lower()
        new.append(low)
    elif(len(part)>3 and len(part)<7): 
        new.append(part)
    elif (len(part)>=7):
        hi=part.upper()        
        new.append(hi)
big=" ".join(new)
if (count<5):
    print("Poem mixer output: ", big)

if (count>=5): 
    mixer(new)
    fin=str(mixer(new))
    print("Poem mixer output: ", ''.join(fin))    
