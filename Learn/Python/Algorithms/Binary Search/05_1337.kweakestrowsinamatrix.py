""" 
Problem 1337. The K Weakest Rows in a Matrix

Input:
1. A m x n binary matrix. The 1's are all positioned on the left of all 0's in each row.

Row i is weaker than row j if one of the following is true:
-the number of 1's in row i < number of 1's in row j
-both rows have the same number of 1's and i < j

2. k is the number of weakest rows

Output:
1. The indices of the k weakest rows in the matrix ordered from weakest to strongest

Constraints:
1. m == mat.length
2. n == mat[i].length
3. 2 <= n, m <= 100
4. 1 <= k <= m
5. matrix[i][j] is either 0 or 1

"""
def kWeakestRowsInAMatrix(matrix,k):
    result = []
    for rowIndex, row in enumerate(matrix):
        #Use Binary Search to find index of rightmost 1 in the row
        #Binary Search will return index+1, this can be used as count of 1's in the row
        numberOf1s = binarySearch(row,1)
        result.append([numberOf1s, rowIndex])
    result.sort(key=lambda x: x[0])
    return [result[rowIndex][1] for rowIndex in range(k)]


def binarySearch(row, target):
    #lastIndex is +1 of index since it will be used to count numbers of 1
    firstIndex, lastIndex = 0, len(row)

    while firstIndex < lastIndex:
        middleIndex = (firstIndex+lastIndex)//2
        if row[middleIndex]==target:
            firstIndex=middleIndex+1
        else:
            lastIndex=middleIndex
    return firstIndex


matrix = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 3
print(kWeakestRowsInAMatrix(matrix,k))