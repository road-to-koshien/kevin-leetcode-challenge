#Uses Python3
a = input()
lists = a.split()
x = int(lists[0]) 
y = int(lists[1])
if y%2 == 0:
    t = y*2
else:
    t = (y-1)*4 +4
k = x%t
a, b = 0, 1
for i in range(0, k):
    a, b = b, a+ b
print(a%y)
print(k)
