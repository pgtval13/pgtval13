""" 
Problem 1213. Intersection of Three Sorted Arrays

Input:
1. 3 integer arrays sorted in increasing order : arr1, arr2, arr3

Output:
1. A sorted array of only the integers that appeared in all 3 arrays

Constraints:
1. 1 <= arr1.length, arr2.length, arr3.length <= 1000
2. 1 <= arr1[i], arr2[i], arr3[i] <= 2000

"""

def intersectionOfThreeSortedArrays(arr1,arr2,arr3):
    x_loc, y_loc, z_loc = 0,0,0
    n1=len(arr1)
    n2=len(arr2)
    n3=len(arr3)
    resultingArray=[]

    while x_loc != n1 and y_loc != n2 and z_loc != n3:
        x = arr1[x_loc]
        y = arr2[y_loc]
        z = arr3[z_loc]
        if x==y and y==z:
            resultingArray.append(x)
            x_loc+=1
            y_loc+=1
            z_loc+=1
        elif x<=y and x<=z:
            x_loc+=1
        elif y<=x and y<=z:
            y_loc+=1
        else:
            z_loc+=1
    
    return resultingArray

firstArray=[1,2,3,4,5]
secondArray=[1,3,4,5,8]
thirdArray=[1,2,5,7,9]

print(intersectionOfThreeSortedArrays(firstArray,secondArray,thirdArray))