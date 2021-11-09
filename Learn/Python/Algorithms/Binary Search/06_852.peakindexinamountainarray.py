""" 
Problem 852. Peak Index in a Mountain Array

Input:
1. array with the following properties
- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Output:
1. i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Constraints:
1. 3 <= arr.length <= 10^4
2. 0 <= arr[i] <= 10^6
3. arr is guaranteed to be a mountain array

"""
def peakIndexInAMountainArray(arr):
    firstIndex, lastIndex = 0, len(arr)-1
    while firstIndex < lastIndex:
        middleIndex = (firstIndex+lastIndex)//2
        if arr[middleIndex-1] < arr[middleIndex] and arr[middleIndex] > arr[middleIndex+1]:
            return middleIndex
        elif arr[middleIndex-1] < arr[middleIndex] and arr[middleIndex] < arr[middleIndex+1]:
            firstIndex=middleIndex
        else:
            lastIndex=middleIndex

arr = [24,69,100,99,79,78,67,36,26,19]
print(peakIndexInAMountainArray(arr))