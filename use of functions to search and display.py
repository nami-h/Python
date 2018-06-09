def numbers (term, list1=['1','2','3','4','5']):
    for num in list1:
        if num == term:
            return True
        else:
            pass
    return False

list2=['6','7','8','9','0']
term1=input("Find number in list 1: ")
print(term1, " in list 1: ", numbers(term1))
term2=input("Find another number in list 2: ")
print(term2, " in list 2: ", numbers(term2,list2))
