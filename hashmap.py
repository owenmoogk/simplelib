class hashTable:
    def __init__(self, len = 100):
        self.max = len
        # setting 100 values to an array
        self.arr = [[] for i in range(self.max)]

    def getHash(self, key):
        h = 0
        for character in key:
            h += ord(character)
        return(h % self.max)
    
    def __setitem__(self, key, value):
        h = self.getHash(key)

        for i in self.arr[h]:
            if i[0] == key:
                i = [key, value]
                return
        self.arr[h].append([key, value])

    def __getitem__(self, key):
        h = self.getHash(key)

        for i in self.arr[h]:
            if i[0] == key:
                return(i[1])
        return(None)

    def __delitem__(self, key):
        h = self.getHash(key)

        for i in range(0,len(self.arr[h])):
            if self.arr[h][i][0] == key:
                self.arr[h].pop(i)
                return

if __name__ == "__main__":
    t = hashTable()
    t["march 6"] = 130
    t["march 6"] = 20
    t["april 2"] = "45 degrees"
    t["april 3"] = "23 degrees"
    print(t["march 6"])
    print(t["april 2"])