
import sys                      # for exit
!curl  https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi -o pi.txt
pi=open("pi.txt",'r')
name=input("print name: ")
print("Hi ", name)
seed=len(name)
x=pi.seek(0)
y=pi.seek(seed)                  # pointer placement  

if (y<=1):                          #single char name
    print("not a name")
    sys.exit("End of game")         #exit program

y+=1
digits=pi.readline()
digits=digits[1:]


print("Enter the immediate digit that follows in pi after the number of letters in your name. Press Q to quit")

for dig in digits:
    guess=input("Number: ")
    if (guess==dig):
        print('correct.')

    elif (guess.lower()=='q'):
        print("game over")
        print("Answer: ", digits)    #shows digits from location of pointer
        break
    
    else:
        print("wrong. It's okay. Skip that digit")




'''print name: ed
Hi  ed
Enter the immediate digit that follows in pi after the number of letters in your name. Press Q to quit
Number: 3
wrong. It's okay. Skip that digit
Number: q
game over
Answer:  415926535897932384626433832795028841971693993751058209749445923
078164062862089986280348253421170679821480865132823066470938446095505822
317253594081284811174502841027019385211055596446229489549303819644288109
756659334461284756482337867831652712019091456485669234603486104543266482
13393607260249141273
