!curl  https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt
temp=open('mean_temp.txt','r')
heading=temp.readline()
parts=heading.split(',')       # heading 
print("Heading: ", parts,'\n')      
city_temp=temp.readlines()[1:]  #rest of list 
for cities in city_temp:
    print(cities)

for cities in city_temp:       #split into list of items
    words=cities.split(',')
    cities=cities.strip('\n')
    print(words)

print("\n")    
    
for cities in city_temp:       
    words=cities.split(',')    
    print(words[:3])     #print country, cities and high temp only 
    
    
    
    
    
    
    '''
Heading:  ['city', 'country', 'month ave: highest high', 'month ave: lowest low\n'] 

Cairo,Egypt,34.7,1.2

London,UK,23.5,2.1

Nairobi,Kenya,26.3,10.5

New York City,USA,28.9,-2.8

Sydney,Australia,26.5,8.7

Tokyo,Japan,30.8,0.9

['Cairo', 'Egypt', '34.7', '1.2\n']
['London', 'UK', '23.5', '2.1\n']
['Nairobi', 'Kenya', '26.3', '10.5\n']
['New York City', 'USA', '28.9', '-2.8\n']
['Sydney', 'Australia', '26.5', '8.7\n']
['Tokyo', 'Japan', '30.8', '0.9\n']


['Cairo', 'Egypt', '34.7']
['London', 'UK', '23.5']
['Nairobi', 'Kenya', '26.3']
['New York City', 'USA', '28.9']
['Sydney', 'Australia', '26.5']
['Tokyo', 'Japan', '30.8']
'''
