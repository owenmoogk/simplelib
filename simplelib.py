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
