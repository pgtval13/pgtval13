#Binary Search Code
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

