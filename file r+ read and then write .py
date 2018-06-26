!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o poem1.txt
poem_file=open('poem1.txt','r+')          #read and then write (no overwrite: not the whole file)
reading=poem_file.read() 
print(reading)
print("\nafter attachment")
poem_file.write("New loops here and there")
poem_file.seek(0)
reading=poem_file.read()
print(reading)

'''Loops I repeat
loops
loops
loops
I repeat
until I
break


after attachment
Loops I repeat
loops
loops
loops
I repeat
until I
break
New loops here and there'''
