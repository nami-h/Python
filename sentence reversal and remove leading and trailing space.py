def sent_rev(s):
    l=[]
    x=s.split(' ')
    l=x[::-1]
    if l[0]=='':
        l.remove('')
    elif l[-1]=='':
        l.remove('')
    s=str(' '.join(l))
    return s
    
print(sent_rev(' Hi John,  are you ready to go? '))


'''

go? to ready you are  John, Hi 


'''
