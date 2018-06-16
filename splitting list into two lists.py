spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
length=len(spell_list)
first=[]
second=[]
for word in spell_list[:int(length/2)]:
    first.append(word)
print("first 1/2: ", first)

for wor in spell_list[int(length/2):]:
    second.append(wor)
print("second 1/2: ", second)  
