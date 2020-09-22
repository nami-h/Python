net_device={}
net_device['ip_addr']='192.168.1.1'   #key and value
print(net_device)
var1='vendor'
net_device[var1]='Cisco'
net_device['device_type']='ios'
print(net_device)

print(net_device['vendor'])
net_device['vendor']='Juniper'  #change value of key
print(net_device)
net_device2=net_device  #copying dict 
print(net_device2)
net_device3=net_device   #another dict copy 
print(net_device3 is net_device2)  #check true or false
print(net_device3==net_device) #check true or false
