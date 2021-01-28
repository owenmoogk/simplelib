def swap(a, b, arr):
    if arr[a] != arr[b]:
        arr[a], arr[b] = arr[b], arr[a]

def partition(elements, start, end):
    pivotIndex = start
    pivot = elements[pivotIndex]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while end >= 0 and elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)
        
    swap(pivotIndex, end, elements)
    return(end)

def quickSortHelper(elements, start, end):
    if start < end:
        partitionIndex = partition(elements, start, end)
        quickSortHelper(elements, start, partitionIndex - 1)
        quickSortHelper(elements, partitionIndex + 1, end)

def quickSort(elements):
    quickSortHelper(elements, 0, len(elements)-1)

if __name__ == "__main__":
    elements = [11,9,29,7,2,15,28]

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    for i in tests:
        quickSort(i)
    print(tests)