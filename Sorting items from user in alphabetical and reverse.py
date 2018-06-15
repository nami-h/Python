lis=[]
num=int(input("How many animals do you want to enter? "))
for add in range(num):
    add=input("Enter animal: ")
    lis.append(add)  
animals=['horse','cat','mouse']
s=lis+animals
print("Our list consists of: ", s)
s.sort()
print("Alphabetically ordered: ", s)
s.reverse()
print("Reverse ordered: ",s)
