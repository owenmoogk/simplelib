class node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class doublyLinkedList:

    def __init__(self):
        self.head = node()

    def append(self, data):
        newNode = node(data)
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = newNode
        newNode.prev = currentNode

    def insertAtIndex(self, data, index):
        if index > self.size() or index < 0:
            print("error, out of range")
            return
        if index == self.size():
            self.append(data)
            return
        newNode = node(data)
        currentIndex = 0
        currentNode = self.head
        while True:
            lastNode = currentNode
            currentNode = currentNode.next
            if currentIndex == index:
                lastNode.next = newNode
                newNode.next = currentNode
                newNode.prev = lastNode
                currentNode.prev = newNode
                return
            currentIndex += 1

    def get(self, index):
        if index >= self.size() or index < 0:
            print("error, out of range")
            return
        currentIndex = 0
        currentNode = self.head
        while True:
            currentNode = currentNode.next
            if currentIndex == index:
                return(currentNode.data)
            currentIndex += 1

    def swap(self, index1, index2):
        if index1 == index2:
            return
        data1 = self.get(index1)
        data2 = self.get(index2)

        if index1 > index2:
            index1, index2 = index2, index1

        currentIndex = 0
        currentNode = self.head
        while True:
            currentNode = currentNode.next
            if currentIndex == index1:
                currentNode.data = data2
            if currentIndex == index2:
                currentNode.data = data1
                # we can return here knowing that node one is done, as we performed the swap above
                return
            currentIndex += 1

    def sort(self):
        size = self.size()
        for i in range(size-1):
            swapped = False
            for j in range(size-1-i):
                if self.get(j) > self.get(j+1):
                    self.swap(j, j+1)
                    swapped = True
            if not swapped:
                break

    def size(self):
        currentNode = self.head
        count = 0
        while currentNode.next != None:
            count += 1
            currentNode = currentNode.next
        return(count)
    
    def display(self):
        elements = []
        currentNode= self.head
        while currentNode.next != None:
            currentNode = currentNode.next
            elements.append(currentNode.data)
        print(elements)
    
    def erase(self,index):
        if index >= self.size() or index < 0:
            print ("error, erase out of range!")
            return 
        currentIndex = 0
        currentNode = self.head
        while True:
            lastNode = currentNode
            currentNode = currentNode.next
            if currentIndex == self.size():
                nextNode = None
            else:
                nextNode = currentNode.next
            if currentIndex == index:
                lastNode.next = currentNode.next
                if nextNode != None:
                    nextNode.prev = currentNode.prev
                return
            currentIndex += 1

    def eraseItem(self,item):
        currentNode = self.head
        currentIndex = 0
        while currentNode.next != None:
            currentNode = currentNode.next
            if currentNode.data == item:
                print("the index is ",currentIndex)
                self.erase(currentIndex)
                break
            currentIndex += 1

    def insertBefore(self, data, item):
        currentNode = self.head
        currentIndex = 0
        while currentNode.next != None:
            currentNode = currentNode.next
            if currentNode.data == item:
                self.insertAtIndex(data, currentIndex)
            currentIndex += 1

    def insertAfter(self, data, item):
        currentNode = self.head
        currentIndex = 0
        while currentNode.next != None:
            currentNode = currentNode.next
            if currentNode.data == item:
                self.insertAtIndex(data, currentIndex+1)
            currentIndex += 1

    def inList(self, item):
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
            if currentNode.data == item:
                return(True)
        return(False)

    def getItemIndex(self, item):
        currentNode = self.head
        currentIndex = 0
        indexes = []
        while currentNode.next != None:
            currentNode = currentNode.next
            if currentNode.data == item:
                indexes.append(currentIndex)
            currentIndex += 1
        if len(indexes) == 0:
            return
        if len(indexes) == 1:
            return(indexes[0])
        return(indexes)

    def deleteList(self):
        currentNode = self.head 
        while currentNode != None: 
            nextNode = currentNode.next
            del(currentNode.data) 
            currentNode = nextNode

def buildDoublyLinkedList(array):
    mylist = doublyLinkedList()
    for i in array:
        mylist.append(i)
    return(mylist)

if __name__ == "__main__":
    myArray = [1,6,5,1,6,5,18,9,-2]
    mylist = buildDoublyLinkedList(myArray)

    mylist.display()
    mylist.sort()
    mylist.display()

    # print(mylist.size())
    # mylist.insertAtIndex("hello",5)
    # mylist.display()

    # mylist.eraseItem(545)
    # mylist.eraseItem(545)
    # mylist.eraseItem(545)
    # mylist.display()

    # print(mylist.inList(1))
    # print(mylist.inList(3))

    # print(mylist.getItemIndex("boiiiii smd"))
    # print(mylist.getItemIndex("hello"))
    # print(mylist.getItemIndex(545))

    # mylist.append(1)
    # mylist.append(6)
    # mylist.display()
    # mylist.erase(1)
    # mylist.insertAfter("hello",1)
    # mylist.display()
    # print("Size:",mylist.size())
    # print("'hello' index:",mylist.getItemIndex("hello"))