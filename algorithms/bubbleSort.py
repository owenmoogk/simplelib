def bubbleSort(elements):
    size = len(elements)
    for j in range(0,size-1):
        swapped = False
        for i in range(0,size-1-j):
            if elements[i] > elements[i+1]:
                tmp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = tmp
                swapped = True
        if not swapped:
            break
        

if __name__ == "__main__":
    elements = [43,2,5,3,46,312,65,24,2,4,6,3]

    bubbleSort(elements)
    print(elements)