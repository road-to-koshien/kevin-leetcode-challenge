s = "0P"
del_list = [' ',':',',','.']
list_strs = list(s)
list_strs = list(filter(lambda x: x.isalpha() == True,list_strs))
check = ''.join(list_strs).lower()
print(check)
print(check[::-1])
if check[::1] == check[::-1]:
    print(True)
else:
    print(False)