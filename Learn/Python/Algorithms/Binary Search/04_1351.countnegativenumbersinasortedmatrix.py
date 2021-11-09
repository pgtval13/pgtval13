""" 
Problem 1351. Count Negative Numbers in a Sorted Matrix

Input:
1. A m x n matrix sorted in decreasing order both row-wise and column-wise

Output:
1. The number of negative numbers in the matrix

Constraints:
1. m == grid.length
2. n == grid[i].length
3. l <= m, n <= 100
4. -100 <= grid[i][j] <= 100

"""
def binarySearch(numbers):
    firstIndex=0
    lastIndex=len(numbers)-1
    length=len(numbers)

    while firstIndex+1 <= lastIndex:
        middleIndex = firstIndex + (lastIndex-firstIndex) //2
        if numbers[middleIndex] > -1:
            firstIndex=middleIndex+1
        elif numbers[middleIndex] < 0:
            lastIndex=middleIndex

    if numbers[firstIndex] < 0:
        return length-firstIndex
    if numbers[lastIndex] < 0:
        return length-(firstIndex+1)
    
    return 0


def countNegativeNumbersInASortedMatrix(mat):
    negatives= 0

    for row in mat:
        #Perform binary search to find negative numbers in current row
        negatives += binarySearch(row)
    
    return negatives
        

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegativeNumbersInASortedMatrix(grid))