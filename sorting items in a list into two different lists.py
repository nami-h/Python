places=['alabama',"georgia",'london','mumbai','argentina','arctic','sao paulo','antartica']
a_name=[]
no_a_name=[]
for place in places:
    if place[0].upper()=='A':
        a_name.append(place)
    else:    
        no_a_name.append(place)
print("A places : ",a_name)
print("Non a places : ",no_a_name)
