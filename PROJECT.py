def get_names():
    ans=[]
    tot=5
    while tot:
    
        e1=input("Enter element: ")
        tot-=1
        x=e1.lower()
        if x in ans:                         #duplication 
            print(e1, " was already specified")
        elif (e1=='' or e1==" "):            #space and empty string  
            print("Unacceptable input")
        else: 
            ans.append(x)                 #add to list    
    return ans
    
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt
twenty=open('elements1_20.txt','r')    
ele_list=[]
while twenty: 
    line=twenty.readline().strip('\n \n')  #remove white spaces
    ele_list.append(line.lower())
    if line=='':
        break
print("********************Quiz***********************")
print("Enter any 5 elements from the first 20 elements in the periodic table\n")
response=get_names()
correct=[]
wrong=[]
print("\nYour response: ", response,"\n")   #user reponse
for ele in response:
    if ele in ele_list:
        print(ele, " is in the list")
        correct.append(ele)
    if ele not in ele_list: 
        print(ele, " is not in the list")
        wrong.append(ele)

print("\n\nYour correct responses: ", correct)        
print("Your incorrect responses: ", wrong)

final=len(correct)
x=final*20
print("\n\nYour score: ", x)
print("\nEnd of quiz")






'''

Output: 
********************Quiz***********************
Enter any 5 elements from the first 20 elements in the periodic table

Enter element: neon
Enter element: flourine
Enter element: 
Unacceptable input
Enter element: Neon
Neon  was already specified
Enter element: Carbon

Your response:  ['neon', 'flourine', 'carbon'] 

neon  is in the list
flourine  is not in the list
carbon  is in the list


Your correct responses:  ['neon', 'carbon']
Your incorrect responses:  ['flourine']


Your score:  40

End of quiz

'''
