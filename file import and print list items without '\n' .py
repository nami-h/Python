!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt
cities_file=open('cities.txt','r')
cities_lines=cities_file.readlines()
print(cities_lines)
for city in cities_lines:
    print(city)
count=0
for line in cities_lines: 
    cities_lines[count]=line[:-1]
    count+=1
print(cities_lines) 

cities_file.close()                   #close file
