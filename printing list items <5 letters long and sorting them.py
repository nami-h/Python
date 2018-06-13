visited = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
new=[]
for city in visited: 
    if len(city)<=5:
        new.append(city)

print(new)
n=sorted(new)        
print(n)
