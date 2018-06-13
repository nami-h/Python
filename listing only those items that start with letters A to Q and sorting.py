visited = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
new=[]
visited.sort()
print(visited)
for city in visited:
    if 'A' <=city[0] <='Q':
        new.append(city)

print(new)
