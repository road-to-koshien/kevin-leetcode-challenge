#Uses Python3
a = input()
lists = a.split()
x = int(lists[0]) 
y = int(lists[1])
a,b = x,y
while y != 0:
    x,y = y, x%y
print(int((a//x)*b))