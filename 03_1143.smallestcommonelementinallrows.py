""" 
Problem 1143. Find Smallest Common Element in All Rows

Input:
1. A matrix where every row is sorted in increasing order

Output:
1. The smallest common element in all rows
2. If there is no common element, return -1

Constraints:
1. 1 <= mat.length, mat[i].length <= 500
2. 1 <= mat[i][j] <= 10^4
3. mat[i] is sorted in increasing order

"""

def smallestCommonElementInAllRows(mat):
    intersections = set(mat[0])
    for i in range(1, len(mat)):
        intersections &= set(mat[i])
        if not intersections:
            return -1
    
    return min(intersections)

mat=[[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
print(smallestCommonElementInAllRows(mat))
