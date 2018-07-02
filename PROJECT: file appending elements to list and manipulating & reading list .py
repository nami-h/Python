!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt
temp=open('mean_temp.txt','r')
heading=temp.readline()

split2=heading.split(',')              # split line with elements separated by ',' into list of elements  

# output is : ['city', 'country', 'month ave: highest high', 'month ave: lowest low\n'] 

line=temp.readlines()
split = [i.split(',') for i in line]           #split lines into elements 
for words in split: 
    print(split2[0], " of ", words[0], split2[2] , " is ", words[2], " Celsius ")
temp.close()



plus=open('mean_temp.txt','a+')
plus.write("Rio de Janeiro,Brazil,30.0,18.0\n")
plus.seek(0)
newfile=plus.read()
print("\nList wit Rio:\n", newfile)

plus.seek(0)
head=plus.readline()
splitx=head.split(',')

lin=plus.readlines()
spli=[j.split(',') for j in lin]
for word in spli:
    print(splitx[0], " of ", word[0], splitx[2], " is ", word[2], " Celsius ")
temp.close()


'''
city,country,month ave: highest high,month ave: lowest low
Beijing,China,30.9,-8.4
Cairo,Egypt,34.7,1.2
London,UK,23.5,2.1
Nairobi,Kenya,26.3,10.5
New York City,USA,28.9,-2.8
Sydney,Australia,26.5,8.7
Tokyo,Japan,30.8,0.9
'''



'''
Output: 

city  of  Beijing month ave: highest high  is  30.9  Celsius 
city  of  Cairo month ave: highest high  is  34.7  Celsius 
city  of  London month ave: highest high  is  23.5  Celsius 
city  of  Nairobi month ave: highest high  is  26.3  Celsius 
city  of  New York City month ave: highest high  is  28.9  Celsius 
city  of  Sydney month ave: highest high  is  26.5  Celsius 
city  of  Tokyo month ave: highest high  is  30.8  Celsius 

List wit Rio:
 city,country,month ave: highest high,month ave: lowest low
Beijing,China,30.9,-8.4
Cairo,Egypt,34.7,1.2
London,UK,23.5,2.1
Nairobi,Kenya,26.3,10.5
New York City,USA,28.9,-2.8
Sydney,Australia,26.5,8.7
Tokyo,Japan,30.8,0.9
Rio de Janeiro,Brazil,30.0,18.0

city  of  Beijing month ave: highest high  is  30.9  Celsius 
city  of  Cairo month ave: highest high  is  34.7  Celsius 
city  of  London month ave: highest high  is  23.5  Celsius 
city  of  Nairobi month ave: highest high  is  26.3  Celsius 
city  of  New York City month ave: highest high  is  28.9  Celsius 
city  of  Sydney month ave: highest high  is  26.5  Celsius 
city  of  Tokyo month ave: highest high  is  30.8  Celsius 
city  of  Rio de Janeiro month ave: highest high  is  30.0  Celsius 
'''

