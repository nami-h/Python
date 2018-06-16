code_tip = "Python-uses-spaces-for-indentation"
split=code_tip.split('-')
print(split)

split_a=code_tip.split('a')
print(split_a)

sp="Python uses spaces for indentation"
split_sp=sp.split(' ')
print(split_sp)

big_quote = """Jack and Jill went up the hill
To fetch a pail of water
Jack fell down and broke his crown
And Jill came tumbling after"""
br=big_quote.split('\n')
print(br)

for line in br[::-1]:
    print(line)
