elements_40 = ['Hydrogen', 
 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 
 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 
 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 
 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium']

for ele in elements_40:
    if ((elements_40.index(ele)%2)==0):
        print(ele," At. no. : ", elements_40.index(ele)+1)
