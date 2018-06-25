!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow_messy -o rainbow_messy.txt
rainbow_messy=open('rainbow_messy.txt','r')
color=rainbow_messy.readline().strip("*\n")           #remove * and newline
while color:
    print(color)
    color=rainbow_messy.readline().strip("*\n")
rainbow_messy.close()    

!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities_messy -o cities_messy.txt
cities_messy=open('cities_messy.txt','r')
line=cities_messy.readline().strip('\n : \n')       #remove newline and :
while line:
    print(line)
    line=cities_messy.readline().strip('\n : \n')
cities_messy.close() 

!curl  https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2_messy -o poem2_messy.txt
poem2_messy=open('poem2_messy.txt','r')
line=poem2_messy.readline().strip('( ) \n')          #remove ( ) and newline
while(line):
    print(line)
    line=poem2_messy.readline().strip('( ) \n')
poem2_messy.close()    
