num = 1993
list_num = [int(x) for x in list(str(num))]
list_sorted = sorted(list_num)
list_sorted = list_sorted[::-1]
for i in range(0, len(list_num)):
    if list_num[i] != list_sorted[i]:
        t = list_sorted[i]
        k = str(num).rindex(str(t))
        list_num[i], list_num[k] = list_num[k], list_num[i]
        break
print(list_num)
res = [str(x) for x in list_num]
res1 = int(''.join(res))
print(res1)