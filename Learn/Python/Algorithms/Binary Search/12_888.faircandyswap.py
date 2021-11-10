""" 
Problem 888. Fair Candy Swap

Input:
1.  two integer arrays aliceSizes and bobSizes where 
aliceSizes[i] is the number of candies of the ith box of candy that Alice has and 
bobSizes[j] is the number of candies of the jth box of candy that Bob has.

Exchange one candy box each so that after the exchange, they both have the same total amount of candy. 
The total amount of candy a person has is the sum of the number of candies in each box they have.

Output:
1. integer array answer where answer[0] is the number of candies in the box that Alice must exchange, 
and answer[1] is the number of candies in the box that Bob must exchange. 

If there are multiple answers, you may return any one of them. 
It is guaranteed that at least one answer exists.

Constraints:
1. 1 <= aliceSizes.length, bobSizes.length <= 104
2. 1 <= aliceSizes[i], bobSizes[j] <= 105
3. Alice and Bob have a different total number of candies.
4. There will be at least one valid answer for the given input.
"""
def fairCandySwap(aliceSizes, bobSizes):
    aliceCandiesSum = sum(aliceSizes)
    candiesPerPerson = (aliceCandiesSum + sum(bobSizes))//2
    i = 0
    bobSizes.sort()
    while i < len(aliceSizes):
        if aliceCandiesSum - aliceSizes[i] < candiesPerPerson:
            bobExchangeable = candiesPerPerson - (aliceCandiesSum - aliceSizes[i])
            if binarySearch(bobSizes, bobExchangeable):
                return [aliceSizes[i], bobExchangeable]
        i += 1

def binarySearch(array, target):
    firstIndex, lastIndex = 0, len(array)-1
    while firstIndex <= lastIndex:
        middleIndex = firstIndex + (lastIndex-firstIndex)//2
        if target == array[middleIndex]:
            return True
        elif target > array[middleIndex]:
            firstIndex = middleIndex + 1
        else:
            lastIndex = middleIndex - 1
    return None

aliceSizes, bobSizes = [1,2,5], [2,4]
print(fairCandySwap(aliceSizes,bobSizes))