A = [54,64,85,85,35,42,16,59,39,70,31,37,66,16,24,56,67,13,42,46]
B = [41,7,69,70,25,54,83,75,1,32,23,87,70,75,2,75,15,19,47,61]
# sumA, sumB = 0, 0
# newdict = {}
# for each in A:
#     sumA += each
# for each in B:
#     sumB += each
# if sumA > sumB:
#     A,B = B,A
# equal = (sumA + sumB)/2
# exchange = abs(sumA - equal)
# for each in B:
#     if each-exchange not in newdict:
#         newdict[each-exchange] = each
# for each in A:
#     if each in newdict:
#         print([each, newdict[each]])
# print(newdict)
# print(sumA, sumB, equal, exchange)

print(sum(A))