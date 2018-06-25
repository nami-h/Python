'''after any write, the pointer is at the end of text that has been written
to read the entire file, the pointer needs to be at the beginning of the file - see .seek() below to set the file pointer'''

new_file=open('new_file.txt', 'w+')
new_file.write("Poems about soccer, \naka football, \naka the beautiful game, \nin time for the World Cup.")
new_file.seek(0)
next=new_file.read()
while(next):
    print(next)
    next=new_file.read()
new_file.close()  
