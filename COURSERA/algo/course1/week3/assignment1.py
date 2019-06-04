#Uses Python3
n = int(input())
count = 0
if n//10 >0:
    count = count + n//10
    n = n - (n//10)*10
if n//5 > 0:
    count = count + n//5
    n = n - (n//5)*5
count = count + n
print(count)