"""
Longest Common Prefix

Topics: stringarrays

Input:
1. array of strings

Output:
1. common prefix, if it does not exist return and empty string ""

Constraints:
1. 1 <= strs.length <= 200
2. 0 <= strs[i].length <= 200
3. strs[i] consists of only lower-case English letters
"""
class Solution:
    def longestCommonPrefix1(self, strs):
        prefix = min(strs, key=len)

        for s in strs:
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]

        return prefix

    def longestCommonPrefix2(self, strs):
        pre = strs[0]
        
        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]
        
        return pre 

strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
Test = Solution()
print(Test.longestCommonPrefix1(strs1))
print(Test.longestCommonPrefix2(strs2))