elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 
 'Potassium', 'Calcium']

length=len(elements)
for ele in elements:
    if ((elements.index(ele))%2!=0):
        print(ele, "At. no. : ", elements.index(ele)+1)
