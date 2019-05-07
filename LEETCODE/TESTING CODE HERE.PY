A = [6,0,8,2,1,5]


list_index = []
for i,each in enumerate(A):
    list_index.append(i)
list_check = [x for _,x in sorted(zip(A,list_index))]
max_current = 0
i_min = float('inf')
for each in list_check:
    max_current = max(max_current, each - i_min)
    i_min = min(each, i_min)
print(max_current)
