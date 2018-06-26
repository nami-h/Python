!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o -poem1.txt
poem=open('poem1.txt','a')
poem.write("-The End-")
poem.seek(0)

poem=open('poem1.txt','r')
read1=poem.read()
print(read1)

'''
Loops I repeat
loops
loops
loops
I repeat
until I
break
-The End-


'''
