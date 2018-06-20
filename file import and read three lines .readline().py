!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o poem1.txt
poem1=open('poem1.txt','r')
poem_line1=poem1.readline()
poem_line2=poem1.readline()
poem_line3=poem1.readline()
print(poem_line1+poem_line2+poem_line3)     #first three lines
