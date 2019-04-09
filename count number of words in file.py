!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o poem1.txt
poem_file=open('poem1.txt', 'r')
x=poem_file.read()
c=x.splitlines()         split text into lines
count=0
for words in c:
    r=words.split(' ')      split lines into words
    if len(r)>1:
        count+=len(r)
    else:
        count+=1
print("total", count)
