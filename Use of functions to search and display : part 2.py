paint=['green', 'blue','yellow','black','brown']
color=input("Enter a color: ")

def find_it(color, paint):
    for item in paint:
        if item==color.lower():
            return "Found it "
        else:
            pass 
    return  "Not found"

print(color, " : ", find_it(color,paint))
