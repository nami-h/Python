tips_file=open('codex.txt','w+')
tips_file.write('-use simple function and variable names\n-comment code\n-organize code into functions\n')
tips_file.seek(0)
tipsy=tips_file.read()               #reads whole doc
tips_file.seek(0)
tipsy2=tips_file.readline()            #reads one line
print(tipsy)
print(tipsy2)
