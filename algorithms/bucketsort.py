# used for a range from 0 to 1

def insertionSort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = anchor
    return(elements)
        
def bucketSort(elements): 
    buckets = [] 
    slot_num = 10 # 10 means 10 slots, each slot's size is 0.1

    for i in range(slot_num): 
        buckets.append([])

    # Put array elements in different buckets  
    for j in elements: 
        index_b = int(slot_num * j)
        print(index_b)
        buckets[index_b].append(j) 

    # Sort individual buckets  
    for i in range(slot_num): 
        buckets[i] = insertionSort(buckets[i]) 

    # concatenate the result 
    k = 0
    for i in range(slot_num): 
        for j in range(len(buckets[i])): 
            elements[k] = buckets[i][j] 
            k += 1

if __name__ == "__main__":
    elements = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    bucketSort(elements)
    print(elements)