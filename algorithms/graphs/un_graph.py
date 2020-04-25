class UndirectedGraph:
    def __init__(self):
        self.vertices = None
        self.edges = None
        self.adj = None

        self.inputVertices()
        self.inputEdges()

    def inputVertices(self):
        self.vertices = set(map(str, input().split()))

    def inputEdges(self):
        edgeList = list(map(str, input().split()))

        self.edges = set()
        self.adj = dict()

        for edge in edgeList:
            vertices = list(map(str, edge.split(",")))
            self.edges.add(tuple(vertices))

            if vertices[0] not in self.adj:
                self.adj[vertices[0]] = set()
            self.adj[vertices[0]].add(vertices[1])

            if vertices[1] not in self.adj:
                self.adj[vertices[1]] = set()
            self.adj[vertices[1]].add(vertices[0])

    def printVertices(self):
        print(self.vertices)

    def printEdges(self):
        print(self.edges)

    def printAdj(self):
        print(self.adj)

# if __name__ == "__main__":
#     graph = UndirectedGraph()
#     graph.printVertices()
#     graph.printEdges()
#     graph.printAdj()