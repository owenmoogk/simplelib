def mergeSortedArrays(a,b):
    sortedList = []
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            sortedList.append(b[0])
            b.pop(0)
        else:
            sortedList.append(a[0])
            a.pop(0)
    sortedList += a + b
    return(sortedList)

def mergeSort(elements):
    if len(elements) == 1:
        return(elements)
    mid = len(elements) // 2
    left = elements[:mid]
    right = elements[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return(mergeSortedArrays(left, right))

if __name__ == "__main__":
    elements = [21,38,29,17,4,25,32,9]
    print(mergeSort(elements))