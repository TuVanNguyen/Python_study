class Vertex:
    def __init__(self, key):
        self.key = key
        self.edges = {}

    def addNeighbor(self, vertex: 'Vertex', weight=1):
        self.edges[vertex] = weight


    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
class Graph:
    def __init__(self):
        self.vertexList = {}

    def addVertex(self,key):
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertexList:
            return self.vertexList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertexList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertexList:
            nv = self.addVertex(f)
        if t not in self.vertexList:
            nv = self.addVertex(t)
        self.vertexList[f].addNeighbor(self.vertexList[t], weight)

    def getVertices(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())

    
        