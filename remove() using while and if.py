

types=['pug','lab','poodle','bulldog']
print(types)

if 'pug' in types:
    types.remove("pug")
else:
    print("no pug")

print(types)

while "lab" in types:
    types.remove("lab")

print(types)    

