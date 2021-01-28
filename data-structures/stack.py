from collections import deque

class Stack:
    
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        self.stack.append(data)

    def remove(self):
        element = self.stack.pop()
        return(element)

    def isEmpty(self):
        if len(self.stack) == 0:
            return(True)
        return(False)

    def size(self):
        return(len(self.stack))
    
    def peek(self):
        return(self.stack[-1])
    
    def display(self):
        print(list(self.stack))

def reverse_string(string):
    reverseString = Stack()
    for i in string:
        reverseString.push(i)
    returnString = ''
    while reverseString.size() > 0:
        returnString += reverseString.remove()
    return(returnString)

if __name__ == "__main__":
    s = Stack()
    s.push("elloo")
    s.push(55)
    s.display()
    s.remove()
    s.display()
    print(s.isEmpty())
    print(s.size())
    s.remove()
    print(s.isEmpty())
    print(reverse_string("hello my name is owen"))