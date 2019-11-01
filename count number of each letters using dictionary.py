def nonrep(a):
    dictionary={}
    for i in a:
        if i in dictionary:
            dictionary[i]+=1
        else:
            dictionary[i]=1
    print(dictionary)
a="geeksforgeeks"
nonrep(a)
