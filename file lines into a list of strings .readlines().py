!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o poem1.txt
poem1=open('poem1.txt','r')
poem_lines=poem1.readlines()      #converts lines into a list of strings
print(poem_lines)
for lines in poem_lines:
    print(lines)
