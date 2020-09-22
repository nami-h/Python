net_device={}
net_device['ip_addr']='192.168.1.1'   #key and value
print(net_device)
var1='vendor'
net_device[var1]='Cisco'
net_device['device_type']='ios'

print(net_device['vendor'])
net_device['vendor']='Juniper'  #change value of key
net_device2=net_device  #copying dict 
net_device3=net_device   #another dict copy 
print(net_device3 is net_device2)  #check true or false
print(net_device3==net_device) #check true or false


print(net_device.get('model'))    #non existent key
print(net_device.get('vendor'))   #getting values corresponding to keys
print(net_device.get('model',999)) #initializing new key value pair

print(dir(net_device2))  
net_device4=net_device.copy() #making copy 
print(net_device4 is net_device) #not identical
net_device['model']=998
print(net_device.pop('model')) #popping values
net_device2={'model':551} #change entire dict
print(net_device2)
net_device.update(net_device2) #update 
print(net_device)

for key in net_device:  #keys
    print(key)
for v in net_device.values():  #values
    print(v)
for v in net_device.items():   #key value pairs
    print(v)
for k,v in net_device.items(): #storing k and v in tuple
    print(k)
    print(v)
    print('-'*30)
