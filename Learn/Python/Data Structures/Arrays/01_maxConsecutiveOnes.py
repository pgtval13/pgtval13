""" 
Max Consecutive Ones

Input:
1. binary array nums

Output:
1. return the maximum number of consecutive 1's in the array

Constraints:
1. 1 <= nums.length <= 10^5
2. nums[i] is either 0 or 1.

Example 1.
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2.
Input: nums = [1,0,1,1,0,1]
Output: 2
"""
def findMaxConsecutiveOnes(nums):
    current,highestcount=0,0
    for element in nums:
        if element == 1:
            current+=1
            highestcount=max(highestcount,current)
        else:
            current=0
    return highestcount

nums = [1,0,1,1,0,1]
#nums = [1,1,0,1,1,1]
#nums = [0,1]
print(findMaxConsecutiveOnes(nums))