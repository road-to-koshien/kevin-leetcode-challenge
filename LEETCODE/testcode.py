A = [2,1,2]
def check_triangle(a,b,c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False
A.sort()
A = A[::-1]
print(A)
i = 0
while i+2 <= len(A) - 1:
    if check_triangle(A[i], A[i+1], A[i+2]) == True:
        print((A[i] + A[i+1] + A[i+2]))
        break
    else:
        i +=1
print(0)

# print(check_triangle(2,2,1))