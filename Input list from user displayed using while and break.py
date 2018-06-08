
# coding: utf-8

# In[23]:


print("Enter price of items")
pur=[] 
while True: 
    p=input()
    pur.append(p)
    if p=='q' or p=='Q': 
        break
pur.pop()
print ("The prices of items are ",pur)

