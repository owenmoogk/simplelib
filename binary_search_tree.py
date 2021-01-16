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
        returnList = []
        if self is None:
            return(returnList)
        if level == 1:
            returnList.append(self.data)
            return(returnList)
        elif level > 1:
            if self.left:
                returnList += (self.left.getLevel(level-1))
            if self.right:
                returnList += (self.right.getLevel(level-1))
        return(returnList)

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

def removeDuplicatesFromList(array):
    array = list(dict.fromkeys(array))
    return(array)

def buildTree(elements, rootVal = 0):
    elements = removeDuplicatesFromList(elements)
    root = Node(rootVal)
    for i in range(0,len(elements)):
        root.addChild(elements[i])
    return(root)