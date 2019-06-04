#Uses Python3
n = input()
a = input().split()
x = [int(x) for x in a]
b = input().split()
y = [int(x) for x in b]
res = 0
x.sort()
y.sort()
for i,each in enumerate(x):
    res = res + x[i]*y[i]
print(res)