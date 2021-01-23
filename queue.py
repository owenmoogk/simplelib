from collections import deque

class Queue:
    
    def __init__(self):
        self.collection = deque()

    def queue(self, data):
        self.collection.appendleft(data)

    def dequeue(self):
        element = self.collection.pop()
        return(element)

    def isEmpty(self):
        if len(self.collection) == 0:
            return(True)
        return(False)

    def size(self):
        return(len(self.collection))
    
    def peek(self):
        return(self.collection[-1])
    
    def display(self):
        print(list(self.collection))

if __name__ == "__main__":
    s = Queue()
    s.queue("elloo")
    s.queue(55)
    s.queue("should be last")
    s.display()
    s.dequeue()
    s.display()