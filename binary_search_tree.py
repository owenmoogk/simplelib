class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def addChild(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = Node(data)
        if data > self.data:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = Node(data)
    
    def findMin(self):
        if self.left:
            return(self.left.findMin())
        else:
            return(self.data)

    def findMax(self):
        if self.right:
            return(self.right.findMax())
        else:
            return(self.data)

    def calculateSum(self):
        elements = self.inOrderTraversal()
        sum = 0
        for i in elements:
            sum += i
        return(sum)

    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inOrderTraversal()
        return elements

    def search(self, val):
        if self.data == val:
            return(True)
        elif val > self.data:
            if self.right:
                return(self.right.search(val))
            else:
                return(False)
        elif val < self.data:
            if self.left:
                return(self.left.search(val))
            else:
                return(False)

def removeDuplicatesFromList(array):
    array = list(dict.fromkeys(array))
    return(array)

def getMedian(array):
    array.sort()
    length = len(array)
    medianIndex = round(length/2) - 1
    return(array[medianIndex])

def buildTree(elements):
    elements = removeDuplicatesFromList(elements)
    root = Node(elements[0])
    for i in range(1,len(elements)):
        root.addChild(elements[i])
    return(root)

if __name__ == "__main__":
    numbers = [8,13,4,56,-9,155,8,8,8]
    numbersTree = buildTree(numbers)
    print(numbersTree.findMax())