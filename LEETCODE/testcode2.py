# Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

# Return any permutation of A that maximizes its advantage with respect to B.

# Example 1:

# Input: A = [2,7,11,15], B = [1,10,4,11]
# Output: [2,11,7,15]
# Example 2:

# Input: A = [12,24,8,32], B = [13,25,32,11]
# Output: [24,32,8,12]
def advantageCount(A, B):
    A.sort()
    B_sorted = sorted(B)[::-1]
    newdict = {}
    res = []
    for b in B_sorted:
        if b < A[-1]:
            newdict.setdefault(b, []).append(A.pop())
    for b in B:
        try:
            res.append(newdict[b].pop())
        except:
            res.append(A.pop())
    return res

A = [2,0,4,1,2]
B = [1,3,0,0,2] #[24,32,8,12]
print(advantageCount(A,B))


