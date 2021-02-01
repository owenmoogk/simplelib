def optimizedSelectionSort(array):
    for i in range(len(array)//2):
        lowest = array[i]
        highest = array[i]
        lowestIndex = i
        for j in range(i,len(array)-i):
            if array[j] < lowest:
                lowest = array[j]
                lowestIndex = j
            elif array[j] > highest:
                highest = array[j]
        array[i], array[lowestIndex] = array[lowestIndex], array[i]
        highestIndex = -1
        for index, x in enumerate(array):
            if x == highest:
                highestIndex = index
        array[len(array)-i-1], array[highestIndex] = array[highestIndex], array[len(array)-i-1]

if __name__ == "__main__":
    elements = [1,54,5,31,56,32,1,24,5,342,64,2,-2,5.5]
    optimizedSelectionSort(elements)
    print(elements)