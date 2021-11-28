""" 
Remove Element

Topics: arrays, two pointers

Input:
1. integer array nums
2. value to be removed val

Remove all occurrences of val in-place from the integer array. The relative order of the elements may be changed.

Output:
1. k after placing the final result in the first k slots of integer array(k is number of elements after removing val, not index of last element after removing val)

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:
1. 0 <= nums.length <= 100
2. 0 <= nums[i] <= 50
3. 0 <= val <= 100
"""
def removeElement(nums, val):
    indexOfNotVal = 0
    for indexOfCurrent in range(0, len(nums)):
        if nums[indexOfCurrent] != val:
            nums[indexOfNotVal] = nums[indexOfCurrent]
            indexOfNotVal += 1
    return indexOfNotVal

nums = [0,1,2,2,3,0,4,2] #k is 5 after removing all 2's
val = 2
print(removeElement(nums, val))
print(nums)