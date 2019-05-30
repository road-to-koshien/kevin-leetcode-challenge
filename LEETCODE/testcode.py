# # Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i 
# # for which A[i] > B[i].

# # Return any permutation of A that maximizes its advantage with respect to B.

# # Example 1:

# # Input: A = [2,7,11,15], B = [1,10,4,11]
# # Output: [2,11,7,15]
# # Example 2:

# # Input: A = [12,24,8,32], B = [13,25,32,11]
# # Output: [24,32,8,12]

# A = [2,0,4,1,2]
# B = [1,3,0,0,2]

# # A = [12,24,8,32] 
# # B = [13,25,32,11]
# newdict = {}
# res = []
# x = sorted(A)
# y = sorted(B)
# minB = min(y)
# for i,each in enumerate(x):
#     if each > minB:
#         k = i
#         break
# x1 = x[k:]
# x2 = x[:k]
# x_sorted = x1 + x2
# for i,each in enumerate(x_sorted):
#     if y[i] in newdict:
#         newdict[y[i]].append(each)
#     if y[i] not in newdict:
#         newdict[y[i]] = [each]
# for each in B:
#     if len(newdict[each]) > 1:
#         t = newdict[each]
#         res.append(t.pop())
#         newdict[each] = t
#     else:
#         res.append(newdict[each][0])
# print(res)

x = "loveleetcode"
print(x.split('e'))