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