# Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix and flip every cell in that column.  Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.

# Return the maximum number of rows that have all values equal after some number of flips.

 

# Example 1:

# Input: [[0,1],[1,1]]
# Output: 1
# Explanation: After flipping no values, 1 row has all values equal.
# Example 2:

# Input: [[0,1],[1,0]]
# Output: 2
# Explanation: After flipping values in the first column, both rows have equal values.
# Example 3:

# Input: [[0,0,0],[0,0,1],[1,1,0]]
# Output: 2
# Explanation: After flipping values in the first two columns, the last two rows have equal values.

def maxEqualRowsAfterFlips(A):
    dic = {}
    for row in A:
        combination = []
        for num in row:
            converted_num = num ^ row[0]      # if first number in row is 0, go with , if 1 then flip all numbers in row
                                              # Ex. [0,1,1] would become [0,1,1] and [1,0,0] would become [0,1,1]
                                              # This is to make [1,0,0] same as [0,1,1]
            combination.append(converted_num)

        tup = tuple(combination)
        print(tup)              # This is just to make this combination hashable in dictionary
        if tup in dic:
            dic[tup] += 1
        else:
            dic[tup] = 1

    return max(dic.values())

A = [[0,0,0],[0,0,1],[1,1,0]]
print(maxEqualRowsAfterFlips(A))


