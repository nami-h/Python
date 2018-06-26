tips_file=open('codex.txt','w+')
tips_file.write('-use simple function and variable names\n-comment code\n-organize code into functions\n')

tips_file.seek(0,2)
tips_file.write("-use seek(0,2) to set read/write at end of file\n".upper())
tips_file.seek(0,0)
tipsy=tips_file.read()
print(tipsy)
