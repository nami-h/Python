numbers_1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
numbers_2 = list(range(30,50,2))
num=numbers_1+numbers_2
print(num)

first_row = ['Hydrogen', 'Helium']
second_row = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
first_row.extend(second_row)
print(first_row)
