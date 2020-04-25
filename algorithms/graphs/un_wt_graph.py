class UndirectedWeightedGraph(object):

    def __init__(self):
        self.vertices = None
        self.edges = None
        self.adj = None
        self.weights = None
        self.d = None
        self.predecessor = None

        self.inputVertices()
        self.inputEdgesAndWeights()

    def inputVertices(self):
        self.vertices = set(map(str, input().split()))

    def inputEdgesAndWeights(self):
        edgeList = list(map(str, input().split()))

        self.edges = set()
        self.adj = dict()
        self.weights = dict()

        for edge_wt in edgeList:
            args = list(map(str, edge_wt.split(",")))
            edge1 = (args[0], args[1])
            edge2 = (args[1], args[0])
            weight = int(args[2])

            self.edges.add(edge1)

            if args[0] not in self.adj:
                self.adj[args[0]] = set()
            self.adj[args[0]].add(args[1])
            if args[1] not in self.adj:
                self.adj[args[1]] = set()
            self.adj[args[1]].add(args[0])

            self.weights[edge1] = weight
            self.weights[edge2] = weight

    def initialize(self, s = ""):
        self.d = dict()
        self.predecessor = dict()

        for v in self.vertices:
            if v == s:
                self.d[v] = 0
            else:
                self.d[v] = float('inf')

            self.predecessor[v] = None

    def relax(self, u, v):
        edge = (u, v)
        if self.d[v] > self.d[u] + self.weights[edge]:
            self.d[v] = self.d[u] + self.weights[edge]
            self.predecessor[v] = u
            return self.d[u] + self.weights[edge]
        return False

    def check_init(self):
        if self.d is None:
            raise ValueError("Source not initialized yet")

    def enumerate(self):
        self.check_init()
        print("Sl. No.\t|\tVertice\t|\tShortest Path\n")
        print()
        i = 1
        for v in self.vertices:
            print(f"{i}\t|\t{v}\t|\t{self.d[v]}")
            i += 1

    def printVertices(self):
        print(self.vertices)

    def printEdges(self):
        print(self.edges)

    def printAdj(self):
        print(self.adj)

    def printWts(self):
        print(self.weights)

if __name__ == "__main__":
    pass