A = [1,2]
max1 = 0
res = 0
for i, each in enumerate(A):
    res_cur = max1 + each - i
    if res_cur > res:
        res = res_cur
    max_cur = A[i] + i
    if max_cur > max1:
        max1 = max_cur
print(res)
    
     















