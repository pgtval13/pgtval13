""" 
Problem 702. Search in a Sorted Array of Unknown Size

Input:
1. array sorted in ascending order
2. target number to be searched in the array

However, the array size is unknown to you.
You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).
You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.

Output:
1. if target exists, then return its index, otherwise return -1

Constraints:
1. You may assume that all elements in the array are unique.
2. The value of each element in the array will be in the range [-9999, 9999].

"""
def searchInASortedArrayOfUnknownSize():



array = [-1,0,3,5,9,12]
target = 9
print(searchInASortedArrayOfUnknownSize(array,target))

