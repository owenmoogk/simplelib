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

def mergeListsAndSort(*arg):
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
        x = mergeListsAndSort(arg)
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

def decimalToBinary(number):
    number = int(number)
    binaryNumber = ''
    while number > 0:
        binaryNumber = str(number%2) + binaryNumber
        number = int(number/2)
    return(int(binaryNumber))

def decimalToHex(number):
    hexNum = str(hex(number)).upper()
    return(hexNum[2:])

def binaryToDecimal(number):
    number = str(number)
    multiplier = 1
    result = 0
    for i in range(len(number)-1, -1, -1):
        result += int(number[i]) * multiplier
        multiplier *= 2
    return(result)

def hexToDecimal(number):
    number = str(number)
    number = number.lower()
    dictionary = {"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
    multiplier = 1
    result = 0
    for i in range(len(number)-1, -1, -1):
        try:
            num = int(number[i])
        except:
            num = dictionary[number[i]]
        result += num * multiplier
        multiplier *= 16
    return(result)

def reverseString(string):
    reversed = "" 
    for i in range(len(string)-1, -1,-1):
        reversed += string[i]
    return(reversed)

if __name__ == "__main__":
    # list1 = [1,14,5,64]
    # list2 = [2,87,8]
    # list3 = [53,0]
    # print(mergeLists(list1,list2,list3))
    # print(mergeListsAndSort(list1, list2, list3))

    # print(decimalToBinary(1073741823))
    # print(binaryToDecimal(101101010010001))
    # print(hexToDecimal(1544))
    # print(decimalToHex(6549295001155813370))
    print(reverseString("hello, my name is owen"))