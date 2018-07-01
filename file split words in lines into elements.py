!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt
temp=open('mean_temp.txt','r')
heading=temp.readline()

split2=heading.split(',')
print(split2, "\n")

line=temp.readlines()
split = [i.split(',') for i in line]           #split lines into elements 
for words in split: 
    print(split2[0], " of ", words[0], split2[2] , " is ", words[2], " Celcius ")
    
    
    
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
['city', 'country', 'month ave: highest high', 'month ave: lowest low\n'] 

city  of  Beijing month ave: highest high  is  30.9  Celcius 
city  of  Cairo month ave: highest high  is  34.7  Celcius 
city  of  London month ave: highest high  is  23.5  Celcius 
city  of  Nairobi month ave: highest high  is  26.3  Celcius 
city  of  New York City month ave: highest high  is  28.9  Celcius 
city  of  Sydney month ave: highest high  is  26.5  Celcius 
city  of  Tokyo month ave: highest high  is  30.8  Celcius 
'''
