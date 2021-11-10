""" 
Problem 1608. Special Array With X Elements Greater Than or Equal X

Input:
1. array of non-negative integers. 

An array is considered special if there exists a number x such that 
there are exactly x numbers in the array that are greater than or equal to x.

x does not have to be an element in nums.

Output:
1. x if the array is special, otherwise, return -1.

It can be proven that if nums is special, the value for x is unique.

Constraints:
1. 1 <= nums.length <= 100
2. 0 <= nums[i] <= 1000
"""
def specialArrayWithXElementsGreaterThanOrEqualX(nums):
    firstIndex, lastIndex = 0, len(nums)
    while firstIndex <= lastIndex:
        middleIndex = firstIndex + (lastIndex-firstIndex)//2
        count = 0
        for element in nums:
            if element >= middleIndex:
                count += 1
        if count == middleIndex:
            return middleIndex
        elif count > middleIndex:
            firstIndex = middleIndex + 1
        else:
            lastIndex = middleIndex -1
    return -1

nums = [0,4,3,0,4]
print(specialArrayWithXElementsGreaterThanOrEqualX(nums))