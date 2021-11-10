""" 
Problem 167. Two Sum II - Input Array Is Sorted

Input:
1. 1-indexed array of integer numbers that is already sorted in non-decreasing order
2. target number

Find two numbers such that they add up to the specific target number.

Output:
1. the indices of the two numbers, index1 and index2, 
added by one as an integer array [index1, index2] of length 2.

You may not use the same element twice.

Constraints:
1. 2 <= numbers.length <= 3 * 104
2. -1000 <= numbers[i] <= 1000
3. numbers is sorted in non-decreasing order.
4. -1000 <= target <= 1000
5. The tests are generated such that there is exactly one solution.
"""
def twoSum2(numbers,target):
    result = []
    elementCounter=1
    #Get the difference of target with 1st element
    #If difference exists in numbers array using binary search, append both the indices+1 of the element and difference
    for element in numbers:
        #Check if result already have content/answer
        if result:   
            break
        else:
            difference=target-element
            position=binarySearch(numbers, difference)+1
            #Check that same element is not used twice
            if elementCounter != position and position != None:
                result.append(elementCounter)
                result.append(position)
                break
            elementCounter += 1
    result.sort()
    return result

def binarySearch(array, difference):
    firstIndex, lastIndex = 0, len(array)-1
    while firstIndex <= lastIndex:
        middleIndex = firstIndex + (lastIndex-firstIndex)//2
        if difference == array[middleIndex]:
            return middleIndex
        elif difference > array[middleIndex]:
            firstIndex = middleIndex + 1
        else:
            lastIndex = middleIndex - 1

#numbers, target = [2,3,4], 6
numbers, target = [0,0,3,4], 0
print(twoSum2(numbers, target))
