#Ways to create Dictionary

dictA = {'thap':'son', 'hung':'brother', 'Me Duyen':'mom'}

dict_temp = [('thap', 'son'), ('hung','brother'), ('Me Duyen','mom')]
dictB = dict(dict_temp)

# dictC = dict(thap = 1, hung = 2, 'Me Duyen' = 3) #Can not use with space

list1 = ['thap', 'hung', 'Me Duyen']
list2 = ['son', 'brother', 'mom']
dictD = dict(zip(list1, list2))

print(dictA == dictB == dictD)

list_from_keys = ['thap','hung','mom']
dictE = dict.fromkeys(list_from_keys, 0)
print(dictE)
