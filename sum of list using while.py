print("Enter price of items") 
pur=[] 
while True: 
    p=input() 
    pur.append(p) 
    if p=='q' or p=='Q': 
        break 
pur.pop() 
print ("The prices of items are ",pur)

sub=0 
pur=[int(i) for i in pur]
while True: 
    one=pur.pop()
    sub+=one
    if not pur:
        break
print("Total is ", sub)