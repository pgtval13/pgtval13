""" 
Remove Duplicates from Sorted Array

Topics: arrays, two pointers

Input:
1. integer array sorted in non-decreasing order

Remove the duplicates in-place such that each unique element appears only once.

Place the elements in the first part of the array, ie if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result.

The relative order of the elements should be kept the same.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Output:
1. k after placing the final result in the first k slots of nums

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Constraints: 
1. 0 <= nums.length <= 3 * 104
2. -100 <= nums[i] <= 100
3. nums is sorted in non-decreasing order.
"""
def removeDuplicates(sortedNumbers):
    indexOfUniqueValue = 1
    for indexOfCurrent in range(1, len(sortedNumbers)):
        if sortedNumbers[indexOfCurrent] != sortedNumbers[indexOfCurrent-1]:
            sortedNumbers[indexOfUniqueValue] = sortedNumbers[indexOfCurrent]
            indexOfUniqueValue += 1
    return indexOfUniqueValue

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
print(nums)