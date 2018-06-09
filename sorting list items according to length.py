mine=["This", "is", "a", "sentence."]
print(mine)
for each in mine:
    if (len(each)<5):
        print(each, "=small word")
    else:
        print(each, "=big word")
