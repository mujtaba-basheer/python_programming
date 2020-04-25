import dir_wt_graph

class DAG(dir_wt_graph.DirectedWeightedGraph):
    def __init__(self):
        super().__init__()
        self.parent = None
        self.order = None
        self.topological_sort()

    def topological_sort(self):
        self.order = list()
        self.parent = dict()
        self.DFS()
        self.order.reverse()

    def DFS_Visit(self, s):
        if s not in self.adj:
            self.adj[s] = set()
        for v in self.adj[s]:
            if v not in self.parent:
                self.parent[v] = s
                self.DFS_Visit(v)
        self.order.append(s)

    def DFS(self):
        for s in self.vertices:
            if s not in self.parent:
                self.parent[s] = None
                self.DFS_Visit(s)
        print()

    def shortest_path(self, s = "s"):
        self.initialize(s)
        for u in self.order:
            if u not in self.adj:
                self.adj[u] = set()
            for v in self.adj[u]:
                self.relax(u, v)

    def get_shortest_path(self, u, v):
        self.shortest_path(u)
        return self.d[v]

if __name__ == "__main__":
    pass