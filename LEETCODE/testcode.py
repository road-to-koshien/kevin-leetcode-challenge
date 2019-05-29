customers = [1,0,1,2,1,1,7,5]
grumpy =    [0,1,0,1,0,1,0,1]
X = 3
sum1 = 0
sum2 = 0
max = 0
for i,each in enumerate(customers):
    if grumpy[i] == 0:
        sum1 += each
        customers[i] = 0
for i,each in enumerate(customers):
    sum2 += each
    if i >= X:
        sum2 -= customers[i-X]
    if sum2 > max:
        max = sum2
print(sum1 + max)



















