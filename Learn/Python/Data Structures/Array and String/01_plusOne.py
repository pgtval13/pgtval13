""" 
Plus One

Topics: arrays

Input:
1. array representing integer digits, where each element is the th digit of the integer
eg [1,2,3,4] represents integer 1,234

The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Output:
1. resulting array

Constraints:
1. 1 <= digits.length <= 100
2. 0 <= digits[i] <= 9
3. digits does not contain any leading 0's.
"""
class Solution:
    def plusOne(self, nums):
        nums.reverse()
        for index in range(0, len(nums)):
            nums[index]=nums[index]+1
            if nums[index]>9:
                nums[index]=0
                if index+1 >= len(nums):
                    nums.append(1)
                    break
                else:
                    nums[index+1]=nums[index+1]
            else:
                break
        nums.reverse()
        return nums

nums1 = [3,6,1,0]
nums2 = [9,9,9,9]
nums3 = [4,3,2,1] 
nums4 = [0]  
nums5 = [8,9,9,9]

Test = Solution()

print(Test.plusOne(nums1))
print(Test.plusOne(nums2))
print(Test.plusOne(nums3))
print(Test.plusOne(nums4))
print(Test.plusOne(nums5))