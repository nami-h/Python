#poem file: 
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o poem1.txt 
poem1=open('poem1.txt','r')    
poem_line=poem1.readline()
while poem_line:
    print(poem_line[:-1].upper())
    poem_line=poem1.readline()
poem1.close()  

#rainbow colors file:
!curl  https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow  -o rainbow.txt
rainbow=open('rainbow.txt','r')
rainbow_line=rainbow.readline()
while rainbow_line:
    print(rainbow_line.upper())
    rainbow_line=rainbow.readline()
rainbow.close

