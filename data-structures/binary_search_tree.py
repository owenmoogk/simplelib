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
    
    def deleteHalfNodes(self):

        # if leaf return self
        if self.left is None and self.right is None: 
            return(self)

        if self.left is None: 
            self.right = None
            return(self)

        if self.right is None: 
            self.left = None
            return(self)

        # recursive
        self.left = self.left.deleteHalfNodes()  
        self.right = self.right.deleteHalfNodes() 
        
        return(self) 

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

    def rightSideView(self):
        returnList = []
        returnList.append(self.data)
        if self.right != None:
            returnList += self.right.rightSideView()
        elif self.left != None:
            returnList += self.left.rightSideView()
        return(returnList)

    def leftSideView(self):
        returnList = []
        returnList.append(self.data)
        if self.left != None:
            returnList += self.left.leftSideView()
        elif self.right != None:
            returnList += self.right.leftSideView()
        return(returnList)

    def calculateSum(self):
        elements = self.inOrderTraversal()
        sum = 0
        for i in elements:
            sum += i
        return(sum)

    def invertTree(self):
        if self.right != None:
            self.right.invertTree()
        if self.left != None:
            self.left.invertTree()
        rightTemp = self.right
        leftTemp = self.left
        self.right = leftTemp
        self.left = rightTemp

    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inOrderTraversal()
        return(elements)

    def preOrderTraversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preOrderTraversal()
        if self.right:
            elements += self.right.preOrderTraversal()
        return(elements)

    def postOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.postOrderTraversal()
        if self.right:
            elements += self.right.postOrderTraversal()
        elements.append(self.data)
        return(elements)

    def getLevel(self, level):
        # gets the elements in a given level
        elements = []
        if self is None:
            return(elements)
        if level == 1:
            elements.append(self.data)
            return(elements)
        elif level > 1:
            if self.left:
                elements += (self.left.getLevel(level-1))
            if self.right:
                elements += (self.right.getLevel(level-1))
        return(elements)

    def levelOrderTraversal(self):
        elements = []
        for i in range(1,self.getHeight()+1):
            elements += self.getLevel(i)
        return(elements)

    def getHeight(self):
        if self.data == None:
            return(0)
        lheight = 0
        rheight = 0
        if self.left:
            lheight = self.left.getHeight()
        if self.right:
            rheight = self.right.getHeight()

        if lheight > rheight:
            return(lheight + 1)
        else:
            return(rheight + 1)

    def getLeaves(self):
        array = []
        if self.left:
            array += self.left.getLeaves()
        if self.right:
            array += self.right.getLeaves()
        if not self.right and not self.left:
            array.append(self.data)
        return(array)

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

    def deleteNode(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.deleteNode(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.deleteNode(val)
        else:
            if self.left == None and self.right == None:
                return(None)
            if self.left == None:
                return(self.right)
            if self.right == None:
                return(self.left)
            
            minVal = self.right.findMin()
            self.data = minVal
            self.right = self.right.delete(minVal)
        return(self)

    def deleteNodeAndChildren(self, val):
        if self.data < val:
            self.right = self.right.deleteNodeAndChildren(val)
            return self
        elif self.data > val:
            self.left = self.left.deleteNodeAndChildren(val)
            return self
        else:
            return None

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def delete(self):
        if self.left != None:
            self.left.delete() 
        if self.right != None:
            self.right.delete()
        self.right = None
        self.left = None
        self.data = None
        self = None

def removeDuplicatesFromList(array):
    array = list(dict.fromkeys(array))
    return(array)

def buildTree(elements, rootVal = 0):
    elements = removeDuplicatesFromList(elements)
    root = Node(rootVal)
    for i in range(0,len(elements)):
        root.addChild(elements[i])
    return(root)

if __name__ == "__main__":
    numbers = [8,56,13,4,3,5,6,7,-9,155,155,155]
    numbersTree = buildTree(numbers, 7)
    numbersTree.addChild(-14.5)
    numbersTree.display()
    print(numbersTree.rightSideView())
    print(numbersTree.leftSideView())
    print(numbersTree.calculateSum())
    # numbersTree.invertTree()
    numbersTree.display()
    numbersTree.deleteNode(5)
    print("deleted")
    numbersTree.display()
    numbersTree.deleteNodeAndChildren(-9)
    numbersTree.display()
    numbersTree.addChild(154)
    numbersTree.addChild(156)
    print(numbersTree.getLeaves())
    # numbersTree.delete()
    # numbersTree.display()