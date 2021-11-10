""" 
Problem 1385. Find the Distance Value Between Two Arrays

Input:
1. two integer arrays, arr1 and arr2
2. integer d

Output:
1. distance value between the two arrays

distance value is defined as the number of elements arr1[i] such that 
there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Constraints:
1. 1 <= arr1.length, arr2.length <= 500
2. -1000 <= arr1[i], arr2[j] <= 1000
3. 0 <= d <= 100

"""
def findTheDistanceValueBetweenTwoArrays(arr1, arr2, d):
    arr2.sort()
    def binarySearch(arr1Element):
        firstIndex, lastIndex = 0, len(arr2)
        while firstIndex < lastIndex:
            middleIndex = (firstIndex+lastIndex)//2
            if abs(arr2[middleIndex]-arr1Element) <= d:
                return False
            elif arr2[middleIndex] > arr1Element:
                lastIndex = middleIndex
            else:
                firstIndex = middleIndex + 1
        return True

    return sum(binarySearch(element) for element in arr1)

arr1, arr2 = [2,1,100,3], [-5,-2,10,-3,7]
d = 6
print(findTheDistanceValueBetweenTwoArrays(arr1, arr2, d))