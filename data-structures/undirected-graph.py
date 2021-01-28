class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.graphDict = {}
        for start, end in self.edges:
            if start in self.graphDict:
                if end not in self.graphDict[start]:
                    self.graphDict[start].append(end)
            else:
                self.graphDict[start] = [end]

            if end in self.graphDict:
                if start not in self.graphDict[end]:
                    self.graphDict[end].append(start)
            else:
                self.graphDict[end] = [start]

    def getPaths(self, start, end, path=[]):
        path = path + [start] # path holds the current path
        if start == end: # break case
            return [path]
        if start not in self.graphDict: # if there are no outgoing flights
            return []
        paths = [] # paths holds all possible paths
        for node in self.graphDict[start]:
            if node not in path: # prevents circular loops
                new_paths = self.getPaths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return(paths)

    def getShortestPath(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return(path)
        if start not in self.graphDict:
            return(None)
        shortestPath = None
        for node in self.graphDict[start]:
            if node not in path: # prevents circular loops
                newpath = self.getShortestPath(node, end, path)
                if newpath:
                    if shortestPath is None or len(newpath) < len(shortestPath):
                        shortestPath = newpath
        return(shortestPath)
    
    def addNode(self, start, end):
        if start in self.graphDict:
            if end not in self.graphDict[start]:
                self.graphDict[start].append(end)
        else:
            self.graphDict[start] = [end]

        if end in self.graphDict:
            if start not in self.graphDict[end]:
                self.graphDict[end].append(start)
        else:
            self.graphDict[end] = [start]

    def addEdge(self, start, end):
        if start in self.graphDict:
            if end not in self.graphDict[start]:
                self.graphDict[start].append(end)
        else:
            self.graphDict[start] = [end]

        if end in self.graphDict:
            if start not in self.graphDict[end]:
                self.graphDict[end].append(start)
        else:
            self.graphDict[end] = [start]

    def deleteEdge(self, start, end):
        if start in self.graphDict:
            if end in self.graphDict[start]:
                self.graphDict[start].remove(end)
                if len(self.graphDict[start]) == 0:
                    del self.graphDict[start]
        if end in self.graphDict:
            if start in self.graphDict[end]:
                self.graphDict[end].remove(start)
                if len(self.graphDict[end]) == 0:
                    del self.graphDict[end]

    def deleteNode(self, node):
        toDelete = []
        if node in self.graphDict:
            del self.graphDict[node]
        for key in self.graphDict:
            if node in self.graphDict[key]:
                self.graphDict[key].remove(node)
                if len(self.graphDict[key]) == 0:
                    toDelete.append(key)
        for key in toDelete:
            del(self.graphDict[key])

    def displayGraph(self):
        print()
        for key in self.graphDict:
            print(key, "--", self.graphDict[key])
        print()

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Toronto"),
        ("Paris", "Toronto"),
    ]

    routeGraph = Graph(routes)
    routeGraph.addNode("Toronto", "Ottawa")
    routeGraph.addNode("Paris", "Violet")
    routeGraph.addEdge("Violet", "Toronto")
    routeGraph.addNode("Violet", "Ottawa")
    routeGraph.displayGraph()
    print(routeGraph.getShortestPath("Mumbai", "Ottawa"))
    print(routeGraph.getPaths("Mumbai", "Ottawa"))
    # routeGraph.deleteEdge("Violet", "Ottawa")
    routeGraph.deleteNode("Ottawa")
    routeGraph.displayGraph()
    # routeGraph.deleteNode("Ottawa")
    # routeGraph.displayGraph()
    # routeGraph.deleteEdge("New York", "Toronto")
    # routeGraph.displayGraph()
    # print(routeGraph.getShortestPath("Mumbai", "Ottawa"))