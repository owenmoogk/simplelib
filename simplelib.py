import math, singly_linked_list, doubly_linked_list, binary_search_tree

def getInteger(message = "Input an integer: ", errorMsg = "Not an integer, Try again."):
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
            print(errorMsg)
            continue
        else:
            return (userInput)

def getFloat(message = "Input an number: ", errorMsg = "Not an number, Try again."):
    while True:
        try:
            userInput = float(input(message))       
        except ValueError:
            print(errorMsg)
            continue
        else:
            return (userInput)

def getString(message = "Input a string: "):
    userInput = str(input(message))
    return(userInput)

def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i == 0:
            return(False)
    return(True)

def getPrimesUpTo(rangeMax):
    # sieve of eratosthenes
    possibleDivisors = []
    for i in range(2,rangeMax + 1):
        possibleDivisors.append(i)
    i = 2
    while(i <= int(math.sqrt(rangeMax))):
        if i in possibleDivisors:
            for j in range(i*2, rangeMax+1, i):
                if j in possibleDivisors:
                    possibleDivisors.remove(j)
        i = i+1
    return(possibleDivisors)

def primesInList(numList):
    primeList = []
    for i in numList:
        if isPrime(i):
            primeList.append(i)
    return(primeList)

def getDictKeys(dictionary):
    return(list(dictionary.keys()))

def mergeLists(*arg):
    finalList = []
    for i in arg:
        finalList += i
    return(finalList)

def mergeListsByNumber(*arg):
    if len(arg) == 1:
        arg = arg[0]
    arg = list(arg)
    arg[0].sort()
    arg[1].sort()
    sortedList = []
    while len(arg[0]) > 0 or len(arg[1]) > 0:
        # if one of them has 0 the append the other
        if len(arg[0]) == 0:
            sortedList += arg[1]
            arg[1] = []
        elif len(arg[1]) == 0:
            sortedList += arg[0]
            arg[0] = []
        else:
            if arg[0][0] <= arg[1][0]:
                sortedList.append(arg[0][0])
                arg[0].remove(arg[0][0])
            else:
                sortedList.append(arg[1][0])
                arg[1].remove(arg[1][0])
    
    arg.remove(arg[0])
    arg[0] = sortedList
    
    if len(arg) <= 1:
        return(arg[0])
    else:
        x = mergeListsByNumber(arg)
        return(x)

def mergeListsByAlpha(*arg):
    if len(arg) == 1:
        arg = arg[0]
    arg = list(arg)
    arg[0].sort()
    arg[1].sort()
    sortedList = []
    while len(arg[0]) > 0 or len(arg[1]) > 0:
        # if one of them has 0 the append the other
        if len(arg[0]) == 0:
            sortedList += arg[1]
            arg[1] = []
        elif len(arg[1]) == 0:
            sortedList += arg[0]
            arg[0] = []
        else:
            if arg[0][0] <= arg[1][0]:
                sortedList.append(arg[0][0])
                arg[0].remove(arg[0][0])
            else:
                sortedList.append(arg[1][0])
                arg[1].remove(arg[1][0])
    
    arg.remove(arg[0])
    arg[0] = sortedList
    
    if len(arg) <= 1:
        return(arg[0])
    else:
        x = mergeListsByNumber(arg)
        return(x)

def removeDuplicatesFromList(array):
    array = list(dict.fromkeys(array))
    return(array)

def getMedian(array):
    array.sort()
    length = len(array)
    medianIndex = round(length/2) - 1
    return(array[medianIndex])

def getRange(array):
    array.sort()
    range = array[len(array)-1] - array[0]
    return(range)

def getAverage(array):
    sum = 0
    for i in array:
        sum += i
    average = sum / len(array)
    return(average)

if __name__ == "__main__":
    numbers = [8,56,13,4,3,5,6,7,-9,155,155,155]
    numbersTree = binary_search_tree.buildTree(numbers, 7)
    numbersTree.display()
    numbersTree.addChild(-14)
    numbersTree.display()
    print(numbersTree.rightSideView())
    print(numbersTree.leftSideView())



    # numbersTree.delete()
    # numbersTree.display()
    