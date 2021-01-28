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

def binarySearchRecursive(numbersList, numToFind, leftIndex = 0, rightIndex = -1):
    if rightIndex == -1:
        rightIndex = len(numbersList) - 1
    if rightIndex < leftIndex:
        return(-1)
    
    midIndex = (leftIndex + rightIndex) //2
    midNumber = numbersList[midIndex]

    if midNumber == numToFind:
        return(midIndex)
    if midNumber > numToFind:
        leftIndex = midIndex + 1
    else:
        rightIndex = midIndex - 1

    return(binarySearchRecursive(numbersList, numToFind, leftIndex, rightIndex))

if __name__ == "__main__":
    numbers = [1,5,6,7,8,9,10,15,3215]
    num = 7

    print(binarySearchRecursive(numbers, num))