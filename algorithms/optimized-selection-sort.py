def optimizedSelectionSort(array):
    for i in range(len(array)//2):
        lowest = array[i]
        highest = array[i]
        lowestIndex = i
        highestIndex = i
        for j in range(i,len(array)-i):
            if array[j] < lowest:
                lowest = array[j]
                lowestIndex = j
            elif array[j] > highest:
                highest = array[j]
                highestIndex = j

        if highestIndex > lowestIndex:
            array.pop(highestIndex)
            array.pop(lowestIndex)
        else:
            array.pop(lowestIndex)
            array.pop(highestIndex)

        array.insert(i, lowest)
        array.insert(len(array)-i, highest)

if __name__ == "__main__":
    elements = [1,54,5,31,56,32,1,24,5,342,64,2,-2, 56, 56, 56, 5.5, 5.5, 5.5, 342, 64]
    optimizedSelectionSort(elements)
    print(elements)