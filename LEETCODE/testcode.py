B = ["loo","eo"]

newdict = {}
for each in B:
    for letter in each:
        if letter in newdict:
            newdict[letter] = max(each.count(letter), newdict[letter])
        if letter not in newdict:
            newdict[letter] = each.count(letter)

print(newdict)
x = list(newdict.items())
print(x)
for each in x:
    print(each[0], each[1])