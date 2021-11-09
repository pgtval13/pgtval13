"""
Binary Search

Input:
1. A list of numbers sorted in increasing order
2. A number to be searched in the list

Output:
1. The index of the searched number in the list
2. If number is not found in the list, return None

Constraints:

"""

def search(items, target):
    firstIndex = 0
    lastIndex = len(items)-1

    while firstIndex<=lastIndex:
        middleIndex=firstIndex+(lastIndex-firstIndex)//2
        if target==items[middleIndex]:
            return middleIndex
        elif target<items[middleIndex]:
            lastIndex=middleIndex-1
        else:
            firstIndex=middleIndex+1    
    return None

nums = [-1,0,3,5,9,12]
target = 9
print(search(nums,target))

