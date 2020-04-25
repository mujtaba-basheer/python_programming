import dir_graph

class Graph(dir_graph.DirectedGraph):
    def __init__(self):
        super().__init__()

def DFS_Visit(Adj = dict(), s = ""):
    if s not in Adj:
        Adj[s] = set()
    for v in Adj[s]:
        if v not in parent:
            parent[v] = s
            DFS_Visit(Adj, v)
    print(s, end = " ")

def DFS(V = set(), Adj = dict()):
    global parent
    for s in V:
        if s not in parent:
            parent[s] = None
            DFS_Visit(Adj, s)
    print()


if __name__ == "__main__":
    graph = Graph()
    parent = dict()
    DFS(graph.vertices, graph.adj)
    

