
new_file=open('poem2.txt','w')
print(new_file)
new_file.write('Dayum.....! The power!!!')
new_file.write("\nWeekdays assemble ")
new_file.close()
new_file=open('poem2.txt','r')
lines=new_file.readline()
while lines:
    print(lines)
    lines=new_file.readline()
new_file.close()
