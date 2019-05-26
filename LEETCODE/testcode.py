arr = [11, 13, 21, 3] 
res = [-1] * len(arr)
stack = []
for i in range(0, len(arr)):
    while stack and arr[i] > arr[stack[-1]]:
        res[stack.pop()] = arr[i]
    stack.append(i)
print(res)


11 13 21 3
13 21 -1 -1


