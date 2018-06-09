letter=input("Enter a letter or space or - :")

def let_to_num(letter): //function to check equivalent letters 
    if letter == " ":
        phone_letter='1'
    elif letter.upper() == "A" or letter.upper()== "B" or letter.upper()=="C":
        phone_letter='2'
    elif letter.upper() == "D" or letter.upper()== "E" or letter.upper()=="F":
        phone_letter='3'
    elif letter.upper() == "G" or letter.upper()== "H" or letter.upper()=="I":
        phone_letter='4'
    elif letter.upper() == "J" or letter.upper()== "K" or letter.upper()=="L":
        phone_letter='5'
    elif letter.upper() == "M" or letter.upper()== "N" or letter.upper()=="O":
        phone_letter='6'    
    elif letter.upper() == "P" or letter.upper()== "Q" or letter.upper()=="R" or letter.upper()=="S":
        phone_letter='7' 
    elif letter.upper() == "T" or letter.upper()== "U" or letter.upper()=="V":
        phone_letter='8' 
    elif letter.upper() == "W" or letter.upper()== "X" or letter.upper()=="Y" or letter.upper()=="Z":
        phone_letter='9'
    elif letter == "-":
        phone_letter='0'
    else:    
        phone_letter='invalid '
    return phone_letter  

code=let_to_num(letter)
print("The equivalent number is: ", code)
ans=input("Another go? Print Y/N: ")
while ans.upper() in ("Y"): 
    letter=input("Enter a letter or space or - :")
    code=let_to_num(letter)
    print("The equivalent number is: ", code)
    ans=input("Another go? Print Y/N: ")
