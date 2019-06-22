list_input = [1,2,3,4,5,6]#IN[0]
divide1 = [3,3]#IN[1]
divide2 = [1,1,1,2,1]#IN[2]
result, temp, temp2, res = [], [], [], []
t, k = 0,0
error = False

if sum(divide1) != sum(divide2) or sum(divide1) != len(list_input):
    error = True

for i in divide1:
	for j in range(t, t + i):
		if j == len(list_input):
			break
		temp.append(list_input[j])
	result.append(temp)
	temp = []
	t += i

for i in result:
    count = 0
    temp = []
    for j in range(k, len(divide2)):
        if divide2[j] == 1:
            count += 1
            temp.append(i[count-1])
        if divide2[j] > 1:
            for w in range(count, count + divide2[j]):
                print(count, divide2[j])
                temp2.append(i[w])
            temp.append(temp2)
            temp2 = []
            count = count + divide2[j]
        if count == len(i):
            k = k + count -1
            break
    res.append(temp)

# if error:
#     OUT = ('Please check again your input. The length of list and sub-list is not equal')
# else:
#     OUT = res

print(res)