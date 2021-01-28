def shellSort(elements):
    size = len(elements)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = elements[i]
            j = i
            while j >= gap and elements[j-gap] > anchor:
                elements[j] = elements[j-gap]
                j -= gap
            elements[j] = anchor
        gap = gap // 2

if __name__ == "__main__":
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [5]
    ]
    for i in tests:
        shellSort(i)
        print(i)