tips_file=open('code_tips.txt','w+')
tips_file.write("There's no escape.\nThere's an escape.\nGift it to someone else")
tips_file.seek(0)
tips_text=tips_file.read()
print(tips_text)

tips_file.seek(4)
tips_text=tips_file.read()
print(tips_text)

tips_file.seek(0)
tips_text=tips_file.read()
print(tips_text[:4])
