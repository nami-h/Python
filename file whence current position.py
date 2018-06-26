days=open('days.txt','w+')
days.write("Mon\nTue\nWed\nThurs\nFri\nSat\nSun")
days.seek(0)
readit=days.read()
print(readit,'\n')
days.close()


days=open('days.txt','r')
days.seek(19,0)            #start at 19th position
readit=days.read()
print(readit)
