!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o poem1.txt
poem_file=open('poem1.txt','a+')          #append and read
poem_file.write('\nExtra appended stuff')
poem_file.seek(0)                        
newone=poem_file.read()
print(newone)


'''Loops I repeat
loops
loops
loops
I repeat
until I
break

Extra appended stuff'''
