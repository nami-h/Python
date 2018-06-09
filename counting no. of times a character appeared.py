cities=['sao paulo','hyderabad','shanghai','melbourne','new york']
tot=0
for city in cities:
    tot+=city.lower().count('a' or 'b')
print("no. of times a or b appeared in the names: ", tot)
