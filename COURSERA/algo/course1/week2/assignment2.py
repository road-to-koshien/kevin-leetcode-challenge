#Uses Python3
n = int(input())
a, b = 0, 1
if n == 1:
    print(1)
else:
    for i in range(0, n):
        a, b = b%10, a%10 + b%10
    print(a)
    
