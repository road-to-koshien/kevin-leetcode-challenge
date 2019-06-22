#Uses Python3
n = int(input())
num_operation = [None] * (n+1)
num_operation[1] = 0
res = [n]
for i in range(2, n+1):
    tmp1,tmp2,tmp3 = float('inf'), float('inf'), float('inf')
    tmp1 = num_operation[i-1] + 1
    if i%2 == 0:
        tmp2 = num_operation[i//2] + 1
    if i%3 == 0:
        tmp3 = num_operation[i//3] + 1
    tmp = min(tmp1,tmp2,tmp3)
    num_operation[i] = tmp
print(num_operation[n])
x = n 
while x != 1:
    if num_operation[x] == num_operation[x//2] + 1 and x%2 == 0:
        res.append(x//2)
        x = x // 2      
    elif num_operation[x] == num_operation[x//3] + 1 and x%3 == 0:
        res.append(x//3)
        x = x // 3   
    else:
        res.append(x-1)
        x = x - 1      
res = res[::-1]
for each in res:
    print(each, end=' ')
    
