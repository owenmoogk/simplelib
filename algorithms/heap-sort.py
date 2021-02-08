def heapify(arr, length, i): 
    largest = i         # largest is root
    l = 2 * i + 1       # left = 2*i + 1 
    r = 2 * i + 2       # right = 2*i + 2 
  
    # if right child exists and is larger than root
    if l < length and arr[i] < arr[l]: 
        largest = l 
  
    # if right child exists and is larger than root 
    if r < length and arr[largest] < arr[r]: 
        largest = r 
  
    # swap root if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify the root. 
        heapify(arr, length, largest) 

def heapSort(arr): 
    length = len(arr) 
  
    # Build a maxheap. 
    # Since last parent will be at ((n//2)-1) we can start at that location. 
    for i in range(length // 2 - 1, -1, -1): 
        heapify(arr, length, i) 
  
    # One by one extract elements 
    for i in range(length-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0)

arr = [12,11,13,5,6,7]
heapSort(arr)
print(arr)