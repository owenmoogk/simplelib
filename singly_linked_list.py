class node:
    
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class singlyLinkedList:

    def __init__(self):
        self.head = node()

    def append(self, data):
        newNode = node(data)
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = newNode

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
            if currentIndex == index:
                lastNode.next = currentNode.next
                return
            currentIndex += 1

    def eraseItem(self,item):
        currentNode = self.head
        currentIndex = 0
        while currentNode.next != None:
            currentNode = currentNode.next
            if currentNode.data == item:
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