import math

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
        # if one of them is 0 the append the other
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

