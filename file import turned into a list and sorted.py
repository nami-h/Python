!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow -o rainbow.txt
rainbow_file=open('rainbow.txt','r')
lis=[]
for lin in rainbow_file:
    print(lin)
    lis.append(lin)    
lis.sort()
print("Alphabetical order: ")
for letters in lis: 
    print(letters)    
rainbow_file.close()
