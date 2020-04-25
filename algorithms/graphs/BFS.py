import un_graph

class Graph(un_graph.UndirectedGraph):
    def __init__(self):
        super().__init__()

def BFS(Adj = dict(), s = ""):
    level = { s: 0 }
    parent = { s: None }

    i = 1
    frontier = [s,]
    while frontier:
        next = list()
        for u in frontier:
            for v in Adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        
        frontier = next
        i += 1

if __name__ == "__main__":
    graph = Graph()
    BFS(graph.vertices, graph.adj, "d")

