class Node:

    def __init__(self, data):
        self.children = []
        self.parent = None
        self.data = data

    def addChild(self, child):
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

    laptop = Node("Laptop")
    laptop.addChild(Node("Mac"))
    laptop.addChild(Node("Surface"))
    laptop.addChild(Node("Thinkpad"))

    cellphone = Node("Cell Phone")
    cellphone.addChild(Node("iPhone"))
    cellphone.addChild(Node("Google Pixel"))
    cellphone.addChild(Node("Vivo"))

    tv = Node("TV")
    tv.addChild(Node("Samsung"))
    tv.addChild(Node("LG"))

    root.addChild(laptop)
    root.addChild(cellphone)
    root.addChild(tv)

    root.printTree()

if __name__ == "__main__":
    buildProductTree()