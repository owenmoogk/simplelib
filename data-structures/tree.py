class Node:

    def __init__(self, data, parent = None):
        self.children = []
        self.parent = parent
        self.data = data
        if parent:
            self.parent.children.append(self)

    def addChild(self, data):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return(level)

    def printTree(self, level = -2):
        if level == -1:
            return
        spaces = "   " * self.getLevel()
        print(spaces + self.data)
        for child in self.children:
            child.printTree(level - 1)

def buildProductTree():
    root = Node("Electronics")

    laptop = Node("Laptop", root)
    Node('Macbook', laptop)
    Node("Surface", laptop)
    Node('Thinkpad', laptop)

    cellphone = Node("Cell Phone", root)
    Node('IPhone', cellphone)
    Node("Pixel", cellphone)
    Node('Vivo', cellphone)

    tv = Node("TV", root)
    Node("LG", tv)
    Node('Samsung', tv)

    root.printTree()

if __name__ == "__main__":
    buildProductTree()
