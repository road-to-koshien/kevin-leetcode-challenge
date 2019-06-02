A = [18,12,-18,18,-19,-1,10,10]

sums = sum(A)
equal = sums / 3
sum_temp = 0
count = 0
for each in A:
    sum_temp = sum_temp + each
    if sum_temp != equal:
        continue
    else:
        count += 1
        sum_temp = 0
if count == 3:
    print(True)
else:
    print(False)

print(equal)
print(count)