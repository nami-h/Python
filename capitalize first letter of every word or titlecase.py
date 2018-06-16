poem = "Write code frequently*Save code frequently*Comment code frequently*Study code frequently"
split=poem.split('*')
print(split)

for line in split[::-1]:
    line.title()
    print(line)
