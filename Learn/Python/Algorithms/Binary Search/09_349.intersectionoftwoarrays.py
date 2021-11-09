"""
Problem 349. Intersection of Two Arrays

Input:
1. two integer arrays nums1 and nums2

Output:
1. an array of their intersection
Each element in the result must be unique and you may return the result in any order.

Constraints:
1. 1 <= nums1.length, nums2.length <= 1000
2. 0 <= nums1[i], nums2[i] <= 1000

"""
def intersectionOfTwoArrays(nums1,nums2):
    n1=len(nums1)
    n2=len(nums2)
    if n1<n2:
        n1, n2 = n2, n1
        nums1, nums2 = nums2, nums1
    nums2.sort()

    results = set()
    for elements in nums1:
        if binarySearch(nums2,elements):
            results.add(elements)
    return results

def binarySearch(numbers,target):
    firstIndex, lastIndex = 0, len(numbers)-1
    while firstIndex <= lastIndex:
        middleIndex = firstIndex + (lastIndex-firstIndex) //2
        if target==numbers[middleIndex]:
            return True
        elif target>numbers[middleIndex]:
            firstIndex=middleIndex+1
        else:
            lastIndex=middleIndex-1
    return False

nums1, nums2 = [4,9,5], [9,4,9,8,4]
print(intersectionOfTwoArrays(nums1,nums2))
