def selectionSort(array):
    for i in range(len(array)):
        lowest = array[i]
        lowestIndex = i
        for j in range(i,len(array)):
            if array[j] < lowest:
                lowest = array[j]
                lowestIndex = j
        array[i], array[lowestIndex] = array[lowestIndex], array[i]

if __name__ == "__main__":
    elements = [1,54,5,31,56,32,1,24,5,342,64,2]
    selectionSort(elements)
    print(elements)