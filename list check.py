
#checks if string is a part of another string or not
while my_list is True:
    check=input("Enter name of animal to find in list")
    my_list=["lion","cat","dog","horse","elephant","tiger","sloth","zebra","monkey"]
    if check in my_list is True:
        my_list.remove(0)
    elif check in my_list is False:
        my_list.append(check)
    elif check == " ":
        my_list.pop()
    elif my_list==[]:
        exit(0)
    elif check.upper=="QUIT":
        exit(0)
