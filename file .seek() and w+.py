outer_planets=open("outs.txt",'w+')
outer_planets.write("Jupiter\nSaturn\nUranus\nNeptune")
outer_planets.seek(0)
outer_file=outer_planets.read()
while outer_file:
    print(outer_file)
    outer_file=outer_planets.read()
outer_planets.close()   
