tips_file=open('code_tips.txt','w+')
tips_file.write("first second third fourth")
tips_file.seek(0,2) # current location
tips_file.write("--Middle sentence--")
tips_file.seek(0)
tips_text=tips_file.read()
print(tips_text)
