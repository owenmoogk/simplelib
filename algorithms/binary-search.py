import time

def binarySearch(numbers, numToFind):
    leftIndex = 0
    rightIndex = len(numbers)
    
    while leftIndex <= rightIndex:
        midIndex = (leftIndex + rightIndex) // 2
        midNumber = numbers[midIndex]
        
        if midNumber == numToFind:
            return(midIndex)

        if midNumber < numToFind:
            leftIndex = midIndex + 1
        elif midNumber > numToFind:
            rightIndex = midIndex - 1
    return(-1)

def binarySearchMultiple(numbers, numToFind):
    leftIndex = 0
    rightIndex = len(numbers)
    foundIndex = None

    while leftIndex <= rightIndex:
        midIndex = (leftIndex + rightIndex) // 2
        midNumber = numbers[midIndex]
        
        if midNumber == numToFind:
            foundIndex = midIndex
            break

        if midNumber < numToFind:
            leftIndex = midIndex + 1
        elif midNumber > numToFind:
            rightIndex = midIndex - 1
    
    if foundIndex:
        allIndexes = []
        index = foundIndex
        while numbers[index] == numToFind:
            allIndexes.append(index)
            index -= 1
        index = foundIndex + 1
        while numbers[index] == numToFind:
            allIndexes.append(index)
            index += 1
        allIndexes.sort()
        return(allIndexes)
    return(-1)

# def binarySearchRecursive(numbersList, numToFind, leftIndex, rightIndex):
#     if rightIndex < leftIndex: # break case
#         return(-1)
#     midIndex = (leftIndex + rightIndex) // 2
#     if midIndex >= len(numbersList) or midIndex < 0: # edge case
#         return(-1)
#     midNumber = numbersList[midIndex]
#     if midNumber == numToFind:
#         return(midIndex)
#     if midNumber < numToFind:
#         leftIndex = midIndex + 1
#     else:
#         rightIndex = midIndex - 1
#     return(binarySearchRecursive(numbersList, numToFind, leftIndex, rightIndex))

if __name__ == "__main__":
    numbers = [1,5,6,7,8,8,8,8,9,10,15,3215]
    num = 8

    print(binarySearchMultiple(numbers, num))